from tabnanny import verbose
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def clean(self):
        self.category_name=self.category_name.capitalize()

    def __str__(self) -> str:
        return self.category_name

class foodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='fooditems')
    food_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='foodimages')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.food_name

    def clean(self):
        self.food_name=self.food_name.capitalize()
