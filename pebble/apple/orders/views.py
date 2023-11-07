# from multiprocessing import context
from django.shortcuts import render, redirect
from customer.models import foodItem
from customer.models import Cart
# from customer.views import get_cart_amount
# from .forms import OrderForm
# from .models import OrderedFood
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


