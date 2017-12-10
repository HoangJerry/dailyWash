#from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework import generics, status, exceptions, permissions
from rest_framework.exceptions import APIException
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from unify_django.permissions import IsOwnerOrReadOnly
from serializers import *
from django.shortcuts import render

from unify_django import utils


def IndexPage(request):
    return render(request, 'angular/index.html', {})


# api exceptions
class ServiceUnavailable(APIException):
    status_code = 500
    default_detail = 'Service temporarily unavailable, try again later.'


class UserBaseInformations(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer


class WashMan(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.filter(is_wash_man=True)
    serializer_class = UserBaseSerializer


class UserDetailInformations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class UserMeInformations(generics.ListAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

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
    queryset = Address.objects.filter(active=True, parent__isnull=True)
    serializer_class = AddressSerializer


class Districts(generics.ListAPIView):
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(active=True, parent=self.kwargs['pk'])


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

    def post(self, request, format=None):
        # check data in request
        print(request.data)

        if 'order_id' in request.data:

            # check order_id pass database
            try:
                order = Order.objects.filter(
                    id=request.DATA.get('order_id'))[0]
            except Exception, e:
                print('Error class OrderTaking ', e)
                return Response({'meassages': 'Not found order'}, status=status.HTTP_400_BAD_REQUEST)
            order.take_man = self.request.user
            order.status = Order.DELIVERY_STATUS_TAKING
            order.save()
            serializer = self.get_serializer(order)
            return Response(serializer.data)

        print('Error class OrderTaking')
        raise ServiceUnavailable


class OrderWashing(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderNewSerializer

    def post(self, request, format=None):
        # check data in request
        if 'order_id' in request.data:

            # check order_id pass database
            try:
                order = Order.objects.filter(
                    id=request.DATA.get('order_id'))[0]
            except Exception, e:
                print('Error class OrderWashing ', e)
                return Response({'meassages': 'Not found order'}, status=status.HTTP_400_BAD_REQUEST)
            order.wash_man = self.request.user
            order.status = Order.DELIVERY_STATUS_WASHING
            order.save()
            serializer = self.get_serializer(order)
            return Response(serializer.data)

        print('Error class OrderWashing')
        raise ServiceUnavailable


class OrderWashed(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderNewSerializer

    def post(self, request, format=None):
        # check data in request
        if 'order_id' in request.data:

            # check order_id pass database
            try:
                order = Order.objects.filter(
                    id=request.DATA.get('order_id'))[0]
            except Exception, e:
                print('Error class OrderWashed ', e)
                return Response({'meassages': 'Not found order'}, status=status.HTTP_400_BAD_REQUEST)
            order.status = Order.DELIVERY_STATUS_WASHED
            order.save()
            serializer = self.get_serializer(order)
            return Response(serializer.data)

        print('Error class OrderWashed')
        raise ServiceUnavailable


class OrderReturning(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderNewSerializer

    def post(self, request, format=None):
        # check data in request
        if 'order_id' in request.data:

            # check order_id pass database
            try:
                order = Order.objects.filter(
                    id=request.DATA.get('order_id'))[0]
            except Exception, e:
                print('Error class OrderReturning ', e)
                return Response({'meassages': 'Not found order'}, status=status.HTTP_400_BAD_REQUEST)
            order.return_man = self.request.user
            order.status = Order.DELIVERY_STATUS_RETURNING
            order.save()
            serializer = self.get_serializer(order)
            return Response(serializer.data)

        print('Error class OrderReturning')
        raise ServiceUnavailable


class OrderArrived(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderNewSerializer

    def post(self, request, format=None):
        # check data in request
        if 'order_id' in request.data:

            # check order_id pass database
            try:
                order = Order.objects.filter(
                    id=request.DATA.get('order_id'))[0]
            except Exception, e:
                print('Error class OrderArrived ', e)
                return Response({'meassages': 'Not found order'}, status=status.HTTP_400_BAD_REQUEST)
            order.return_man = self.request.user
            order.status = Order.DELIVERY_STATUS_ARRIVED
            order.save()
            serializer = self.get_serializer(order)
            return Response(serializer.data)

        print('Error class OrderArrived')
        raise ServiceUnavailable


class OrderAllArrived(generics.ListAPIView):
    queryset = Order.objects.filter(status=Order.DELIVERY_STATUS_ARRIVED)
    serializer_class = OrderNewSerializer


class TakingPending(generics.ListAPIView):
    queryset = Order.objects
    serializer_class = OrderNewSerializer

    def get_queryset(self):
        return Order.objects.filter(take_man=self.request.user.id, status=Order.DELIVERY_STATUS_TAKING)

class AllTakingPending(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.filter(status=Order.DELIVERY_STATUS_TAKING)
    serializer_class = OrderNewSerializer

class ReturningPending(generics.ListAPIView):
    queryset = Order.objects
    serializer_class = OrderNewSerializer

    def get_queryset(self):
        return Order.objects.filter(return_man=self.request.user.id, status=Order.DELIVERY_STATUS_RETURNING)

class WashingPending(generics.ListAPIView):
    queryset = Order.objects
    serializer_class = OrderNewSerializer

    def get_queryset(self):
        return Order.objects.filter(wash_man=self.request.user.id, status=Order.DELIVERY_STATUS_WASHING)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderNewSerializer

class CategoryAPI(generics.ListAPIView):
    queryset = Category.objects
    serializer_class = CatagorySerializer

    def get_queryset(self):
        id = self.request.GET.get('id',None)
        category = Category.objects.filter(active=True)
        if id:
            category = category.filter(id=id)
        return category


class ProductAPI(generics.ListAPIView):
    queryset = Product.objects
    serializer_class = ProductSerializer

    def get_queryset(self):
        id = self.request.GET.get('id',None)
        category_id = self.request.GET.get('category_id',None)
        product = Product.objects.filter(status=Product.STATUS_ENABLE).order_by('?')
        if id:
            product = product.filter(id=id)
        if category_id:
            product = product.filter(category=category_id)
        return product



# *******SOCKET******

