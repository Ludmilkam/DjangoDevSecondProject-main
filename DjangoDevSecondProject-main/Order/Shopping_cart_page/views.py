from django.shortcuts import render

# Create your views here.
def shop_cart_func(request):
    return render(request, 'Shopping_cart_page/shopping_cart_page.html')