# Generated by Django 4.2.5 on 2023-11-06 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderedfood_order_delete_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedfood',
            name='amount',
        ),
    ]
