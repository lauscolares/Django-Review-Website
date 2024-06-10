from django.shortcuts import render
from .models import Companies

def home(request):
    context = {
        'companies': Companies.objects.all()
    }
    return render(request, 'blog/home.html', context) 

def about(request): 
    return render(request, 'blog/about.html', {'title': 'About'})
