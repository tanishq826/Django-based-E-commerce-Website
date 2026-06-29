from django.shortcuts import render,HttpResponse,get_object_or_404,redirect

from datetime import datetime
from home.models import *
from django.contrib import messages


# Create your views here.
def index(request):
    context={
        "variable1" : "Tanishq is great",
        "variable2" : "Arjun is also great"
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def category(request):
    return(request,'category.html')

def products(request):
    prods=Products.objects.all()
    print(prods)
    return render(request,'products.html',{"products":prods})
    #return HttpResponse("this is products page")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your Message has been Sent!")
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")

def Cart(request):
    return render(request,"cart.html")

# def add_to_cart(request,product_id):
#     products = get_object_or_404(Products, id=product_id)
#     Cart, created = Cart.objects.get_or_create(products=products)
#     if not created:
#         Cart.quantity += 1
#     Cart.save()
#     return redirect('cart.html')
# #    return HttpResponse("this is cart page")

# def remove_from_cart(request, item_id):
#     Cart = get_object_or_404(Cart, id=item_id)
#     Cart.delete()
#     return redirect('cart.html')

# def view_cart(request):
#     cart_item = Cart.objects.select_related('products').all()
#     total = sum(item.products.price * item.quantity for item in cart_item)
#     return render(request, 'cart.html', {'cart_item': cart_item, 'total': total})

