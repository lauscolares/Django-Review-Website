from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Companies

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Review(models.Model):
    RATING_CHOICES = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )
    título = models.CharField(max_length=100)
    avaliação = models.CharField(max_length=7, choices = RATING_CHOICES, null=True)
    empresa = models.ForeignKey(Companies, on_delete=models.CASCADE, null=True)
    detalhes = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
