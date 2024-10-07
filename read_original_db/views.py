from django.shortcuts import render
from . models import LlxdxProjet

# Create your views here.
def index (request):
    context = {
        'projects': LlxdxProjet.objects.all().using('dolibar')
    }
    return render(request,'ejemplo.html', context )