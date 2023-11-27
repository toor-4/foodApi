from rest_framework import generics
from foodApi.models import MenuItem, Category
from foodApi.serializers import MenuItemSerializer, CategorySerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@permission_classes([IsAuthenticated])
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
