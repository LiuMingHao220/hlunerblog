from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import signals



class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=20,verbose_name='昵称',blank=True,null=True)
    user_img = models.ImageField(upload_to='user_img',blank=True,null=True,verbose_name='头像',default='user_img/user.jpeg')


    class Meta(AbstractUser.Meta):
        pass


    def __str__(self):
        return self.username


class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follower', on_delete=models.CASCADE)
    # on_delete是Django2必须要的
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followed', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return '{self.follower} follow {self.followed}'


    @staticmethod
    def follow(from_user, to_user):
        Follow(follower=from_user,
               followed=to_user).save()  # 关注方法


    @staticmethod
    def unfollow(from_user, to_user):
        f = Follow.objects.filter(follower=from_user, followed=to_user).all()
        if f:
            f.delete()  # 取关


    @staticmethod
    def user_followed(from_user):
        followeders = Follow.objects.filter(follower=from_user).all()
        user_followed = []
        for followeder in followeders:
            user_followed.append(followeder.followed)
        return user_followed  # 得到from_user关注的人，返回列表




def get_nickname(self):
    if UserProfile.objects.filter(user=self).exists():
        profile = UserProfile.objects.get(user=self)
        return profile.nickname
    else:
        return ''

def get_nickname_or_username(self):
    if UserProfile.objects.filter(user=self).exists():
        profile = UserProfile.objects.get(user=self)
        return profile.nickname
    else:
        return '[%s]' % self.username

def has_nickname(self):
    return UserProfile.objects.filter(user=self).exists()

User.get_nickname = get_nickname
User.get_nickname_or_username = get_nickname_or_username
User.has_nickname = has_nickname