from django.http import HttpResponse
def demo_view(request):
    return HttpResponse("Hello, this is a demo view!")