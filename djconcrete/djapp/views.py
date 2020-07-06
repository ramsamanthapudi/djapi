from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin
from .models import Products
from .serializers import productserializer
from rest_framework import permissions
from .paginations import setPaginationforview
# Create your views here.

class View(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Products.objects.all()
    serializer_class = productserializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)


# Concrete class which uses generics classes which inturn uses mixins and generics classes , here code will be less as it provides more abstraction
class APIView(generics.ListCreateAPIView):
    queryset = Products.objects.all().order_by("Id")
    serializer_class = productserializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = setPaginationforview

class APIMethods(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = productserializer


