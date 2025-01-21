from django.contrib.auth.models import User
from django.db import models


# Create your models here.


#
class History(models.Model):
   # user_id = models.IntegerField(blank=True, null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    user_number = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    rec_to_history = models.BooleanField(default=True)

    def __str__(self):
        return self.ip_address
