from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    # name = models.CharField(max_length= 50, blank = False)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default = 2)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                                    blank=True)
    def __str__(self):
        return f'Profile of {self.user.username}'