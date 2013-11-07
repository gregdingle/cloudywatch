from django.shortcuts import get_object_or_404

from .models import Comparison
from utils.views import render_to


@render_to('comparitions/detail.html')
def detail(request, comparison_slug):
    comparison = get_object_or_404(Comparison, slug=comparison_slug)
    return {
        'comparison': comparison,
    }
