# Generated by Django 5.0.6 on 2024-06-07 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_companies_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='company_logos'),
        ),
    ]