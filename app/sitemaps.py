from django.contrib.sitemaps import Sitemap
from app.blog.models import *


class WhoWeAreSitemap(Sitemap):
    changefreq = "monthly"
    priorty = 0.6

    def items(self):
        return WhoWeAre.objects.all()

    def location(self, obj: WhoWeAre) -> str:
        return obj.get_absolute_url()


class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priorty = 0.6

    def items(self):
        return Article.objects.all()

    def location(self, obj: Article) -> str:
        return obj.get_absolute_url()


class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priorty = 0.6

    def items(self):
        return Service.objects.all()

    def location(self, obj: Service) -> str:
        return obj.get_absolute_url()