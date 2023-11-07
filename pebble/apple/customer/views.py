from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import userregisterform
from django.contrib.auth.models import User
from django.contrib import messages
from orders.models import *
from customer.models import *
from customer.forms import userprofileform
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseRedirect
# # Create your views here.

@login_required(login_url='login')
def updateprofile(request,id):
    if request.method == 'POST':
        form1=userprofileform(request.POST,request.FILES,instance=request.user.user_profile)
        if form1.is_valid():
            form1.save()
            messages.success(request,f'Your account has been Updated!')
            dynamic_url = f'/profile/{request.user.id}'
            return redirect(dynamic_url)
    else:
        form1=userprofileform(instance=request.user.user_profile)
        context={
            'form1':form1
        }
        return render(request,'customer/update_profile.html',context)

    

@login_required
def cart(request):
    carted_food_items = Cart.objects.filter(user=request.user)
    total = 0
    for item in carted_food_items:
            food_item = foodItem.objects.get(pk=item.food_name.id)
            print(food_item.price)
            quantity = 1
            total += (food_item.price * quantity)
    context = {'total': total , 'carted_food_items' : carted_food_items}
    return render (request, 'customer/cart.html',context)


    
def home(request):
    categories = Category.objects.all()
    restaurants = restaurant.objects.all()
    return render(request, 'customer/home.html', {'categories': categories, 'restaurants': restaurants})

def restaurant_detail(request, restaurant_id):
    restaurant_obj=restaurant.objects.get(pk=restaurant_id)
    food_items = foodItem.objects.filter(restaurant_name=restaurant_obj)
    return render(request, 'customer/restaurant_detail.html', {'restaurant_obj': restaurant_obj, 'food_items': food_items})

def category_detail(request, category_id):
    category_obj=Category.objects.get(pk=category_id)
    food_items = foodItem.objects.filter(category=category_obj)
    return render(request, 'customer/category_detail.html', {'category_obj': category_obj, 'food_items': food_items})

def contact(request):
   return render(request,'customer/contactus.html')

def register(request):
    if request.method=='POST':
        form=userregisterform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('login')
        else:
            messages.error(request,"Error SigningUP")
            print(form.error_messages)
            return redirect('register')
        
    else:
        form=userregisterform()
        return render(request,'customer/register.html',{'form': form})


    
@login_required(login_url='login')

def profile(request,id):
    user1=User.objects.get(pk=id)
    return render(request,'customer/profile.html',{'user':user1})



from django.shortcuts import redirect




@login_required
def add_to_cart(request,id):

    if request.method=='POST':
        print(id, type(id))
        food= foodItem.objects.get(pk=id)
        print(food)
        food_name = food.food_name
        price = food.price
        restaurant_name=food.restaurant_name
        quantity = request.POST.get('quantity')
        food = foodItem.objects.get(restaurant_name =restaurant_name,food_name = food_name ,price = price)
        print("done")
        # Create a Shortlist entry with the specific attributes
        user =User.objects.get(username = request.user)
        print(user)
        created=Cart(user = user, restaurant_name=food.restaurant_name,price = food.price ,food_name = food ,quantity = quantity)

        if created:
            print("1")
            created.save()
            messages.success(request, 'Items added to Cart')
        else:
            messages.info(request, 'Already in Cart')
            
        return redirect('/cart/')
    return redirect('/cart/')
    

@login_required   
def deleteitem(request, item_id):
    if request.method == 'POST':
        cart_item = Cart.objects.get(pk = item_id)
        name=cart_item.food_name
        cart_item.delete()
        messages.success(request, f'you have deleted the {name}')
    url = f'/cart/'
    return redirect(url)

@login_required 
def pastorders(request) :
    order = OrderedFood.objects.filter(user=request.user)
    context = {
        'order' : order
    }
    return render(request,'customer/past_orders.html',context)



@login_required   
def ordernow(request, item_id):

    if request.method=='POST':
        print(id, type(id))
        food= Cart.objects.get(pk=item_id)
        print(food)
        food_name = food.food_name
        price = food.price
        quantity =food.quantity
        food = foodItem.objects.get(food_name = food_name ,price = price)
        print("done")
        # Create a Shortlist entry with the specific attributes
        user =User.objects.get(username = request.user)
        print(user)
        created=OrderedFood(user = user, price = food.price ,fooditem = food ,quantity = 1)

        if created:
            print("1")
            created.save()
            messages.success(request, 'Items added to Cart')
        else:
            messages.info(request, 'Already in Cart')
            
        return redirect('/cart/')
    return redirect('/cart/')

