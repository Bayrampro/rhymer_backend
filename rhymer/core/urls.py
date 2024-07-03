from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/allwords/<str:word>', AllWordsAPIView.as_view())
]
