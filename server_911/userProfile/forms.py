from django import forms
from .models import Device

class device_form(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['enable_SearchMode', 'launch_period', 'time_GPS_search', 'time_GSM_registration', 'enable_acс']

        widgets = {
            'enable_SearchMode': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'launch_period': forms.NumberInput(attrs={'class': 'form-control'}),
            'time_GPS_search': forms.NumberInput(attrs={'class': 'form-control'}),
            'time_GSM_registration': forms.NumberInput(attrs={'class': 'form-control'}),
            'enable_acс': forms.CheckboxInput(attrs={'class': 'form-control'})
        }
    #enable_SearchMode = forms.BooleanField()
    # launch_period = forms.IntegerField() #в минутах
    # time_GPS_search = forms.IntegerField()
    # time_GSM_registration = forms.IntegerField()
    # enable_acс = forms.BooleanField()

    

