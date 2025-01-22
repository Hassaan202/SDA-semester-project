# Generated by Django 5.1.3 on 2024-12-03 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_resourceupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourcesLib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=100)),
                ('fileType', models.CharField(max_length=50)),
                ('fileLink', models.URLField(max_length=500)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.subject')),
            ],
        ),
    ]
