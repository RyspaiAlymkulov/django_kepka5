from django.contrib import admin
from . import models


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email"
    )


admin.site.register(models.CustomUser, CustomUserAdmin)