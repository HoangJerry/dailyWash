#from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework import generics, status, exceptions, permissions

from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from unify_django.permissions import IsOwnerOrReadOnly
from serializers import *
from django.shortcuts import render

from unify_django import utils
 
def IndexPage(request):
    return render(request, 'angular/index.html', {})

class UserBaseInformations(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer
    

class UserDetailInformations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permissions = [permissions.IsAuthenticated]
    
class UserLogin(generics.ListAPIView):
    serializer_class = UserTokenSerializer
    def post(self, request, format=None):
        email = request.DATA.get('email')
        password = request.DATA.get('password')
        user = None
        if request.user.is_authenticated():
            user = request.user
        elif email and password:
            user = authenticate(email=email, password=password)
        if not user:
            return Response({'user': 'INVALID_PROFILE'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(user)
        return Response(serializer.data)
