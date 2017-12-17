
from channels_api.bindings import ResourceBinding
from channels.binding.websockets import WebsocketBinding
from channels_api.decorators import detail_action, list_action
from pprint import pprint
from django.core.paginator import Paginator
from app import settings
from .models import *
from .serializers import OrderNewSerializer

class OrderBinding(ResourceBinding):
    model = Order
    stream = "orders"
    serializer_class = OrderNewSerializer
    queryset = Order.objects.all()

    @list_action()
    def report(self, data=None, **kwargs):
        # pprint(vars(self.get_queryset()))
        if not data:
            data = {}
        queryset = self.filter_queryset(self.get_queryset().model.objects.filter(status))
        paginator = Paginator(queryset, 25)
        data = paginator.page(data.get('page', 1))
        serializer = self.get_serializer(data, many=True)
        return serializer.data, 200
