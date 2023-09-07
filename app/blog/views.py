from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from blog.models import *
from blog.forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.views import *
from django.urls import translate_url
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404


def set_language(request, lang_code):
    url = request.META.get("HTTP_REFERER", None)
    if lang_code == 'az':
        return HttpResponseRedirect('/')
    else:
        response = redirect(translate_url(url, lang_code))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response


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

    form = AppointmentForm(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')

        data = {
            'name': name,
            'email': email,
            'date': date,
        }

        # data = f'Name: {name}, Email: {email}, Date: {date}'
        # form = AppointmentForm()

        text_to_doctor = render_to_string('to_mail_2.html', data)

        send_mail(
            "Sizə gulshendikmen.az saytından müraciət gəlib",
            # data,
            text_to_doctor,
            settings.EMAIL_HOST_USER,
            ['info@gulshendikmen.az'],
            fail_silently=False, html_message=text_to_doctor
        )
        messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
        return redirect(request.META['HTTP_REFERER'])

    """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = AppointmentForm()
    """
    homePage_Description_Edit = HomePage_Description_Edit.objects.all()
    homePage_Keyword_Edit = HomePage_Keyword_Edit.objects.all()
    homePage_Title_Edit = HomePage_Title_Edit.objects.all()
    head_seo_content = HeadSeoContent.objects.all()
    body_seo_content = BodySeoContent.objects.all()
    context["head_seo_content"] = head_seo_content
    context["body_seo_content"] = body_seo_content
    context["form"] = form
    context["sliders"] = sliders
    context["whoweare"] = whoweare
    context["services"] = services
    context["whyus"] = whyus
    context["testimonials"] = testimonials
    context["galleries"] = galleries
    context["articles"] = articles
    context["offers"] = offers
    context['home_title'] = homePage_Title_Edit
    context['home_description'] = homePage_Description_Edit
    context['home_keyword'] = homePage_Keyword_Edit
    return render(request, "index.html", context)



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
    head_seo_content = HeadSeoContent.objects.all()
    body_seo_content = BodySeoContent.objects.all()
    context["head_seo_content"] = head_seo_content
    context["body_seo_content"] = body_seo_content
    context["galleries"] = galleries
    context["certificates"] = certificates

    return render(request, "gallery.html", context)


def about(request):
    context = {}

    whoweare = WhoWeAre.objects.all()
    services = Service.objects.all()
    whyus = WhyUs.objects.all()
    offers = AboutOffers.objects.all()
    head_seo_content = HeadSeoContent.objects.all()
    body_seo_content = BodySeoContent.objects.all()
    context["head_seo_content"] = head_seo_content
    context["body_seo_content"] = body_seo_content
    context["whyus"] = whyus
    context["whoweare"] = whoweare
    context["services"] = services
    context["offers"] = offers

    # return render(request,"about.html",context)
    return render(request, "about.html", context)



def services(request):
    context = {}
    services_title = Services_Title_Edit.objects.all()
    services_description = Services_Description_Edit.objects.all()
    services_keyword = Services_Keyword_Edit.objects.all()
    head_seo_content = HeadSeoContent.objects.all()
    body_seo_content = BodySeoContent.objects.all()
    context["head_seo_content"] = head_seo_content
    context["body_seo_content"] = body_seo_content
    context["services_title"] = services_title
    context["services_description"] = services_description
    context["services_keyword"] = services_keyword
    services = Service.objects.all()

    context["services"] = services

    return render(request, "services.html", context)


def service_detail(request, slug):
    context = {}
    head_seo_content = HeadSeoContent.objects.all()
    body_seo_content = BodySeoContent.objects.all()
    context["head_seo_content"] = head_seo_content
    context["body_seo_content"] = body_seo_content
    service = get_object_or_404(Service, slug=slug)

    services = Service.objects.all()

    context["service"] = service
    context["services"] = services

    return render(request, "service_detail.html", context)























def contact(request):
    head_seo_content = HeadSeoContent.objects.all()
    body_seo_content = BodySeoContent.objects.all()
    contact_form = ContactForm(request.POST)
    contact_seo = ContactSeo.objects.last()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message,

        }

        # data = f'Name: {name}, Email: {email}, Phone: {phone}, Message:{message}, Subject: {subject}'
        # form = ContactForm()

        text_to_doctor = render_to_string('to_mail.html', data)

        send_mail(
            "Sizə gulshendikmen.az saytından müraciət gəlib",
            text_to_doctor,
            settings.EMAIL_HOST_USER,
            ['info@gulshendikmen.az'],
            fail_silently=False, html_message=text_to_doctor
        )
        messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
        return redirect(request.META['HTTP_REFERER'])
    
    
    context = {
        'contact_form': contact_form
               }
    context['contact_seo'] = contact_seo
    context["head_seo_content"] = head_seo_content
    context["body_seo_content"] = body_seo_content
    return render(request, "contact.html", context=context)



























def appointment(request):
    # context = {}
    form = Appointment2Form(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': date,
            'message': message,

        }

        # data = f'Name: {name}, Email: {email}, Phone: {phone}, Message:{message}, Subject: {subject}'
        # form = ContactForm()

        text_to_doctor = render_to_string('to_mail_3.html', data)

        send_mail(
            "Sizə gulshendikmen.az saytından müraciət gəlib",
            text_to_doctor,
            settings.EMAIL_HOST_USER,
            ['info@gulshendikmen.az'],
            fail_silently=False, html_message=text_to_doctor
        )
        messages.success(request, 'Sizin müraciətiniz uğurla göndərildi !')
        return redirect(request.META['HTTP_REFERER'])
    
    context = {
        'form': form
    }
    head_seo_content = HeadSeoContent.objects.all()
    body_seo_content = BodySeoContent.objects.all()
    context["head_seo_content"] = head_seo_content
    context["body_seo_content"] = body_seo_content
    return render(request, "appointment.html", context)








def blogs(request):
    context = {}
    blogs = Article.objects.all()
    bloq_keyword = Bloq_Keyword_Edit.objects.all()
    bloq_title = Bloq_Title_Edit.objects.all()
    bloq_description = Bloq_Description_Edit.objects.all()
    head_seo_content = HeadSeoContent.objects.all()
    body_seo_content = BodySeoContent.objects.all()

    context["head_seo_content"] = head_seo_content
    context["body_seo_content"] = body_seo_content
    context["bloq_keyword"] = bloq_keyword
    context["bloq_title"] = bloq_title
    context["bloq_description"] = bloq_description
    context["blogs"] = blogs
    return render(request, "blog.html", context)


def blog_detail(request, slug):
    context = {}
    head_seo_content = HeadSeoContent.objects.all()
    body_seo_content = BodySeoContent.objects.all()
    context["head_seo_content"] = head_seo_content
    context["body_seo_content"] = body_seo_content
    blog = get_object_or_404(Article, slug=slug)
    latests = Article.objects.all().order_by("-date").exclude(id=blog.id)
    categories = ArticleCategory.objects.all()

    context["blog"] = blog
    context["latests"] = latests
    context["categories"] = categories

    return render(request, "blog_detail.html", context)


def category_detail(request, slug):

    context = {}
    head_seo_content = HeadSeoContent.objects.all()
    body_seo_content = BodySeoContent.objects.all()
    context["head_seo_content"] = head_seo_content
    context["body_seo_content"] = body_seo_content
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







































