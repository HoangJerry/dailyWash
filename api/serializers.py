from rest_framework import fields, serializers
from models import *

class UserBaseSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField('_gender')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
            'gender', 'avatar',)
        
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
    class Meta():
        model = User
    def _gender(self, obj):
        return obj.get_gender_display()
