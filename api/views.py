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
        category = Category.objects.all()
        if id:
            category = Category.objects.filter(id=id)
        return category


class ProductAPI(generics.ListAPIView):
    queryset = Product.objects
    serializer_class = ProductSerializer

    def get_queryset(self):
        id = self.request.GET.get('id',None)
        category_id = self.request.GET.get('category_id',None)
        product = Product.objects.all()
        if id:
            product = Product.objects.filter(id=id)
        if category_id:
            product = Product.objects.filter(category=category_id)
        return product



# *******SOCKET******

# from socketio.namespace import BaseNamespace
# from socketio import socketio_manage

# class ChatNamespace(BaseNamespace):

#     def on_user_msg(self, msg):
#         print "hererer"
#         self.emit('user_msg', msg)

# def socketio_service(request):
#     socketio_manage(request.environ, {'': ChatNamespace}, request)
#     return 'out'


# from gevent import monkey

# from socketio import socketio_manage
# from socketio.server import SocketIOServer
# from socketio.namespace import BaseNamespace
# from socketio.mixins import RoomsMixin, BroadcastMixin


# class ChatNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):
#     def on_nickname(self, nickname):
#         self.request['nicknames'].append(nickname)
#         self.socket.session['nickname'] = nickname
#         self.broadcast_event('announcement', '%s has connected' % nickname)
#         self.broadcast_event('nicknames', self.request['nicknames'])
#         # Just have them join a default-named room
#         self.join('main_room')

#     def recv_disconnect(self):
#         # Remove nickname from the list.
#         nickname = self.socket.session['nickname']
#         self.request['nicknames'].remove(nickname)
#         self.broadcast_event('announcement', '%s has disconnected' % nickname)
#         self.broadcast_event('nicknames', self.request['nicknames'])

#         self.disconnect(silent=True)

#     def on_user_message(self, msg):
#         self.emit_to_room('main_room', 'msg_to_room',
#             self.socket.session['nickname'], msg)

#     def recv_message(self, message):
#         print "PING!!!", message

# class Application(object):
#     def __init__(self):
#         self.buffer = []
#         # Dummy request object to maintain state between Namespace
#         # initialization.
#         self.request = {
#             'nicknames': [],
#         }

#     def __call__(self, environ, start_response):
#         path = environ['PATH_INFO'].strip('/')

#         if not path:
#             start_response('200 OK', [('Content-Type', 'text/html')])
#             return ['<h1>Welcome. '
#                 'Try the <a href="/chat.html">chat</a> example.</h1>']

#         if path.startswith('static/') or path == 'chat.html':
#             try:
#                 data = open(path).read()
#             except Exception:
#                 return not_found(start_response)

#             if path.endswith(".js"):
#                 content_type = "text/javascript"
#             elif path.endswith(".css"):
#                 content_type = "text/css"
#             elif path.endswith(".swf"):
#                 content_type = "application/x-shockwave-flash"
#             else:
#                 content_type = "text/html"

#             start_response('200 OK', [('Content-Type', content_type)])
#             return [data]

#         if path.startswith("socket.io"):
#             socketio_manage(environ, {'': ChatNamespace}, self.request)
#         else:
#             return not_found(start_response)


# def not_found(start_response):
#     start_response('404 Not Found', [])
#     return ['<h1>Not Found</h1>']


# if __name__ == '__main__':
#     print 'Listening on port 8000 and on port 843 (flash policy server)'
#     SocketIOServer(('0.0.0.0', 8000), Application(),
#         resource="socket.io", policy_server=True,
#         policy_listener=('0.0.0.0', 8000)).serve_forever()