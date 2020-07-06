from django.shortcuts import render
from rest_framework import generics
from .serializers import QuoteSerializers
from .models import Quote
from .paginations import QuotePagination
from .permissions import IsAdminorReadonly

# Create your views here.

class GenericQuoteView(generics.ListCreateAPIView):
    serializer_class = QuoteSerializers
    queryset = Quote.objects.all().order_by('id')
    pagination_class = QuotePagination
    permission_classes = [IsAdminorReadonly]


class GenericQuoteUGD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializers
    pagination_class = QuotePagination
    permission_classes = [IsAdminorReadonly]
