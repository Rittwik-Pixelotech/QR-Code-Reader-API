from django.db import models


# Create your models here.
class QRCode(models.Model):
    content = models.TextField()
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    processed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
