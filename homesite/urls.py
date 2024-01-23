from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('courses/', views.courses, name='courses'),
    path('projects/', views.projects, name='projects'),
    # path('portfolio/', views.portfolio, name='portfolio'),
    path('handle_subscription/', views.handle_subscription, name='handle_subscription'),
    path('contact_view/', views.contact_view, name='contact_view'),
    # path('portfolio/', views.Protfoliopage.as_view(), name='portfolio'),
    path('portfolio/<int:portfolio_id>/', views.portfolio_detail, name='portfolio_detail'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail')

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
