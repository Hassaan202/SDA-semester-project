# Generated by Django 5.1.3 on 2024-12-02 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_contactmessage_created_at_alter_contactmessage_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='created_at',
        ),
    ]
