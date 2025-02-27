from django.contrib import admin
from Hospitalapp.models import *

# Register your models here.

admin.site.register(Patient)

admin.site.register(Doctor)
admin.site.register(staff)
admin.site.register(ward)



