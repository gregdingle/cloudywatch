from .models import Comparison


def comparisons(request):
    return {
        'comparisons': Comparison.objects.all()
    }
