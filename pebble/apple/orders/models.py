from django.db import models
from django.contrib.auth.models import User
from customer.models import foodItem



class Order(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    total = models.FloatField()

    
class OrderedFood(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)     
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fooditem = models.ForeignKey(foodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,null = True)
    price = models.FloatField()
    amount = models.FloatField(default=0)

    def __str__(self):
        return self.fooditem.food_name
