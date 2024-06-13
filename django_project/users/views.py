from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ReviewForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
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
    return render(request, 'users/profile.html')

# Review views
def review(request, empresa_id, empresa_name):
    context = {
        'review': Review.objects.filter(empresa_id = empresa_id),
        'empresa_id': empresa_id,
        'empresa_name': empresa_name,
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
