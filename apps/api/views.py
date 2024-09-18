from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.api.serializers import OrdersSerializer
from apps.orders.models import Orders


def api_home(request):
    return render(request, 'api/api_home.html')

@api_view(['GET'])
def getOrder(request, uuid):
    try:
        order = Orders.objects.get(uuid=uuid)
        serializer = OrdersSerializer(order)
        return Response(serializer.data)
    except Orders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
