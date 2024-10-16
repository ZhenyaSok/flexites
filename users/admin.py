from django.contrib import admin

from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Модель "Пользователь" для административной панели Django."""

    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'role', 'is_active',)
    search_fields = ('id', 'email')
    list_filter = ('is_active',)
