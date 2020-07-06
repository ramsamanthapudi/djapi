from django.urls import path
from .views import GenericQuoteView

urlpatterns = [
    path('quotes/', GenericQuoteView.as_view()),
    path('quotes/<int:pk>', GenericQuoteView.as_view()),
]