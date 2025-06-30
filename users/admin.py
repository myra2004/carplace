from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('id', 'username', 'email', 'first_name', 'last_name')

    fieldsets = (
        ('User', {'fields': ('username', 'password', 'email')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'avatar', 'profession', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )