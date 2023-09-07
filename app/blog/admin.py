from django.contrib import admin
from blog.models import *

admin.site.register(HomePage_Description_Edit)
admin.site.register(HomePage_Keyword_Edit)
admin.site.register(HomePage_Title_Edit)
admin.site.register(Bloq_Description_Edit)
admin.site.register(Bloq_Keyword_Edit)
admin.site.register(Bloq_Title_Edit)
admin.site.register(Services_Description_Edit)
admin.site.register(Services_Keyword_Edit)
admin.site.register(Services_Title_Edit)
# Register your models here.
admin.site.register(IndexSlider)
admin.site.register(Testimonial)
admin.site.register(Appointment)
admin.site.register(Gallery)
admin.site.register(AboutOffers)
admin.site.register(Contact)
# admin.site.register(ArticleCategory)
# admin.site.register(Article)
# admin.site.register(Author)
admin.site.register(Certificate)
admin.site.register(HeadSeoContent)
admin.site.register(BodySeoContent)

####################################################################
class Title1Inline(admin.StackedInline):
    model = WhoTitle1
    max_num = 10
    extra = 1
    who = "whotitle1"


class Title2Inline(admin.StackedInline):
    model = WhoTitle2
    max_num = 10
    extra = 1


MAX_OBJECTS = 1


@admin.register(WhoWeAre)
class AdminWhoSettings(admin.ModelAdmin):
    inlines = [Title1Inline,Title2Inline]


    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


###########################################

class ServiceOffersInline(admin.StackedInline):
    model = ServiceOffers
    max_num = 10
    extra = 1


@admin.register(Service)
class AdminGeneralSettings(admin.ModelAdmin):
    inlines = [ServiceOffersInline]
    list_display = ['title', 'order', ]
    # fields = ('title', 'order', 'image')

###########################################################################


class WhyUsOffersInline(admin.StackedInline):
    model = WhyOffers
    max_num = 10
    extra = 1


MAX_OBJECTS = 1

@admin.register(WhyUs)
class AdminGeneralSettings(admin.ModelAdmin):
    inlines = [WhyUsOffersInline]


    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

#########################################################################################


@admin.register(GeneralSettings)
class AdminGeneralSettings(admin.ModelAdmin):


    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)



@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ['title', 'slug', 'order']


@admin.register(ArticleCategory)
class AdminArticleCategory(admin.ModelAdmin):
    list_display = ['name','slug']
