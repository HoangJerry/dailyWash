from django.db import models
from unify_django.models import *
from categories.base import CategoryBase

class User(UnifyBaseUser):
	pass

class Address(CategoryBase):

	def get_absolute_url(self):
        """Return a path"""
        from django.core.urlresolvers import NoReverseMatch

        try:
            prefix = reverse('categories_tree_list')
        except NoReverseMatch:
            prefix = '/'
        ancestors = list(self.get_ancestors()) + [self, ]
        return prefix + '/'.join([force_text(i.name) for i in ancestors]) + '/'
	