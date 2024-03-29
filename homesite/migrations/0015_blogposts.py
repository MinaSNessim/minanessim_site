# Generated by Django 4.2.8 on 2023-12-30 13:30

import ckeditor_uploader.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0014_alter_portfolio_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('filter-barabic', 'Arabic'), ('filter-benglish', 'English'), ('filter-bdata', 'Data'), ('filter-bstatistic', 'Statistics'), ('filter-bmachine_learning', 'Machine Learning'), ('filter-bpython', 'Python'), ('filter-bexcel', 'Excel')], max_length=100)),
                ('insight', models.CharField(blank=True, max_length=259)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='portfolio_photos/')),
            ],
        ),
    ]
