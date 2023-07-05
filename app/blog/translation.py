from modeltranslation.translator import TranslationOptions, register, translator
from blog.models import IndexSlider, WhoWeAre, WhoTitle1, WhoTitle2, Service, ServiceOffers, \
    WhyUs, WhyOffers, Testimonial, Appointment , Gallery, ArticleCategory, Article, GeneralSettings, AboutOffers, Contact


# @register(IndexSlider)
class IndexSliderTranslationOptions(TranslationOptions):
    fields = ('little_title', 'big_title', 'description')


translator.register(IndexSlider, IndexSliderTranslationOptions)


# @register(WhoWeAre)
class WhoWeAreTranslationOptions(TranslationOptions):
    fields = ("title", "text", "experience", "title1", 'title2')


translator.register(WhoWeAre, WhoWeAreTranslationOptions)


# @register(WhoTitle1)
class WhoTitle1TranslationOptions(TranslationOptions):
    # fields = ('name', 'who1', )
    fields = ('name', )


translator.register(WhoTitle1, WhoTitle1TranslationOptions)


@register(WhoTitle2)
class WhoTitle2TranslationOptions(TranslationOptions):
    # fields = ('name', 'who2', )
    fields = ('name', )


# @register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'text', )


translator.register(Service, ServiceTranslationOptions)


# @register(ServiceOffers)
class ServiceOffersTranslationOptions(TranslationOptions):
    fields = ('title', )


translator.register(ServiceOffers, ServiceOffersTranslationOptions)


# @register(WhyUs)
class WhyUsTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


translator.register(WhyUs, WhyUsTranslationOptions)


# @register(WhyOffers)
class WhyOffersTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


translator.register(WhyOffers, WhyOffersTranslationOptions)


# @register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('text', 'author', 'position')


translator.register(Testimonial, TestimonialTranslationOptions)


# @register(Appointment)
class AppointmentTranslationOptions(TranslationOptions):
    fields = ('name', 'message', )


translator.register(Appointment, AppointmentTranslationOptions)


# @register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('link_name',)


translator.register(Gallery, GalleryTranslationOptions)


# @register(ArticleCategory)
class ArticleCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(ArticleCategory, ArticleCategoryTranslationOptions)


# @register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'context', 'category', )


translator.register(Article, ArticleTranslationOptions)


# @register(GeneralSettings)
class GeneralSettingsTranslationOptions(TranslationOptions):
    fields = ('site_title', 'adress', 'footer_text', )


translator.register(GeneralSettings, GeneralSettingsTranslationOptions)


# @register(AboutOffers)
class AboutOffersTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


translator.register(AboutOffers, AboutOffersTranslationOptions)


# @register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('name', 'subject', 'message', )


translator.register(Contact, ContactTranslationOptions)
