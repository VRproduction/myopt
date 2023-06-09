# Generated by Django 4.0.10 on 2023-05-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_service_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_banner',
            field=models.ImageField(null=True, upload_to='article_banner'),
        ),
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.IntegerField(default=0, verbose_name='sıra'),
        ),
    ]
