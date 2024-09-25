from django.contrib import admin
from django.urls import path
from qrcodeapp.views import QRCodeReaderAPI

urlpatterns = [path("generator", QRCodeReaderAPI.as_view(), name="qr_generator")]
