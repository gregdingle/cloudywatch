from django.http import Http404
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect

from .models import Comparison
from utils.views import render_to


@render_to('comparitions/detail.html')
def detail(request, slug=None):
    comparisons = Comparison.objects.all()
    # if full_slug:
    #     app_slugs = full_slug.split('/vs/')
    #     qs = comparisons.annotate(total=Count('applications'))
    #     for slug in app_slugs:
    #         qs = qs.filter(applications__slug=slug)
    #     comparison = get_object_or_404(qs, total=len(app_slugs))
    if slug:
        comparison = get_object_or_404(Comparison, slug=slug)
    else:
        try:
            return redirect(comparisons[0])
        except IndexError:
            raise Http404

    return {
        'comparison': comparison,
        'comparisons': comparisons
    }
