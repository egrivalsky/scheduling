from django.contrib import admin

from . import models

# admin.site.register(models.Employee)
admin.site.register(models.Shift)

# class ShopAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(models.Shop, ShopAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Employee, EmployeeAdmin)