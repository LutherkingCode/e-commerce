from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Product)

admin.site.register(models.ProductCart)
admin.site.register(models.Cart)
admin.site.register(models.Payment)