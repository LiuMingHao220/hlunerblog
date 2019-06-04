# mysite
## 开发环境
    ubuntu 18.04
    MySQL 5.7
## 主要功能
- 文章，页面，分类目录，标签的添加，删除，编辑等。文章及页面支持Markdown，支持代码高亮
- 集成haystack支持文章全文搜索并高亮显示
- 完整的评论功能，包括发表回复评论，点赞评论
- 站内消息通知，将点赞和评论信息通知给用户
- 侧边栏标签云，分类，归档
- 后台集成markdown-editor，支持二合一预览写文章
## 安装
使用pip安装
> pip install -r requirements.txt

## 配置
在setting.py中设置DATABASES，将其中的信息修改为你自己的。
修改如下：
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoblog',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': 3306,
    }
}
```
## 运行
创建数据库
>CREATE DATABASE `mysite`

进入项目目录,生成迁移文件
>python manage.py makemigrations

>python manage.py migrate

创建超级用户
>python manage.py createsuperuser

运行项目
> python manage.py runserver