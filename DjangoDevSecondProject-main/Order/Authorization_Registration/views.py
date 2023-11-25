from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError

# Create your views here.
def auth_func(request):
    context = {}
    
    if request.user.is_authenticated:
        context['error'] = "Ви вже зареєстровані!"
    
    if request.method == 'POST':
        username =  request.POST.get('username')
        password = request.POST.get('password')   
        
        context['username'] = username
        context['password'] = password
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                context['error'] = "Логін або пароль невірні"
        else:
            context['error'] = "Поля не заповнені"
            
    return render(request, 'Authorization_Registration/authorization.html', context)

def reg_func(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        context['username'] = username
        context['password'] = password
        context['email'] = email
        context['phone'] = phone
        
        if username and password and email and phone:
            if len(password) >= 8:
                try: 
                    User.objects.create_user(
                        username=username, 
                        password=password,
                        email=email
                    )
                    return redirect('auth_page')
                except IntegrityError:
                    context['error'] = "Такий користувач існує"
            else:
                context['error'] = 'Пароль повинен бути більше або дорівнювати 8 символів!' 
        else:
            context['error'] = "Поля не заповнені"
        
    return render(request, 'Authorization_Registration/registration.html', context)
