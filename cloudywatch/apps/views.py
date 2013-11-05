from datetime import datetime, timedelta
import urllib
import xml.etree.ElementTree as ET

import requests

from django.db.models import Avg
from django.utils import simplejson as json
from django.shortcuts import get_object_or_404

from utils.views import render_to
from .forms import FindToolForm
from .models import Category, Application


@render_to('apps/index.html')
def index(request):
    return {'featured_categories': Category.objects.all()[:5]}


@render_to('apps/application_list.html')
def application_list(request, category_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        applications = category.application_set.enabled()
    else:
        category = None
        applications = Application.objects.enabled()

    return {
        'category': category,
        'applications': applications
    }


@render_to('apps/application_detail.html')
def application_detail(request, category_slug, application_slug):
    application = get_object_or_404(Application, category__slug=category_slug, slug=application_slug, enabled=True)

    # TODO: Move the logic to Application model
    datetime_from = datetime.now() - timedelta(days=7)
    pingdom_probes_qs = application.pingdom_probes.filter(timestamp__gt=datetime_from).extra(
        {'date': "strftime('%%Y-%%m-%%d', timestamp)", 'hour': "strftime('%%H', timestamp)"}
    ).values('date', 'hour').annotate(responsetime=Avg('responsetime'))

    pingdom_probes = []
    for p in pingdom_probes_qs:
        date = datetime.strptime(p['date'], '%Y-%m-%d')
        hour_to = int(p['hour'])
        hour_from = hour_to - 1 if hour_to != 0 else 23
        responsetime = int(p['responsetime'])
        tooltip = '%s ms (%s, %s:00 to %s:00)' % (responsetime, date.strftime('%d/%m/%Y'), hour_from, hour_to)
        pingdom_probes.append(
            [date.strftime('%b %d'), responsetime, tooltip]
        )

    return {
        'application': application,
        'pingdom_probes': json.dumps(pingdom_probes),
        'point_size': 0 if len(pingdom_probes) > 30 else 5
    }


@render_to('apps/find_tool.html')
def find_tool(request):
    form = FindToolForm(request.GET or None)
    if form.is_valid():
        application = form.cleaned_data['application']
        app_names = []
        for keyword in ('vs', 'compared to'):
            q = '%s %s' % (application.title.lower(), keyword)
            r = requests.get('http://suggestqueries.google.com/complete/search?output=toolbar&hl=en&%s'
                             % urllib.quote_plus('q=%s' % q, safe='='))
            tree = ET.fromstring(r.text)
            suggestions = [item.get('data') for item in tree.findall('*suggestion')]
            app_names += [s.rpartition(q)[2].strip() for s in suggestions if s != q]
        return {'form': form, 'app_names': set(app_names), 'category': application.category}

    return {'form': form}
