from django.contrib import admin
from .models import SubscribeToNewsletter, Contact, Portfolio, BlogPosts


class SubscribeToNewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sent_at')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_photo')  # Update this to display the photo in the admin

    def display_photo(self, obj):
        return obj.photo.url if obj.photo else 'No photo'

    display_photo.short_description = 'Photo'  # Set the column name in the admin panel


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'subscribed_at', 'display_photo')  # Update this to display the photo in the admin

    def display_photo(self, obj):
        return obj.photo.url if obj.photo else 'No photo'

    display_photo.short_description = 'Photo'  # Set the column name in the admin panel


# Register your models here.
admin.site.register(SubscribeToNewsletter, SubscribeToNewsletterAdmin)
admin.site.register(Contact, ContactFormAdmin)
admin.site.register(Portfolio)
admin.site.register(BlogPosts, BlogAdmin)
