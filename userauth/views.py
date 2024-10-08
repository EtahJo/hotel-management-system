from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from userauth.models import User, Profile
from userauth.forms import UserRgisterForm

# Create your views here.

def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("hotel:index")
    form = UserRgisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        full_name= form.cleaned_data.get("full_name")
        phone= form.cleaned_data.get("phone")
        email= form.cleaned_data.get("email")
        password= form.cleaned_data.get("password1")
    
        user = authenticate(email=email, password=password)
        login(request,user)
        messages.success(request, f"Hey {full_name} your account has been created successfully")

        profile = Profile.objects.get(user=request.user)
        profile.full_name= full_name
        profile.phone= phone
        profile.save()
        return  redirect("hotel:index")
    context={
    "form":form
    }
    return  render (request, 'userauth/sign-up.html',context)

def LoginViewTemp(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("hotel:index")
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_query = User.objects.get(email=email)
            user_auth= authenticate(request, email=email, password=password)
            if user_query is not None:
                login(request,user_auth)
                messages.success(request,"You logged in")
                next_url = request.GET.get("next","hotel:index")
                return redirect(next_url)
            else:
                messages.error(request, "Username or password does not exist")
                return redirect("userauth:sign-in")
        except:
            messages.error(request, "User does not exist")
            return redirect("userauth:sign-in")

    # context={
    # "form":form
    # }
    return  render (request, 'userauth/sign-in.html')


def LogoutView(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect("userauth:sign-in")