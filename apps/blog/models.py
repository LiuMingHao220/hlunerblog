from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown
from django.conf import settings

# Create your models here.



class Category(models.Model):
    name = models.CharField('文章分类',max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    name = models.CharField('文章标签',max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

class Article(models.Model):

    title = models.CharField('文章标题',max_length=128)
    # 创建多对一的关系时，需要添加on_delete=models.CASCADE，作用是级联删除，也就是删除主表数据时，从表也一起删除
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者',on_delete=models.CASCADE)
    img = models.ImageField(upload_to='blog_img',null=True,blank=True,verbose_name='文章配图')
    body = models.TextField(verbose_name='文章内容')
    # null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。
    # blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，比如 admin 界面下增加 model 一条记录的时候。
    abstract = models.CharField('摘要',max_length=512,null=True,blank=True)
    visiting = models.PositiveIntegerField('访问量',default=0)
    category = models.ForeignKey('Category',verbose_name='文章分类', on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField('Tag',verbose_name='文章标签')
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    modifyed_time = models.DateTimeField('修改时间',auto_now=True)






    def __str__(self):
        return self.title

    class Meta:
        # ordering必须是列表或者元组
        ordering = ['-created_time']
        verbose_name = 'article'
        verbose_name_plural = verbose_name

    def body_to_markdown(self):
        return markdown.markdown(self.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

    def get_absolute_url(self):
        # 获取当前博客详情页的url

        # reverse 反向解析url地址
        # 第一个参数：" blog:detailbyid ":  blog应用下的name = detailbyid。detailbyid对应的正则表达式 article/<int:article_id>
        # 第二个参数：self.id会替代正则表达式里面的article_id
        # 然后reverse函数区解析视图函数对应的URL。
        return reverse('blog:detailbyid', kwargs={
            'article_id': self.id,
        })


    def increase_visiting(self):
        # 访问量＋1
        self.visiting += 1
        # 只保存visiting字段
        self.save(update_fields=['visiting'])


    def save(self, *args,**kwargs):
        if not self.abstract:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.abstract = strip_tags(md.convert(self.body))[:54]
            # 调用父类方法写入数据库中
        super(Article,self).save(*args,**kwargs)

    def get_user(self):
        return self.author