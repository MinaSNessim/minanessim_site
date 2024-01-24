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

    try:
        image_dir = 'static/img/certificates'
        image_list = os.listdir(image_dir)
    except:
        image_dir ='/home/msnessim/minanessim_site/static/img/certificates'
        image_list = os.listdir(image_dir)

    countries_visited = 8+1+1+3+5+3+3+2+1
    cups_of_coffee = 21300 + (datetime.now() - datetime(2023, 1, 12)).days * 5
    rubix_puzzles = 1500 + (datetime.now() - datetime(2023, 1, 12)).days
    years_of_experience = datetime.now().year - 2009

    context = {'subscriber_form': subscriber_form, 'contact_form': contact_form, 'image_list': image_list,
               'cups_of_coffee': cups_of_coffee, 'countries_visited': countries_visited,
               'rubix_puzzles': rubix_puzzles, 'years_of_experience': years_of_experience, 'choices': Portfolio.choices,
               'portfolio': Portfolio.objects.all().order_by('-id'), 'blog_choices': BlogPosts.choices,
               'blogs': BlogPosts.objects.all().order_by('-id')
               }
    return render(request, 'home.html', context)


def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)

    subscriber_form = SubscriberForm()

    return render(request, 'portfolio_detail.html', {'portfolio': portfolio, 'subscriber_form': subscriber_form})


def blog_detail(request, blog_id):
    blogpost = get_object_or_404(BlogPosts, pk=blog_id)

    subscriber_form = SubscriberForm()

    return render(request, 'blog_detail.html', {'blogpost': blogpost, 'subscriber_form': subscriber_form})


def handle_subscription(request):
    if request.method == 'POST':
        subscribe_form = SubscriberForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()  # Saves the form data to the database
            return redirect(reverse('home') + '#footer')  # Redirect after successful subscription
    return redirect('home')  # Redirect in case of invalid form or GET request


def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('home') + '#contact')  # Redirect after successful subscription
    return redirect('home')  # Redirect in case of invalid form or GET request


def error_404(request, exception):
    return render(request, '404.html', {}, status=404)


def about(request):
    return render(request, 'about.html')


def blog(request):
    subscriber_form = SubscriberForm()
    return render(request, 'blog.html', {'subscriber_form': subscriber_form})


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def courses(request):
    return render(request, 'courses.html')


def projects(request):
    return render(request, 'projects.html')


'''
def portfolio(request):
    subscriber_form = SubscriberForm()

    return render(request, 'portfolio.html', {'subscriber_form': subscriber_form})

class Protfoliopage(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
'''
