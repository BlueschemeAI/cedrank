# Generated by Django 2.2.4 on 2019-09-12 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0020_auto_20190912_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtors',
            name='clientid',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='agency.Creditors'),
        ),
    ]
