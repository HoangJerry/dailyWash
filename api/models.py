# -*- encoding: utf8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from unify_django.models import *


from categories.base import CategoryBase
from django.utils.encoding import force_text

class User(UnifyBaseUser):
    city = models.ForeignKey("Address",related_name='city', null=True, blank=True)
    district = models.ForeignKey("Address",related_name='district', null=True, blank=True)
    street = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    
class Address(CategoryBase):

    def get_absolute_url(self):
        """Return a path"""
        from django.core.urlresolvers import NoReverseMatch

        try:
            prefix = reverse('categories_tree_list')
        except NoReverseMatch:
            prefix = '/'
        ancestors = list(self.get_ancestors()) + [self, ]
        return prefix + '/'.join([force_text(i.name) for i in ancestors]).encode('utf-8').strip() + '/'
    