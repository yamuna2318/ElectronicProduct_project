from django.contrib import admin
from .models import *

# Register your models here.
class Admincommondata(admin.ModelAdmin):
    list_display = ['name','desc','header_img','processor','RAM']

class Adminmobiledata(admin.ModelAdmin):
    list_display = ['name','desc','header_img','processor','RAM','screensize','color']

class Adminlaptopdata(admin.ModelAdmin):
    list_display = ['name','desc','header_img','processor','RAM','HD_capacity']

admin.site.register(commondata,Admincommondata)
admin.site.register(mobilesdata,Adminmobiledata)
admin.site.register(laptopsdata,Adminlaptopdata)