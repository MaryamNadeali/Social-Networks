from django.conf import settings
from django.db import models
from django.conf import settings
from django.forms import DateTimeField



# Create your models here.

def upload_image(instance, filename):
    return "posts/{user}/{filename}".format(user=instance.user,filename=filename)

class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)
    updates = models.DateTimeField(auto_now=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content or ""