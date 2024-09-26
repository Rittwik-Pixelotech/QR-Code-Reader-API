from django.contrib import admin

# Register your models here.
from qrcodeapp.models import QRCode


admin.site.register(QRCode)
