from django.urls import path
from .views import getLoginPg,verify

urlpatterns = [
    path('', getLoginPg, name='userlogin'),
    path('verify',verify, name='verify')
]