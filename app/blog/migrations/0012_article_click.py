# Generated by Django 4.2 on 2023-04-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='click',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
