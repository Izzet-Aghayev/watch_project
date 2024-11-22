from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active:
            login(request, user=user)
            messages.success(request, f'Xoş gəldiniz, {user.username}')
            return redirect('all_watch')
        else:
            messages.info(request, 'İstifadəçi adı və ya şifrə yanlışdır.')
            return redirect('login')
    
    else:
        context = {
            'form': AuthenticationForm()
        }
        return render(request, 'accounts/login.html', context)


def sign_out(request):
    logout(request)
    messages.success(request, 'Çıxış edildi.')
    return redirect('all_watch')