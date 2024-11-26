from .models import Profile
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.forms import ProfileForm


# Hesaba daxil olamq üçünü funksiya.
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        seller = authenticate(request, username=username, password=password)
        
        if seller is not None and seller.is_active:
            login(request, user=seller)
            messages.success(request, f'Xoş gəldiniz, {seller.username}')
            return redirect('all_watch')
        else:
            messages.info(request, 'İstifadəçi adı və ya şifrə yanlışdır.')
            return redirect('login')
    
    else:
        context = {
            'form': AuthenticationForm()
        }
        return render(request, 'accounts/login.html', context)


# Çıxış üçün funksiay.
def sign_out(request):
    logout(request)
    messages.success(request, 'Çıxış edildi.')
    return redirect('all_watch')


# Qeydiyyat üçün funksiya.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Qeydiyyatdan keçdiniz')
            return redirect('all_watch')
        else:
            messages.error(request, form.errors)
            return redirect('register')
    else:
        form = UserCreationForm()
        context = {
            'creation_form': form
        }
        return render(request, 'accounts/register.html', context)
    

# Profili update etmək üçün funksiya.
def profile(request):
    seller_profile = Profile.objects.filter(seller=request.user)    # Userə uyğun profili alır.
    profile = get_object_or_404(seller_profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)      # instance formun məlumatlarını foruma dolduru.
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil məlumatlar yeniləndi.')
            return redirect('all_watch')
        else:
            messages.error(request, form.errors)
            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)
        context = {
            'profile_form': form
        }
        return render(request, 'accounts/profile.html', context)