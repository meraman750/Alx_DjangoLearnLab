from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Author, Book, Librarian, Library, UserProfile
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "date_of_birth")

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Information", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )

    # Fields shown when creating a user
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "date_of_birth", "profile_photo", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email", "username")
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Librarian)
admin.site.register(Library)
admin.site.register(UserProfile)