from django.db import models

class Companies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='company_logos')
    website=models.URLField(max_length=200, default='https://www.google.com/')

    def __str__(self):
        return self.name

