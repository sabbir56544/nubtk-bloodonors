# Generated by Django 3.2.8 on 2021-10-31 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0010_donorregister_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donorregister',
            name='last_donate_date',
        ),
    ]
