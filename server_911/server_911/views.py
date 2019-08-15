from django.shortcuts import render, redirect

def main_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('device_profile')

