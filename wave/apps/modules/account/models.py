from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#details of user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ('-user',)