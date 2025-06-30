from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


"""
1. Default User Modelini extend qilish
class CustomUser(User):
    avatar = ...


2. AbstractUser Modelini extend qilish
class CustomUser(AbstractUser):
    avatar = ...

3. AbstractBaseUser Modelini extend qilish
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = 
    avatar = ...

4. Alohida Profile modelini ochib, default Userga One2One qilish
class Profile(models.Model):
    user = models.One2OneField(CustomUser, on_delete=models.CASCADE)
"""