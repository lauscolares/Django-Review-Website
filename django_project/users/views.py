from django.shortcuts import render, redirect
from django.contrib import messages
from blog.models import Companies
from django.db.models import Avg
from .forms import UserRegisterForm, ReviewForm, ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Review

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    context = {
        'review': Review.objects.filter(author=request.user),
    }

    return render(request, 'users/profile.html', context)

# Review views
def review(request, empresa_id, empresa_name):
    empresas = Companies.objects.filter(id = empresa_id)
    for empresa in empresas:
        empresa.average_avaliação = Review.objects.filter(empresa=empresa).aggregate(Avg('avaliação'))['avaliação__avg']
        empresa.website = empresa.website    
    context = {
        'review': Review.objects.filter(empresa_id = empresa_id),
        'empresa_id': empresa_id,
        'empresa_name': empresa_name,
        'empresas': empresas,
    }
    return render(request, 'users/review.html', context) 

@login_required
def newReview(request, empresa_id, empresa_name):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.empresa_id = empresa_id
            form.save()
            messages.success(request, f'Sua Avaliação foi salva!')
            return redirect('blog-home')
    else:
        form = ReviewForm()
    return render(request, 'users/reviewForm.html', {'form': form, 'empresa_id': empresa_id, 'empresa_name': empresa_name})
