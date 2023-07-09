from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import ArticleSitemap, ServiceSitemap, ArticleCategorySitemap, StaticSitemap
from django.views.generic import TemplateView
from blog.views import set_language


sitemaps = {
    'article_sitemap': ArticleSitemap,
    'service_sitemap': ServiceSitemap,
    'article_category': ArticleCategorySitemap,
    'static_sitemap': StaticSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('set_language/<str:lang_code>/', set_language, name="set_lang"),

]


urlpatterns += i18n_patterns(
    path('', include("blog.urls")),
    path(
        'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'
    ),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),
    prefix_default_language=False
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
