from django.contrib.syndication.views import Feed
from .models import Article


class LatestArticlesFeed(Feed):
    link = 'hluner.cn'
    description = '最新文章'

    def items(self):
        return Article.objects.all().order_by('-created_time')[:5]


    def item_title(self,item):
        return item.title


    def item_description(self, item):
        return item.abstract

