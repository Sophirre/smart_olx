from django.contrib import admin
from .models import *

admin.site.register(Account)
admin.site.register(Advertisement)
admin.site.register(AdvertisementCategory)
admin.site.register(AdvertisementSubCategory)

# Register your models here.
