# Generated by Django 4.2.13 on 2024-06-11 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review", old_name="rating", new_name="avaliação",
        ),
        migrations.RenameField(
            model_name="review", old_name="details", new_name="detalhes",
        ),
        migrations.RenameField(
            model_name="review", old_name="empresa", new_name="empresa",
        ),
        migrations.RenameField(
            model_name="review", old_name="title", new_name="título",
        ),
    ]
