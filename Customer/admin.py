from django.contrib import admin
from .models import (Customer, ToDo)
# Register your models here.
admin.site.register(Customer)
admin.site.register(ToDo)
