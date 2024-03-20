from datetime import datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Portfolio, BlogPosts


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return BlogPosts.objects.all().order_by('id')


    def lastmod(self, obj):
        return obj.subscribed_at

    def location(self, obj):
        return '/blog/%s' % (obj.title.replace(' ', '-'))

class PortfolioSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Portfolio.objects.all().order_by('id')

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return '/portfolio/%s' % (obj.title.replace(' ', '-'))


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['digital', 'about', 'training', 'erp', 'casestudy']  # returning static pages; home and contact us

    def location(self, item):
        return reverse(item)  # returning the static pages URL; home and contact us
