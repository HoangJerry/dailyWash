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
    permission_classes = [permissions.IsAuthenticated]
    
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

class Cities(generics.ListAPIView):
    queryset = Address.objects.filter(active=True,parent__isnull=True)
    serializer_class= AddressSerializer

class Districts(generics.ListAPIView):
    serializer_class= AddressSerializer
    def get_queryset(self):
        return Address.objects.filter(active=True,parent=self.kwargs['pk'])

class EmailExist(APIView):
    def get(self, request, format=None):
        email = request.GET.get('email')
        if User.objects.filter(email=email):
            return Response(1)
        return Response(0)

class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

class OrderNew(generics.ListAPIView):
    queryset = Order.objects.filter(status=Order.DELIVERY_STATUS_NEW)
    serializer_class = OrderNewSerializer

class OrderTaking(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderNewSerializer
    # queryset = Order.objects

    # def get_queryset(self):

    #     return Order.objects.filter(take_man=self.request.user,status=Order.DELIVERY_STATUS_TAKING)

    def post(self, request, format=None):
        order = Order.objects.filter(id=request.DATA.get('order_id'))[0]
        order.take_man = self.request.user
        order.status = Order.DELIVERY_STATUS_TAKING
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)
        # return super(OrderTaking, self).get_queryset()



