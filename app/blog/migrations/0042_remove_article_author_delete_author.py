# Generated by Django 4.0.10 on 2023-05-23 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_alter_article_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
