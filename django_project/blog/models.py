from django.db import models


class Companies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='company_logos')

    def __str__(self):
        return self.name

