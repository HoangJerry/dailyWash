# -*- encoding: utf8 -*-
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from import_export import resources,fields
from import_export.admin import ExportActionModelAdmin
from unify_django.admin import UnifyBaseUserAdmin, BaseModelAdmin

from models import *


class UserAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminForm, self).__init__(*args, **kwargs)
        self.fields['city'].queryset = Address.objects.filter(parent__isnull=True)
        self.fields['district'].queryset = Address.objects.filter(parent__isnull=False)

class UserResource(resources.ModelResource):
    class Meta:
        Model = User
        # exclude = []
        fields = ('id', 'first_name', 'last_name', 'email', 'gender','city')
        export_order = fields

class UserAdmin(ExportActionModelAdmin,UnifyBaseUserAdmin):
    form = UserAdminForm
    resource_class = UserResource
    
    # readonly_fields =('password',)
    fieldsets = (
        (None, {'fields': ('status', 'email','password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name','city','district', 'avatar', 'fb_uid', 'gender',
                     'dob', 'about', 'relationship_status',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login','date_joined')}),
    )
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','name', '_link','active')
    fieldsets = (
        (None, {
            'fields': ('parent', 'name','active')
        }),
    )

    def _link(self, obj):
        link = str(obj.get_absolute_url()).title()[1:]
        return link.replace("/", ", ")
    _link.short_description = 'Full Category'
    
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Address,AddressAdmin)


