# Generated by Django 4.2.5 on 2023-11-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=200)),
            ],
        ),
    ]