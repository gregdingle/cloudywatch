from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

from .models import Comparison
from utils.views import render_to


@render_to('comparitions/detail.html')
def detail(request, comparison_slug=None):
    print comparison_slug
    comparisons = Comparison.objects.all()
    if comparison_slug:
        comparison = get_object_or_404(Comparison, slug=comparison_slug)
    else:
        try:
            print comparisons[0].get_absolute_url()
            return redirect(comparisons[0])
        except IndexError:
            raise Http404

    return {
        'comparison': comparison,
        'comparisons': comparisons
    }
