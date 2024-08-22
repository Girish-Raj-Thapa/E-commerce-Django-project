from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from . models import Product, Customer, Cart, Payment, OrderPlaced, WishList
from . forms import CustomerRegisterationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
import razorpay
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@login_required 
def home(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    return render(request, 'home.html', locals())


@login_required 
def about(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    return render(request, 'about.html', locals())


@login_required  
def contact(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    return render(request, 'contact.html', locals())


@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request, value):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))

        product = Product.objects.filter(category=value)
        title = Product.objects.filter(category=value).values('title')
        return render(request, 'category.html', locals())
    

@method_decorator(login_required, name='dispatch') 
class CategoryTitleView(View):
    def get(self, request, value):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))

        product = Product.objects.filter(title=value)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'category.html', locals())    


@method_decorator(login_required, name='dispatch')
class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))

        product = get_object_or_404(Product, pk=pk)
        wishlist = WishList.objects.filter(product=product, user=request.user) if request.user.is_authenticated else []
        return render(request, 'productdetail.html', {'product': product, 'totalitem': totalitem, 'wishlist': wishlist, 'wishitem':wishitem})

    
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegisterationForm()
        return render(request, 'customerregistration.html', locals())
    
    def post(self, request):
        form = CustomerRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations!! User Registered Successfully")
        else:
            messages.warning(request, "Invalid Input Data")

        return render(request, 'customerregistration.html', locals())
    

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))

        form = CustomerProfileForm()
        return render(request, 'profile.html', locals())
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            customer_info = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            customer_info.save()
            messages.success(request, "Congratulations!! Profile Saved Successfully")
        else:
            messages.warning(request, "Invalid Input Data")

        return render(request, 'profile.html', locals())
    

@login_required 
def address(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    address = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', locals())


@method_decorator(login_required, name='dispatch')
class UpdateAddress(View):
    def get(self, request, pk):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))
             
        address = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=address)
        return render(request, 'updateaddress.html', locals())


    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            address = Customer.objects.get(pk=pk)
            address.name = form.cleaned_data['name']
            address.locality = form.cleaned_data['locality']
            address.city = form.cleaned_data['city']
            address.mobile = form.cleaned_data['mobile']
            address.state = form.cleaned_data['state']
            address.zipcode = form.cleaned_data['zipcode']
            
            address.save()
            messages.success(request, "Congratulations!! Profile Updated Successfully")
        else:
            messages.warning(request, "Invalid Input Data")

        return redirect('address')
    

@login_required 
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


@login_required 
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(Product, id=product_id)
    
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        # The item is already in the cart, so you can update it (e.g., increment quantity)
        cart_item.quantity += 1
        cart_item.save()
    else:
        # The item was newly added
        cart_item.save()

    # Your response logic here
    return redirect('/cart')


@login_required 
def show_cart(request):
    user = request.user 
    cart = Cart.objects.filter(user=user)
    amount = 0
    for each in cart:
        value = each.quantity * each.product.discounted_price 
        amount += value 
    totalamount = 50 + amount 

    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    return render(request, 'addtocart.html', locals())


@login_required 
def plus_cart(request):
    if request.method == "GET":
        product_id = request.GET['product_id']
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity += 1 
        c.save()

        cart = Cart.objects.filter(user=request.user)
        amount = 0
        for each in cart:
            value = each.quantity * each.product.discounted_price 
            amount += value 
        totalamount = 50 + amount 

        print(product_id)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)


@login_required 
def minus_cart(request):
    if request.method == "GET":
        product_id = request.GET['product_id']
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.quantity -= 1 
        c.save()

        cart = Cart.objects.filter(user=request.user)
        amount = 0
        for each in cart:
            value = each.quantity * each.product.discounted_price 
            amount += value 
        totalamount = 50 + amount 

        print(product_id)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)
    

@login_required 
def remove_cart(request):
    if request.method == "GET":
        product_id = request.GET['product_id']
        c = Cart.objects.get(Q(product=product_id) & Q(user=request.user))
        c.delete()

        cart = Cart.objects.filter(user=request.user)
        amount = 0
        for each in cart:
            value = each.quantity * each.product.discounted_price 
            amount += value 
        totalamount = 50 + amount 

        print(product_id)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)
    

@method_decorator(login_required, name='dispatch')
class Checkout(View):
    def get(self, request):
        user = request.user 
        address = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(WishList.objects.filter(user=request.user))

        famount = 0
        for item in cart_items:
            value = item.quantity * item.product.discounted_price
            famount += value
        totalamount = famount + 40
        razoramount = int(totalamount * 100)
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = {
            'amount': razoramount,
            'currency': 'INR',
            'receipt': 'order_rcptid_11',
        }
        payment_response = client.order.create(data=data) 
        print(payment_response)

        order_id = payment_response['id']
        order_status = payment_response['status']

        if order_status == 'created':
        # Assuming `Payment` is a Django model and `user` and `totalamount` are defined
            payment = Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
            )
            payment.save()

        return render(request, 'checkout.html', locals())
    

@login_required 
def payment_done(request):
    # Extract parameters from the request
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')

    # Get the current user
    user = request.user

    # Get the customer object
    customer = Customer.objects.get(id=cust_id)

    # Update payment status and payment id
    payment = Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()

    # Save order details
    cart_items = Cart.objects.filter(user=user)
    for cart_item in cart_items:
        OrderPlaced.objects.create(
            user=user,
            customer=customer,
            product=cart_item.product,
            quantity=cart_item.quantity,
            payment=payment
        )
        # Delete the cart item after placing the order
        cart_item.delete()

    # Redirect to the orders page
    return redirect("orders")


@login_required 
def orders(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'orders.html', locals())


@login_required
def show_wishlist(request):
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))
    user = request.user 
    product = WishList.objects.filter(user=user)
    return render(request, 'wishlist.html', locals())


@login_required 
def plus_wishlist(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'User not authenticated'}, status=403)
        
        product_id = request.GET.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        WishList.objects.get_or_create(user=request.user, product=product)
        
        return JsonResponse({'message': 'WishList added successfully'})


@login_required 
def minus_wishlist(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'User not authenticated'}, status=403)
        
        product_id = request.GET.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        WishList.objects.filter(user=request.user, product=product).delete()
        
        return JsonResponse({'message': 'WishList removed successfully'})
    

@login_required 
def search(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(WishList.objects.filter(user=request.user))

    query = request.GET['search']
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, 'search.html', locals())