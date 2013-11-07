from .models import Comparison


def comparisons(request):
    return {
        'all_comparisons': Comparison.objects.all()
    }
