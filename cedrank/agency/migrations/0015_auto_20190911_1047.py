# Generated by Django 2.2.4 on 2019-09-11 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0014_auto_20190905_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditors',
            name='individual_id',
        ),
        migrations.AddField(
            model_name='creditors',
            name='clientid',
            field=models.CharField(default=123, max_length=20),
        ),
        migrations.AddField(
            model_name='debtors',
            name='clientid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agency.Creditors'),
        ),
    ]
