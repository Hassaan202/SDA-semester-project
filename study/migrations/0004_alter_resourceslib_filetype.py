# Generated by Django 5.1.3 on 2024-12-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_resourceslib'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourceslib',
            name='fileType',
            field=models.CharField(choices=[('books', 'books'), ('pastpapers', 'pastpapers'), ('playlists', 'playlists')], max_length=50),
        ),
    ]
