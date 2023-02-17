from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import User


class Twittes(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('User')
    )
    message = models.TextField(verbose_name=_('Message'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email


class TwittesMedia(models.Model):
    twittes = models.ForeignKey(
        Twittes, on_delete=models.CASCADE, verbose_name=_('Twittes'), related_name='media_twittes'
    )
    media = models.ImageField(upload_to='twittes/', verbose_name=_('Media'))
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('User'), related_name='like_user'
    )
    twittes = models.ForeignKey(
        Twittes, on_delete=models.CASCADE, verbose_name=_('Twittes'), related_name='like_twittes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.email


class Comment(models.Model):
    user = models.ForeignKey(
        User, models.CASCADE, verbose_name=_('User'), related_name='comment_user'
    )
    twittes = models.ForeignKey(
        Twittes, on_delete=models.CASCADE, verbose_name=_('Twittes'), related_name='comment_twittes'
    )
    message = models.TextField(verbose_name=_('Message'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.email


class ReTwittes(models.Model):
    user = models.ForeignKey(
        User, models.CASCADE, verbose_name=_('User'), related_name='reTwittes_user'
    )
    twittes = models.ForeignKey(
        Twittes, on_delete=models.CASCADE, verbose_name=_('Twittes'), related_name='reTwittes_twittes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.email
