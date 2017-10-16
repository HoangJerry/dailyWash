from django.contrib import admin


from import_export import resources,fields
from import_export.admin import ExportActionModelAdmin
from unify_django.admin import UnifyBaseUserAdmin, BaseModelAdmin

from models import *


class UserResource(resources.ModelResource):
	class Meta:
		Model = User
		# exclude = []
		fields = ('id', 'first_name', 'last_name', 'email', 'gender')
    	export_order = fields

class UserAdmin(ExportActionModelAdmin,UnifyBaseUserAdmin):
    resource_class = UserResource
    



# Register your models here.
admin.site.register(User, UserAdmin)

