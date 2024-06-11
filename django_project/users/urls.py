from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('review/<empresa_id>/<empresa_name>/', views.review, name='review'),
    path('new-review/<empresa_id>/<empresa_name>/', views.newReview, name='new-review'),
]
