from modeltranslation.translator import TranslationOptions, register
from blog.models import *


@register(IndexSlider)
class IndexSliderTranslationOptions(TranslationOptions):
    fields = ('little_title', 'big_title', 'description')


@register(WhoWeAre)
class WhoWeAreTranslationOptions(TranslationOptions):
    fields = ("title", "text", "experience", "title1", 'title2')


@register(WhoTitle1)
class WhoTitle1TranslationOptions(TranslationOptions):
    fields = ('name', 'who', )


@register(WhoTitle2)
class WhoTitle2TranslationOptions(TranslationOptions):
    fields = ('name', 'who', )


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'text', )


@register(ServiceOffers)
class ServiceOffersTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(WhyUs)
class WhyUsTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


@register(WhyOffers)
class WhyOffersTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('text', 'author', 'position')


@register(Appointment)
class AppointmentTranslationOptions(TranslationOptions):
    fields = ('name', 'message', )


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('link_name',)


@register(ArticleCategory)
class ArticleCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'context', 'category', )


@register(GeneralSettings)
class GeneralSettingsTranslationOptions(TranslationOptions):
    fields = ('site_title', 'adress', 'footer_text', )


@register(AboutOffers)
class AboutOffersTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('name', 'subject', 'message', )


