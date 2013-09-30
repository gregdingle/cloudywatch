from datetime import datetime
from django.core.management.base import BaseCommand
from pingdom.api import pingdom
from apps.models import Application


class Command(BaseCommand):
    "This command should run every hour and collect latest pingdom data for last hour"
    
    def handle(self, *args, **opts):
        for app in Application.objects.all():
            print 'getting pingdom data for %s(%s)' % (app, app.pingdom_id)
            #FOR now getting 60 latest items, not sure yet how often pingdom check per hour maximum
            for probe in pingdom.get('/results/{0}?limit=60'.format(app.pingdom_id))['results']:
                obj, created = app.pingdom_probes.get_or_create(
                    probeid = int(probe['probeid']),
                    timestamp = datetime.fromtimestamp(probe['time']),
                    defaults = dict(
                        status = probe['status'],
                        responsetime = probe['responsetime']
                    )
                )
                print created, obj.probeid, obj.timestamp
