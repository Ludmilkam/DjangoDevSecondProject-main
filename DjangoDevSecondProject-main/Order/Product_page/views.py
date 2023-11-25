from django.shortcuts import render

# Create your views here.
def product_func(request):
    return render(request, 'Product_page/product_page.html')