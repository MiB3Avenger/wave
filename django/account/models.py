from django.db import models
from django.conf import settings

#details of user
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userid = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True)

    def __str__(self):
            return"Profile for user {}".format(self.user.username)

    def save(self, *args, **kwargs):
            if self.user_id:
                self.userid = self.user_id
            super(Profile, self).save(*args, **kwargs)