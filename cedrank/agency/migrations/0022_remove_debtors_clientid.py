# Generated by Django 2.2.4 on 2019-09-12 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0021_auto_20190912_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debtors',
            name='clientid',
        ),
    ]
