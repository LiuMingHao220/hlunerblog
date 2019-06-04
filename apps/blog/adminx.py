from .models import Category,Article,Tag
import xadmin
from django.db import models
from markdown_editor.widgets import XAdminMarkdownWidget
# Register your models here.



class ArticleAdmin:
    list_display = ['title', 'author', 'visiting', 'created_time', 'modifyed_time']
    formfield_overrides = {
        models.TextField: {'widget': XAdminMarkdownWidget()},
    }

xadmin.site.register(Category)
xadmin.site.register(Tag)
xadmin.site.register(Article,ArticleAdmin)