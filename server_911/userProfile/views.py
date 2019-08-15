from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .models import userProfile, Device
from .forms import device_form

# Create your views here.

#@login_required
def view_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            profile = userProfile.objects.get(username=request.user)
            device_imei = Device.objects.filter(user=profile)
            return render(request, 'userProfile/index.html', context={'devices':device_imei})
        except:
            return render(request, 'userProfile/index.html')
    

class Device_parametrs(View):
    def get(self, request, imei):
        profile = userProfile.objects.get(username=request.user)
        device_imei = Device.objects.get(user=profile, imei__iexact=imei)
        bound_form = device_form(instance=device_imei)

        # Map data
        gps_lat_start = str(float(device_imei.GPS_latitude) - 0.006)
        gps_lat_end = str(float(device_imei.GPS_latitude) + 0.006)
        gps_long_start = str(float(device_imei.GPS_longitude) - 0.006)
        gps_long_end = str(float(device_imei.GPS_longitude) + 0.006)
        url_gps = 'https://www.openstreetmap.org/export/embed.html?bbox=' + gps_long_start + '%2C' + gps_lat_start + '%2C' + gps_long_end +'%2C' + gps_lat_end + '&layer=mapnik&marker=' + device_imei.GPS_latitude + '%2C' + device_imei.GPS_longitude   
        #
        
        return render(request, 'userProfile/device_detail.html', context={'form':bound_form, 'device':device_imei, 'url_gps':url_gps})

    def post(self, request, imei):
        profile = userProfile.objects.get(username=request.user)
        device_imei = Device.objects.get(user=profile, imei__iexact=imei)
        bound_form = device_form(request.POST, instance=device_imei)

        if bound_form.is_valid():
            new_profile = bound_form.save()
            return redirect(new_profile)



# def device_detail(request, imei):
#     profile = userProfile.objects.get(username=request.user)
#     device_imei = Device.objects.get(user=profile, imei__iexact=imei)
#     return render(request, 'userProfile/device_detail.html', context={'device':device_imei})


