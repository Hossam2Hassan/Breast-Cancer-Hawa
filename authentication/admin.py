from django.contrib import admin

# Register your models here.
from .models import User


# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'auth_provider', 'created_at','first_name']
# admin.site.register(User, UserAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'auth_provider', 'created_at','first_name','is_staff',"is_verified"]
    ordaring=('email',)
    search_fields=('first_name','email')