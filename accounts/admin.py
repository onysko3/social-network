from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_active', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar', 'slug',
                  'status', 'bio', 'birthdate', 'sex', 'country', 'city', 'education')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
