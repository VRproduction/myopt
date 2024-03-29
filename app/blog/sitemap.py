from django.contrib.sitemaps import Sitemap
from . models import *
from django.urls import reverse


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'
    
    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.date
    
    def location(self, obj):
        return obj.get_absolute_url()


class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Service.objects.all()

    def location(self, obj: Service) -> str:
        return obj.get_absolute_url()


class ArticleCategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return ArticleCategory.objects.all()

    def location(self, obj: ArticleCategory) -> str:
        return obj.get_absolute_url()


class StaticSitemap(Sitemap):

    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            'index', 'about', 'gallery',
            'appointment', 'services', 'blogs', 'contact',
        ]

    def location(self, item):
        return reverse(item)
