# Generated by Django 2.2.4 on 2019-09-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0007_auto_20190904_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtors',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to=''),
        ),
    ]
