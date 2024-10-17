from django.contrib import admin

from companies.models import Company
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Модель "Организация" для административной панели Django."""
    list_display = ('id', 'title', 'description',)