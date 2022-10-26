from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
    )
    email_verify = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.author}'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_text = models.TextField()
    post = models.ForeignKey(mmorpg, on_delete=models.CASCADE, related_name='replies')


class OneTimeCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)