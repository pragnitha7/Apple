# Generated by Django 4.2.5 on 2023-11-06 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_orderedfood_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedfood',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
