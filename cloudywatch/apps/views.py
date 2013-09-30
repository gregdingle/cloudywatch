from utils.views import render_to

@render_to('template.html')
def my_view(request):
    return {}

