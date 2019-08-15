from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class userProfile(AbstractUser):
    phone_number = models.CharField(max_length=12)
    
    def __str__(self):
        return self.username

class Device(models.Model):
    user = models.ForeignKey('userProfile', on_delete=models.CASCADE)
    imei = models.CharField(max_length=15, unique=True)
    sid_1 = models.CharField(max_length=18, blank=True)
    sid_2 = models.CharField(max_length=18, blank=True)
    rn = models.CharField(max_length=12, blank=True)
    version = models.CharField(max_length=19, blank=True)
    enable_SearchMode = models.BooleanField(default=False)
    launch_period = models.IntegerField(blank=True, default=0) #в минутах
    time_GPS_search = models.IntegerField(default=15)
    time_GSM_registration = models.IntegerField(default=30)
    send_SMS_SearchMode = models.BooleanField(default=False)
    enable_acс = models.BooleanField(default=False)
    send_SMS_MoveAcc = models.BooleanField(default=False)
    send_data_Email = models.BooleanField(default=False)
    send_status_30days = models.BooleanField(default=False)
    date_device_registration = models.DateField(auto_now=False, auto_now_add=True)
    battery_level = models.FloatField(blank=True, null=True)
    date_to_end = models.IntegerField(blank=True, null=True)
    date_last_message = models.DateField(auto_now=True, auto_now_add=False, blank=True)
    date_next_message = models.DateField(auto_now=False, auto_now_add=False, null=True)
    
    temperature = models.CharField(max_length=4, blank=True)
    last_message_sim = models.CharField(max_length=1, blank=True)

    GPS_last_HDOP = models.CharField(max_length=4, blank=True)
    GPS_time_UTC = models.CharField(max_length=10, blank=True)
    GPS_status = models.CharField(max_length=1, blank=True)
    GPS_latitude = models.CharField(max_length=15, blank=True)
    GPS_n_s = models.CharField(max_length=1, blank=True)
    GPS_longitude = models.CharField(max_length=16, blank=True)
    GPS_e_w = models.CharField(max_length=1, blank=True)
    GPS_speed = models.CharField(max_length=8, blank=True)
    GPS_course = models.CharField(max_length=8, blank=True) 
    GPS_date = models.CharField(max_length=6, blank=True)

    GSM_latitude = models.CharField(max_length=15, blank=True)
    GSM_longitude = models.CharField(max_length=16, blank=True)

    motion = models.BooleanField(default=False)
    motion_T = models.IntegerField(blank=True, null=True)
    motion_TS = models.IntegerField(blank=True, null=True)

    balance_info = models.CharField(max_length=162, blank=True)

    log_data = models.TextField(blank=True, null=True)  
    data_F = models.CharField(max_length=2, blank=True)
    data_time_GPS = models.CharField(max_length=13, blank=True)
    data_time_GSM = models.CharField(max_length=13, blank=True)

    device_param = models.TextField(blank=True, null=True) 

    SMS_code = models.CharField(max_length=1, blank=True)  
    SMS_text = models.CharField(max_length=15, blank=True)   

    def get_update_url(self):
        return reverse('device_detail', kwargs={'imei': self.imei})

    def get_absolute_url(self):
        return reverse('device_detail', kwargs={'imei': self.imei})

    def __str__(self):
        return self.imei

class Message_from_FM(models.Model):                                                         
    version = models.CharField(max_length=19)
    type_con = models.CharField(max_length=1)
    imei = models.ForeignKey('Device', on_delete=models.CASCADE) 
    sid = models.CharField(max_length=18)
    p_roaming = models.CharField(max_length=1)
    ops = models.CharField(max_length=7)
    data = models.TextField(blank=True)
    cs = models.CharField(max_length=3)
    date_pub = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):                                                           
        return self.imei.imei

    class Meta:
        ordering = ['-date_pub']