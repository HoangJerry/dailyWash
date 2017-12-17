from rest_framework import fields, serializers
from models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta():
        model = Address
        exclude = ['tree_id','rght','lft']

class UserSignUpSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField('_address')

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name','phone',
            'city','district','street','address')
    def _address(self,obj):
        return obj.address

class UserBaseSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField('_gender')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
            'gender', 'avatar','is_wash_man','is_delivery_man')
        
    def _gender(self, obj):
        return obj.get_gender_display()

class UserTokenSerializer(UserBaseSerializer):
    token = serializers.CharField()
    gender = serializers.SerializerMethodField('_gender')
    class Meta(UserBaseSerializer):
        model = User
        fields = UserBaseSerializer.Meta.fields+('token',)

    def _gender(self, obj):
        return obj.get_gender_display()

class UserDetailSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField('_gender')
    city = AddressSerializer()
    district = AddressSerializer()
    address = serializers.SerializerMethodField('_address')
    class Meta():
        model = User
        exclude = ['password']
    def _gender(self, obj):
        return obj.get_gender_display()
    def _address(self,obj):
        return obj.address
        
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ('id', 'image',)

class ProductSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    class Meta():
        model = Product

class OrderSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField('_status')
    price = serializers.SerializerMethodField('_price')
    class Meta():
        model = Order
        fields = ('id','status')

    def _status(self, obj):
        return obj.get_status_display()
    def _price(self, obj):
        return obj.total

class OrderNewSerializer(OrderSerializer):
    product = ProductSerializer()
    user = UserSignUpSerializer()
    class Meta():
        model = Order
        # fields = ('id', 'user', 'product','estimete_unit')

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'level')


