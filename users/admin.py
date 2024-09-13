from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']
    inlines = [UserProfileInline]
    search_fields = ['email__startswith']
    readonly_fields = ['date_joined',
                       'last_login',
                       'groups',
                       'is_active',
                       'user_permissions']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)