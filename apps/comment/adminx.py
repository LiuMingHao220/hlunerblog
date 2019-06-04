from django.contrib import admin
from .models import Comment
from xadmin import views
import xadmin
from django.db import models
from markdown_editor.widgets import XAdminMarkdownWidget
# Register your models here.


class CommentAdmin:
    list_display = ['comment_text', 'comment_time', 'user','root','parent']



xadmin.site.register(Comment,CommentAdmin)