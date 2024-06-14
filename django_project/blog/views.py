from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Companies
from users.models import Review
from django.views.decorators.http import require_POST

def home(request):
    empresas = Companies.objects.all().order_by('name')
    query = request.GET.get('search')
    if query:
        request.session['search'] = query
        empresas = Companies.objects.filter(name__icontains=query)
    elif 'search' in request.session:
        query = request.session['search']  # Retrieve the search query from the session
        empresas = Companies.objects.filter(name__icontains=query)
    for empresa in empresas:
        empresa.average_avaliação = Review.objects.filter(empresa=empresa).aggregate(Avg('avaliação'))['avaliação__avg']
    context = {
        'empresas': empresas,
        'search': query,
    }
    return render(request, 'blog/home.html', context) 

def about(request): 
    return render(request, 'blog/about.html', {'title': 'About'})

@require_POST
def clear_search(request):
    if 'search' in request.session:
        del request.session['search']
    return redirect('blog-home')