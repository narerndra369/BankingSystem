from django.contrib import admin

# Register your models here.
from .models import TransactionDetails, UserDetails

admin.site.register(UserDetails)
admin.site.register(TransactionDetails)