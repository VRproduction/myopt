from django.db import models
from ckeditor.fields import RichTextField
from .helper import seo
from django.urls import reverse
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _
from datetime import date


class IndexSlider(models.Model):
    little_title = models.CharField(max_length=500)
    big_title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.FileField(upload_to="slider_images")

    class Meta:
        verbose_name = "Index Slider"
        verbose_name = "Index Sliders"


class WhoWeAre(models.Model):
    title = models.CharField(max_length=500)
    text = RichTextField()

    experience = models.IntegerField()
    image = models.FileField()
    title1 = models.CharField(max_length=200, null=True)
    title2 = models.CharField(max_length=200, null=True)

    slug = models.SlugField(
        _('Slug'),
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Who We Are"
        verbose_name_plural = "Who We Are"









class WhoTitle1(models.Model):
    name = models.CharField(max_length=200)
    who1 = models.ForeignKey(
        WhoWeAre, on_delete=models.CASCADE, related_name="title_1")

    class Meta:
        verbose_name = "Title 1"
        # verbose_name_plural = "Title 2"
        verbose_name_plural = "Title 1"


class WhoTitle2(models.Model):
    name = models.CharField(max_length=200)
    who2 = models.ForeignKey(
        WhoWeAre, on_delete=models.CASCADE, related_name="title_2")

    class Meta:
        verbose_name = "Title 2"
        verbose_name_plural = "Title 2"


class Service(models.Model):
    image = models.ImageField(upload_to="Services", null=True)
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=300)
    slug = models.SlugField(editable=False, null=True, unique=True)
    text = RichTextField()

    service_banner = models.ImageField(upload_to="service_banner", null=True)
    order = models.IntegerField(('sıra'), default=0, )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={"slug": self.slug})


class ServiceOffers(models.Model):
    title = models.CharField(max_length=200)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="offers")


class WhyUs(models.Model):
    title = models.CharField(max_length=300)
    # text = models.TextField()
    video_link = models.TextField(null=True)
    video_image = models.ImageField(upload_to="VideoImage", null=True)
    text = RichTextField()

    class Meta:
        verbose_name = "Why Us"
        verbose_name_plural = "Why Us"


class WhyOffers(models.Model):
    title = models.CharField(max_length=300)
    # text = models.TextField()
    text = RichTextField()

    why = models.ForeignKey(
        WhyUs, on_delete=models.CASCADE, related_name="offers")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"


class Testimonial(models.Model):
    text = RichTextField()

    # text = models.TextField()
    author = models.CharField(max_length=300)
    position = models.CharField(max_length=300)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


class Appointment(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    date = models.CharField(max_length=300, null=True)
    phone = models.CharField(max_length=20, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.email


class Gallery(models.Model):
    # image = ResizedImageField(size=[410, 410], upload_to='galleries', blank=True, null=True)
    image = models.FileField(upload_to="galleries")
    link = models.CharField(max_length=3000)
    link_name = models.CharField(max_length=300)

    def __str__(self):
        return self.link_name


class ArticleCategory(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(editable=False, null=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(ArticleCategory, self).save(*args, **kwargs)
        self.slug = seo(self.name)
        super(ArticleCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={"slug": self.slug})


class Article(models.Model):
    # author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name="article",null=True)
    title = models.CharField(max_length=300, unique=True)
    image = models.FileField(upload_to="Article")
    context = RichTextField()
    slug = models.SlugField(editable=False, null=True, unique=True)
    click = models.PositiveIntegerField(default=0, editable=False)
    category = models.ForeignKey(
        ArticleCategory, on_delete=models.CASCADE, related_name="articles", null=True)
    article_banner = models.ImageField(upload_to="article_banner", null=True)
    order = models.IntegerField(('sıra'), default=0, )
    # date = models.DateField(auto_now_add=True)
    date = models.DateField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        self.slug = seo(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={"slug": self.slug})


class GeneralSettings(models.Model):

    site_title = models.CharField(
        max_length=1500, verbose_name="Saytın başlığı")
    email = models.CharField(
        max_length=1500, verbose_name="Email", null=True, blank=True)
    number_1 = models.CharField(
        max_length=1500, verbose_name="Nömrə", null=True, blank=True)
    number_2 = models.CharField(
        max_length=1500, verbose_name="Nömrə", null=True, blank=True)
    number_3 = models.CharField(
        max_length=1500, verbose_name="Nömrə", null=True, blank=True)

    adress = models.CharField(max_length=1500, verbose_name="Ünvan", null=True)
    g_adress = models.CharField(
        max_length=1500, verbose_name="Google Map linki", null=True, blank=True)
    logo = models.FileField(verbose_name="logo(138x35)",
                            blank=True, upload_to="general_settings")
    favicon = models.FileField(verbose_name="favicon(100x100)",
                               blank=True, null=True, upload_to="general_settings")

    footer_logo = models.FileField(verbose_name="Footer logo(150x38)",
                                   help_text="Saytın aşağısındakı logo", blank=True, null=True, upload_to="general_settings")

    mobile_logo = models.FileField(verbose_name="Mobile logo(150x38)",
                                   help_text="Mobile logo", blank=True, null=True, upload_to="general_settings")

    facebook = models.CharField(
        max_length=1500, verbose_name="Facebook", blank=True)
    # linkedin = models.CharField(max_length=1500, verbose_name="Linkedin", blank=True)
    instagram = models.CharField(
        max_length=1500, verbose_name="Instagram", blank=True)
    youtube = models.CharField(
        max_length=1500, verbose_name="Youtube", blank=True)
    tiktok = models.CharField(
        max_length=1500, verbose_name="TikTok", blank=True)

    footer_text = models.TextField(verbose_name="Footer Ucun tekst", null=True)

    def __str__(self):
        return ('%s') % (self.site_title)

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "General Settings"
        # ordering = ['-id']


class AboutOffers(models.Model):
    image = models.ImageField(upload_to="AboutOffers")
    title = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email


class Certificate(models.Model):
    # certificate_image = ResizedImageField(size=[410, 410], upload_to='certificate_images', blank=True, null=True)
    certificate_image = models.FileField(upload_to="certificate_image")


