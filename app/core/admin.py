"""Django admin customization."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    """Define The admin pages for users."""

    ordering = ("id",)
    list_display = (
        "email",
        "name",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (("last login"), {"fields": ("last_login",)}),
    )
    readonly_fields = ("last_login",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "email", "password1", "password2"),
            },
        ),
        (
            "Permissions and sex ",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe)
