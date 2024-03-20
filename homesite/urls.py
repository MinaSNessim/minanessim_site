from django.contrib.sitemaps.views import sitemap

from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .sitemaps import StaticSitemap, BlogSitemap, PortfolioSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'static': StaticSitemap, #add StaticSitemap to the dictionary
    'blog': BlogSitemap, #add DynamicSitemap to the dictionary
    'portfolio': PortfolioSitemap
}

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
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('training/', views.training, name='training'),
    path('erp/', views.erp, name='erp'),
    path('digital/', views.digital, name='digital'),
    path('casestudy/', views.casestudy, name='casestudy'),
    path('404/', views.e404, name='e404'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
