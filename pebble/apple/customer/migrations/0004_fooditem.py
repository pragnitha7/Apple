# Generated by Django 4.2.5 on 2023-11-05 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='foodimages')),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryname', to='customer.category')),
                ('restuarant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurantname', to='customer.restaurant')),
            ],
        ),
    ]