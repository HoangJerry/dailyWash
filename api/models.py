# -*- encoding: utf8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from unify_django.models import *


from categories.base import CategoryBase
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from app import settings

class User(UnifyBaseUser):
    city = models.ForeignKey("Address",related_name='city', null=True, blank=True)
    district = models.ForeignKey("Address",related_name='district', null=True, blank=True)
    street = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_wash_man = models.BooleanField(default=False)
    is_delivery_man = models.BooleanField(default=False)

class Product(models.Model):
    STATUS_DISABLE = 0
    STATUS_ENABLE = 10
    STATUSES = (
        (STATUS_DISABLE, _("Disable")),
        (STATUS_ENABLE, _("Enable")),
    )
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    status = models.SmallIntegerField(choices=STATUSES, default=STATUS_DISABLE)
    describe = models.CharField(max_length=200,null=True, blank=True)
    category = models.ForeignKey("Category",related_name='category')
    seen = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

class SoftAddition(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    photo = models.ImageField(_('Picture shall be squared, max 640*640, 500k'), upload_to='photos')
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Order(models.Model):
    DELIVERY_STATUS_NEW = 0
    DELIVERY_STATUS_TAKING = 10
    DELIVERY_STATUS_WASHING = 20
    DELIVERY_STATUS_RETURNING = 30
    DELIVERY_STATUS_ARRIVED = 40
    DELIVERY_STATUS_NOT_ARRIVED = 50

    DELIVERY_STATUSES = (
        (DELIVERY_STATUS_NEW, _("New")),
        (DELIVERY_STATUS_TAKING, _("Taking")),
        (DELIVERY_STATUS_WASHING, _("Washing")),
        (DELIVERY_STATUS_RETURNING, _("Returning")),
        (DELIVERY_STATUS_ARRIVED, _("Arrived")),
        (DELIVERY_STATUS_NOT_ARRIVED, _("Not arrived")),
    )

    TIME_MORNING = 0
    TIME_NOON = 1
    TIME_AFTERNOON = 2

    TIME_COMING = (
        (TIME_MORNING, _("5h - 7h")),
        (TIME_NOON, _("11h - 13h")),
        (TIME_AFTERNOON, _("17h - 19h")),
    )

    user = models.ForeignKey(User, related_name='user_order')
    take_man = models.ForeignKey(User, related_name='take_man',null=True, blank=True)
    wash_man = models.ForeignKey(User, related_name='wash_man',null=True, blank=True)
    return_man = models.ForeignKey(User, related_name='return_man',null=True, blank=True)
    product = models.ForeignKey(Product, related_name='orders')
    status = models.SmallIntegerField(choices=DELIVERY_STATUSES, default=DELIVERY_STATUS_NEW)
    creation_date = models.DateTimeField(auto_now_add=True)
    time_taking = models.SmallIntegerField(choices=TIME_COMING)
    time_return = models.SmallIntegerField(choices=TIME_COMING,null=True, blank=True)
    unit = models.FloatField(null=True, blank=True, help_text = _('Take man comfirm kg/unit'))
    estimete_unit = models.FloatField(null=True, blank=True, help_text = _('User estimate there order'))
    money = models.FloatField(null=True, blank=True)
    street_source = models.CharField(max_length=200,null=True, blank=True)
    street_destination = models.CharField(max_length=200,null=True, blank=True)
    rating = models.SmallIntegerField(null=True, blank=True)
    feedback = models.CharField(max_length=200,null=True, blank=True)
    soft = models.ForeignKey(SoftAddition,null=True, blank=True)
    @property
    def total(self):
        if self.unit:
            return self.unit*self.product.price
        return self.estimete_unit*self.product.price

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

class Category(CategoryBase):
    pass
