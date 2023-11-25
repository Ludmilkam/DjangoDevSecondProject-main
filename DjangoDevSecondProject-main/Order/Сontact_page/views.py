from django.shortcuts import render

# Create your views here.
def contact_func(request):
    return render(request, 'Сontact_page/contact_page.html')