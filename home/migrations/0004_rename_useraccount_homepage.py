# Generated by Django 5.1.4 on 2025-02-10 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_useraccount_delete_homepage'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAccount',
            new_name='HomePage',
        ),
    ]
