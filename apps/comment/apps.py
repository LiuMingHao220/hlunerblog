from django.apps import AppConfig


class CommentConfig(AppConfig):
    name = 'comment'
    verbose_name = '评论信息'

    def ready(self):
        super(CommentConfig, self).ready()
        from . import signals