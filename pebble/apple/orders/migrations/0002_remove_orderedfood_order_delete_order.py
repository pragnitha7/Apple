# Generated by Django 4.2.5 on 2023-11-06 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedfood',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
