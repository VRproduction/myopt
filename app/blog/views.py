from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from blog.models import *
from blog.forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.views import *


def index(request):

    context = {}

    offers = AboutOffers.objects.all()
    whoweare = WhoWeAre.objects.all()
    sliders = IndexSlider.objects.all()
    services = Service.objects.all().order_by('order')[:4]

    whyus = WhyUs.objects.all()
    testimonials = Testimonial.objects.all()
    galleries = Gallery.objects.all()
    articles = Article.objects.all().order_by("-click")

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = AppointmentForm()

    context["form"] = form
    context["sliders"] = sliders
    context["whoweare"] = whoweare
    context["services"] = services
    context["whyus"] = whyus
    context["testimonials"] = testimonials
    context["galleries"] = galleries
    context["articles"] = articles
    context["offers"] = offers

    return render(request, "index.html", context)


"""
def certificate(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificates.html')
"""


def gallery(request):
    context = {}
    galleries = Gallery.objects.all()
    certificates = Certificate.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(galleries, 9)

    try:
        galleries = paginator.page(page)

    except PageNotAnInteger:
        galleries = paginator.page(1)
    except EmptyPage:

        galleries = paginator.page(paginator.num_pages)

    context["galleries"] = galleries
    context["certificates"] = certificates

    return render(request, "gallery.html", context)


def about(request):
    context = {}

    whoweare = WhoWeAre.objects.all()
    services = Service.objects.all()
    whyus = WhyUs.objects.all()
    offers = AboutOffers.objects.all()

    context["whyus"] = whyus
    context["whoweare"] = whoweare
    context["services"] = services
    context["offers"] = offers

    # return render(request,"about.html",context)
    return render(request, "about.html", context)


def services(request):
    context = {}

    services = Service.objects.all()

    context["services"] = services

    return render(request, "services.html", context)


def service_detail(request, slug):
    context = {}

    service = get_object_or_404(Service, slug=slug)

    services = Service.objects.all()

    context["service"] = service
    context["services"] = services

    return render(request, "service_detail.html", context)


def contact(request):
    context = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = ContactForm()

    context["form"] = form
    return render(request, "contact.html", context)


def appointment(request):
    context = {}

    if request.method == 'POST':
        form = Appointment2Form(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = Appointment2Form()

    context["form"] = form

    return render(request, "appointment.html", context)


def blogs(request):
    context = {}
    blogs = Article.objects.all()
    context["blogs"] = blogs
    return render(request, "blog.html", context)


def blog_detail(request, slug):
    context = {}

    blog = get_object_or_404(Article, slug=slug)
    latests = Article.objects.all().order_by("-date").exclude(id=blog.id)
    categories = ArticleCategory.objects.all()

    context["blog"] = blog
    context["latests"] = latests
    context["categories"] = categories

    return render(request, "blog_detail.html", context)


def category_detail(request, slug):

    context = {}

    category = get_object_or_404(ArticleCategory, slug=slug)
    blogs = Article.objects.filter(category_id=category.id)

    page = request.GET.get('page')
    paginator = Paginator(blogs, 6)

    try:
        blogs = paginator.page(page)

    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:

        blogs = paginator.page(paginator.num_pages)

    context["category"] = category
    context["blogs"] = blogs

    return render(request, "category_detail.html", context)


"""
def categories(request):
    context = {}
    article_categories = ArticleCategory.objects.all()
    context["article_categories"] = article_categories
    # return render(request, "services.html", context)
    return HttpResponse('CATEGORIES ARE HERE')

"""
