# Generated by Django 2.2.4 on 2019-09-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0025_auto_20190912_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtors',
            name='clientid',
            field=models.CharField(max_length=20),
        ),
    ]
