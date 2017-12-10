from rest_framework import fields, serializers
from models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta():
        model = Address
        exclude = ['tree_id','rght','lft']

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name','phone',
            'city','district','street')

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

class OrderNewSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSignUpSerializer()
    class Meta():
        model = Order

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'level')


