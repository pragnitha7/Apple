from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to='profile_pics',default='default.jpg')
    address=models.TextField()
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=13)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def clean(self):
        self.category_name=self.category_name.capitalize()

    def __str__(self) -> str:
        return self.category_name
    
class restaurant(models.Model):
    restaurant_name=models.CharField(max_length=200)

    def __str__(self) -> str:
       return self.restaurant_name


class foodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='categoryname')
    restaurant_name=models.ForeignKey(restaurant,on_delete=models.CASCADE,related_name='restaurantname')
    food_name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='foodimages')
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.food_name

    
class Cart(models.Model):
    restaurant_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.ForeignKey(foodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1,null=True)
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.food_name
