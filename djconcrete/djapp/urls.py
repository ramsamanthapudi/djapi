from django.urls import path
from .views import APIView,View,APIMethods

urlpatterns = [
    path('view/', APIView.as_view()),
    path('genericAPI/', View.as_view()),
    path('genericapis/<int:pk>', APIMethods.as_view())
]
