from django.http import HttpResponse
from demo.textile import *

def textile2html(request):
    text = request.POST.get('data','')
    html = Textile().textile(text, sanitize=True)
    return HttpResponse(html)