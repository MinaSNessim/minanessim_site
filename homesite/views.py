from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import SubscribeToNewsletter, Portfolio, BlogPosts
from .forms import SubscriberForm, ContactForm, PortfolioForm
from django.core.mail import send_mail
import os
from datetime import datetime



# Create your views here.
def home(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()

    countries_visited = 8 + 1 + 1 + 3 + 5 + 3 + 3 + 2 + 1
    cups_of_coffee = 21300 + (datetime.now() - datetime(2023, 1, 12)).days * 5
    reports = 10000
    years_of_experience = datetime.now().year - 2009

    specific_ids = [4, 9, 11]
    specific_portfolio = Portfolio.objects.filter(id__in=specific_ids)

    context = {'subscriber_form': subscriber_form, 'contact_form': contact_form,
               'cups_of_coffee': cups_of_coffee, 'countries_visited': countries_visited,
               'reports': reports, 'years_of_experience': years_of_experience, 'choices': Portfolio.choices,
               'portfolio': Portfolio.objects.all().order_by('-id'), 'blog_choices': BlogPosts.choices,
               'blogs': BlogPosts.objects.all().order_by('-id'), 'specific_portfolio': specific_portfolio
               }
    return render(request, 'home.html', context)


def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)

    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio, 'subscriber_form': subscriber_form,
                                                     'contact_form': contact_form})


def blog_detail(request, blog_id):
    blogpost = get_object_or_404(BlogPosts, pk=blog_id)

    subscriber_form = SubscriberForm()
    contact_form = ContactForm()

    return render(request, 'blog_detail.html', {'blogpost': blogpost, 'subscriber_form': subscriber_form,
                                                'contact_form': contact_form})


def handle_subscription(request):
    if request.method == 'POST':
        subscribe_form = SubscriberForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            messages.success(request, 'You have subscribed to our Newsletter, Thank you!')
        else:
            for field, errors in subscribe_form.errors.items():
                for error in errors:
                    messages.warning(request, f'Error in {field.capitalize()} field: {error}')
    return redirect(f"{request.META.get('HTTP_REFERER', 'home')}#contact")

    # Saves the form data to the database
#           return redirect(reverse('home') + '#footer')  # Redirect after successful subscription
#    return redirect('home')  # Redirect in case of invalid form or GET request


def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            message_email = request.POST['email']
            message_subject = request.POST['subject']
            message_message = request.POST['message']

            contact_form.save()
            send_mail(message_subject, message_message, message_email, ['mina.nessim@datasieger.com'])
            messages.success(request, 'Your message has been sent. Thank you!')
        else:
            for field, errors in contact_form.errors.items():
                for error in errors:
                    messages.warning(request, f'Error in {field.capitalize()} field: {error}')
    return redirect(f"{request.META.get('HTTP_REFERER', 'home')}#contact")

#            return redirect(reverse('home') + '#contact')  # Redirect after successful subscription
#    return redirect('home')  # Redirect in case of invalid form or GET request


def error_404(request, exception):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, '404.html', {'subscriber_form': subscriber_form, 'contact_form': contact_form}, status=404)


def e404(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, '404.html', {'subscriber_form': subscriber_form, 'contact_form': contact_form}, )



def about(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()

    try:
        image_dir = 'static/img/certificates'
        image_list = os.listdir(image_dir)

    except:
        image_dir = '/home/msnessim/minanessim_site/static/img/certificates'
        image_list = os.listdir(image_dir)

    countries_visited = 8 + 1 + 1 + 3 + 5 + 3 + 3 + 2 + 1
    cups_of_coffee = 21300 + (datetime.now() - datetime(2023, 1, 12)).days * 5
    rubix_puzzles = 1500 + (datetime.now() - datetime(2023, 1, 12)).days
    years_of_experience = datetime.now().year - 2009

    return render(request, 'about.html', {'subscriber_form': subscriber_form,
                                          'contact_form': contact_form, 'image_list': image_list,
                                          'cups_of_coffee': cups_of_coffee, 'countries_visited': countries_visited,
                                          'rubix_puzzles': rubix_puzzles, 'years_of_experience': years_of_experience})


def blog(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, 'blog.html', {'subscriber_form': subscriber_form, 'contact_form': contact_form,
                                         'blog_choices': BlogPosts.choices,
                                         'blogs': BlogPosts.objects.all().order_by('-id')})


def contact(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, 'contact.html', {'subscriber_form': subscriber_form, 'contact_form': contact_form})


def services(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, 'services.html', {'subscriber_form': subscriber_form, 'contact_form': contact_form})


def courses(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, 'courses.html', {'subscriber_form': subscriber_form, 'contact_form': contact_form})


def projects(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, 'projects.html', {'subscriber_form': subscriber_form, 'contact_form': contact_form})


def training(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, 'training_service.html', {'subscriber_form': subscriber_form, 'contact_form': contact_form})


def erp(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, 'erp_service.html', {'subscriber_form': subscriber_form, 'contact_form': contact_form})


def digital(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, 'digital_service.html', {'subscriber_form': subscriber_form, 'contact_form': contact_form})


def casestudy(request):
    subscriber_form = SubscriberForm()
    contact_form = ContactForm()
    return render(request, 'casestudy.html', {'choices': Portfolio.choices,
                                              'portfolio': Portfolio.objects.all().order_by('-id'),
                                              'subscriber_form': subscriber_form, 'contact_form': contact_form })


'''
def portfolio(request):
    subscriber_form = SubscriberForm()

    return render(request, 'portfolio.html', {'subscriber_form': subscriber_form})

class Protfoliopage(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
'''
