from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

from .models import Comparison
from utils.views import render_to


@render_to('comparitions/detail.html')
def detail(request, slug=None):
    comparisons = Comparison.objects.all()
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
