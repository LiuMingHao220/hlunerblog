from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
import django.utils.timezone as timezone
import datetime
from django.conf import settings
# Create your models here.


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    comment_text = models.TextField('评论内容')
    comment_time = models.DateTimeField('评论时间',default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='评论人',related_name='comments',on_delete=models.CASCADE)

    root = models.ForeignKey('self',related_name='root_comment',null=True,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',related_name='parent_comment',null=True,on_delete=models.CASCADE)
    reply_to = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='replies',null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text

    def get_user(self):
        return self.user

    def get_absolute_url(self):
        return self.content_object.get_absolute_url()

    class Meta:
        ordering = ['comment_time']
        verbose_name = '评论详情'
        verbose_name_plural = verbose_name

