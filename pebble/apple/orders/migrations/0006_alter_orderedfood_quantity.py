# Generated by Django 4.2.5 on 2023-11-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedfood',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
