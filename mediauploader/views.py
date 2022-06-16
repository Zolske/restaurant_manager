from django.shortcuts import render
from .models import media

def home(request):
    pictures = media.objects.all()
    ctx = {'pictures':pictures,
           'hello': 'say hello'}
    return render(request, 'testImage.html', ctx)
# Create your views here.
