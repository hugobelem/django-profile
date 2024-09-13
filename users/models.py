from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email
    

class UserProfile(models.Model):
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.email}'
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

