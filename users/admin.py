from django.contrib import admin
from . import models


@admin.register(models.User)  # == admin.site.register(models.User, CustomUserAdmin)
class CustomUserAdmin(admin.ModelAdmin):
    """ Custom  User Admin """

    # How to display User Info in admin panel
    list_display = ('username', "email", 'gender', 'language', 'currency', 'superhost')
    # Create Filter
    list_filter = ("language", "currency", "superhost")
