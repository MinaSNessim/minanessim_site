from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from ckeditor_uploader.fields import RichTextUploadingField


class SubscribeToNewsletter(models.Model):
    email = models.EmailField(unique=True, verbose_name='')
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Portfolio(models.Model):
    choices = (
        ('filter-python', 'Python'),
        ('filter-dashboard', 'Dashboard'),
        ('filter-statistic', 'Statistics'),
        ('filter-machine_learning', "Machine Learning"),
        ('filter-scrapping', 'Scrapping'),
        ('filter-excel', 'Excel'),
        ('filter-supply_chain', 'Supply Chain'),
        ('filter-sql', 'SQL'),
        ('filter-tableau_BI', 'Tableau/Power BI'),
    )

    title = models.CharField(max_length=100)
    category = MultiSelectField(choices=choices, max_choices=5, max_length=100, blank=True)
    insight = models.CharField(max_length=259, blank=True)
    body = RichTextUploadingField(blank=True)
    photo = models.ImageField(upload_to='portfolio_photos/', blank=True, null=True)

    def __str__(self):
        return self.title


class BlogPosts(models.Model):
    choices = (
        ('filter-barabic', 'Arabic'),
        ('filter-benglish', 'English'),
        ('filter-bdata', 'Data'),
        ('filter-bstatistic', 'Statistics'),
        ('filter-bmachine_learning', "Machine Learning"),
        ('filter-bpython', 'Python'),
        ('filter-bexcel', 'Excel'),
    )

    title = models.CharField(max_length=100)
    category = MultiSelectField(choices=choices, max_choices=5, max_length=100, blank=True)
    insight = models.CharField(max_length=259, blank=True)
    body = RichTextUploadingField(blank=True)
    photo = models.ImageField(upload_to='portfolio_photos/', blank=True, null=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title
