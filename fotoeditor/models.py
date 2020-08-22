from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'fotoscan/images/{1}'.format(filename)

class Images(models.Model):
    file = models.ImageField(upload_to=user_directory_path, blank=True,null=True),
    pub_date = models.DateTimeField('date published', default=timezone.now)
