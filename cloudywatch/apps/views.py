from django.shortcuts import get_object_or_404

from utils.views import render_to
from .models import Category, Application


@render_to('apps/index.html')
def index(request):
    return {'featured_categories': Category.objects.all()[:5]}


@render_to('apps/application_list.html')
def application_list(request, category_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        applications = category.application_set.all()
    else:
        category = None
        applications = Application.objects.all()

    return {
        'category': category,
        'applications': applications
    }


@render_to('apps/application_detail.html')
def application_detail(request, category_slug, application_slug):
    application = get_object_or_404(Application, category__slug=category_slug, slug=application_slug)

    return {
        'application': application
    }
