from django.contrib import admin
from django.contrib.admin import site, action

from net.models import Organization, Contact, Product

# Register your models here.
site.register(Contact)
site.register(Product)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization_type', 'supplier',)
    list_display_links = ('name', 'supplier',)
    list_filter = ('contacts__city',)
    actions = ('delete_debt',)

    #admin_action для удаления задолженности
    @action(description='delete_debt')
    def delete_debt(self, request, queryset):
        queryset.update(debt=None)