# -*- encoding: utf8 -*-
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from import_export import resources,fields
from import_export.admin import ExportActionModelAdmin
from unify_django.admin import UnifyBaseUserAdmin, BaseModelAdmin

from models import *


class UserAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminForm, self).__init__(*args, **kwargs)
        self.fields['city'].queryset = Address.objects.filter(parent__isnull=True)
        self.fields['district'].queryset = Address.objects.filter(parent__isnull=False)
        self.fields['password'] = ReadOnlyPasswordHashField(label= ("Password"),
        help_text= ("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

class UserResource(resources.ModelResource):
    class Meta:
        Model = User
        # exclude = []
        fields = ('id', 'first_name', 'last_name', 'email', 'gender','city','phone')
        export_order = fields

class UserAdmin(ExportActionModelAdmin,UnifyBaseUserAdmin):
    form = UserAdminForm
    resource_class = UserResource
    
    # readonly_fields =('password',)
    fieldsets = (
        (None, {'fields': ('status', 'email','password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name','phone','city','district', 'avatar', 'fb_uid', 'gender',
                     'dob', 'about', 'relationship_status',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff','is_wash_man','is_delivery_man', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login','date_joined')}),
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','status','title','category','price')
    list_editable = ('status',)

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

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','active')

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.exclude(is_wash_man=True,is_delivery_man=True)
        self.fields['take_man'].queryset = User.objects.filter(is_delivery_man=True)
        self.fields['wash_man'].queryset = User.objects.filter(is_wash_man=True)
        self.fields['return_man'].queryset = User.objects.filter(is_delivery_man=True)

class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_display = ('id','product','status','user','take_man','wash_man','return_man','total')
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 25

class SoftAdditionAdmin(admin.ModelAdmin):
    list_display = ('name','price')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(SoftAddition,SoftAdditionAdmin)


