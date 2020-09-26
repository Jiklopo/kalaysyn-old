from django.urls import path
from main.views import *

urlpatterns = [
    path('', IndexView.as_view())
]