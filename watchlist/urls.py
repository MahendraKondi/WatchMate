from django.urls import path
from . import views

urlpatterns = [
    path('',views.watch,name='watch')
]