# Generated by Django 2.2.4 on 2019-09-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0013_auto_20190905_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditors',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='debtors',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]