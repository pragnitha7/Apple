# from ctypes import addressof
# from email.policy import default
# from multiprocessing import context
# from django.http import HttpResponse,JsonResponse
# from django.shortcuts import render,get_object_or_404,redirect
# from accounts.models import UserProfile
# from orders.models import Order
# from .models import Cart
# from menu.models import Category,foodItem
# from django.db.models import Prefetch,Q
# from .processor import get_cart_counter, get_cart_amount
# from django.contrib.auth.decorators import login_required
# from datetime import date,datetime
# from orders.forms import OrderForm


# def decrease_cart(request,food_id):
#     if request.user.is_authenticated:
#         if request.is_ajax():
#             #check if the food item exists
#             try:
#                 fooditem=foodItem.objects.get(id=food_id)
#                 #check if the food is in the cart
#                 try:
#                     checkcart=Cart.objects.get(user=request.user,fooditem=fooditem)
#                     if checkcart.quantity>1:
#                         #decrease the quantity
#                         checkcart.quantity-=1
#                         checkcart.save()
#                     else:
#                         checkcart.delete()
#                         checkcart.quantity=0
#                     return JsonResponse({'status':'Success','message':'Quantity decreases.','cart_counter':get_cart_counter(request),'qty':checkcart.quantity,'cart_amount':get_cart_amount(request)})
#                 except:
#                     return JsonResponse({'status':'Fail','message':'You do not have this item in your cart.'})
#             except:
#                 return JsonResponse({'status':'Fail','message':'This food does not exist.'})
#         else:
#             return JsonResponse({'status':'Fail','message':'Invalid request.'})
        

#     return JsonResponse({'status':'login_required','message':'Please log in first.'})


# def add_to_cart(request,food_id):
#     if request.user.is_authenticated:
#         if request.is_ajax():
#             #check if the food item exists
#             try:
#                 fooditem=foodItem.objects.get(id=food_id)
#                 #check if the food is in the cart
#                 try:
#                     checkcart=Cart.objects.get(user=request.user,fooditem=fooditem)
#                     #increment the quantity
#                     checkcart.quantity+=1
#                     checkcart.save()
#                     return JsonResponse({'status':'Success','message':'Quantity increases.','cart_counter':get_cart_counter(request),'qty':checkcart.quantity,'cart_amount':get_cart_amount(request)})
#                 except:
#                     #add the food
#                     checkcart=Cart.objects.create(user=request.user,fooditem=fooditem,quantity=1)
#                     return JsonResponse({'status':'Success','message':'Added the food into the cart.','cart_counter':get_cart_counter(request),'qty':checkcart.quantity,'cart_amount':get_cart_amount(request)})
#             except:
#                 return JsonResponse({'status':'Fail','message':'This food does not exist.'})
#         else:
#             return JsonResponse({'status':'Fail','message':'Invalid request.'})
        
    
#     return JsonResponse({'status':'login_required','message':'Please log in first.'})
    
# @login_required(login_url='login')
# def cart(request):
#     cart_items=Cart.objects.filter(user=request.user).order_by('created_at')
#     context={
#         'cart_items' :cart_items,
#     }
#     return render(request,'marketplace/cart.html',context)

# def del_cart(request,cart_id):
#     if request.user.is_authenticated:
#         if request.is_ajax():
#             try:
#                 #check if the cart item exists
#                 cart_item=Cart.objects.get(user=request.user,id=cart_id)
#                 if cart_item:
#                     cart_item.delete()
#                     return JsonResponse({'status':'Success','message':'Cart item has been deleted.','cart_counter':get_cart_counter(request),'cart_amount':get_cart_amount(request)})
#             except:
#                 return JsonResponse({'status':'Fail','message':'Cart item does not exist.'})

#         else:
#             return JsonResponse({'status':'Fail','message':'Invalid request.'})

                
# @login_required(login_url='login')
# def checkout(request):
#     cart_items=Cart.objects.filter(user=request.user).order_by('created_at')
#     cart_count=cart_items.count()
#     if cart_count<=0:
#         return redirect('marketplace')
#     user_profile=UserProfile.objects.get(user=request.user)
#     default_values = {
#         'first_name': request.user.first_name,
#         'last_name': request.user.last_name,
#         'phone': request.user.phone_number,
#         'email': request.user.email,
#         'address': user_profile.address,
#         'country': user_profile.country,
#         'state': user_profile.state,
#         'city': user_profile.city,
#         'pin_code': user_profile.pin_code,
#     }
#     form = OrderForm(initial=default_values)
#     context={
#         'form':form,
#         'cart_items':cart_items,
#     }
#     return render(request,'marketplace/checkout.html',context)
