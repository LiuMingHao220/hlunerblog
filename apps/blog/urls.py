"""webblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from blog.feed import LatestArticlesFeed
# 很重要，注册应用
app_name = "blog"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ?P<value>的意思就是命名一个名字为value的组，匹配规则符合后面的/d+
    path('article/<int:article_id>', views.detail, name='detailbyid'),
    path('category/<int:category_id>', views.CategoryView.as_view(), name='categorybyid'),
    path('tag/<int:tag_id>', views.TagView.as_view(), name ='tagbyid'),
    path('<int:year>/<int:month>', views.ArchivesView.as_view(), name='archives'),
    path('latest/feed/',LatestArticlesFeed(),name='latest_feed'), # RSS订阅
    path('search/', views.MySearchView.as_view(), name='search_view'),  # 全文搜索
    path('get_article_by_author/<slug:author>',views.get_article_by_author,name='get_article_by_author'),

]
