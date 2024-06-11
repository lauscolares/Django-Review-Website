from django.shortcuts import render
from django.db.models import Avg
from .models import Companies
from users.models import Review

def home(request):
    companies = Companies.objects.all()
    for empresa in companies:
        empresa.average_avaliação = Review.objects.filter(empresa=empresa).aggregate(Avg('avaliação'))['avaliação__avg']
    context = {
        'companies': companies,
    }
    return render(request, 'blog/home.html', context) 

def about(request): 
    return render(request, 'blog/about.html', {'title': 'About'})
