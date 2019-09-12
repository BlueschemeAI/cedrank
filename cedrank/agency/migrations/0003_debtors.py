# Generated by Django 2.2.4 on 2019-08-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agency', '0002_delete_debtors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debtors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('individual_id', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
                ('debt_amount', models.IntegerField()),
                ('case_details', models.TextField()),
                ('document', models.FileField(upload_to='')),
            ],
        ),
    ]