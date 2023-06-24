from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns
from blog.views import set_language

# from django.contrib.sitemaps.views import sitemap
# from .sitemap import BlogSitemap, ServiceSitemap, PageSitemap, StaticSitemap


"""
sitemaps = {
    'static': StaticSitemap,
    'blog': BlogSitemap,
    'service': ServiceSitemap,
    'page': PageSitemap,
}

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("blog.urls")),

    path('set_language/<str:lang_code>/', set_language, name="set_lang"),


]


urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False)
    ]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta', include('rosetta.urls'))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
