from django import template
from ..models import Article,Category,Tag
from user.models import UserProfile
from likes.models import LikeRecord
from user.models import Follow
from pymongo import MongoClient
import datetime


register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_popular_articles(num=5):
    return Article.objects.all().order_by('-visiting')[:num]

@register.simple_tag
def get_catetories():
    return Category.objects.all()

@register.simple_tag
def get_acticle_count_of_category(category_name):
    return Article.objects.filter(category__name = category_name).count()

@register.simple_tag
def archives():
    return Article.objects.all().dates('created_time','month',order='DESC')

@register.simple_tag
def get_articles_count_of_archives(year,month):
    return Article.objects.all().filter(created_time__year=year,created_time__month=month).count()

@register.simple_tag
def get_tags():
    return Tag.objects.all()


@register.simple_tag(takes_context=True)
def get_interest_user(context):
    # 获取当前登录用户
    user = context['user']
    # 获取所有点赞信息
    like_all = LikeRecord.objects.all()
    # 获取当前用户的点赞信息
    like_list = LikeRecord.objects.all().filter(user=user)
    user_list = []
    data = []
    users = dict()
    # 遍历,将当前用户点赞信息与所有除了当前用户之外点赞信息中的点赞文章进行比较,如果相同,加入相同点赞列表中
    for like in like_list:
        for likes in like_all:
            if like.user_id != likes.user_id:
                if like.object_id == likes.object_id:
                    user_list.append( likes.user)
            else:
                continue
    # 遍历列表,如果超过3次,放入字典中
    for i in user_list:
        if user_list.count(i) >= 3:
            users[i] = i
    # 将字典转化为列表,此列表内存放要推荐的用户信息
    users_list =list(users.keys())
    # 当前用户的关注信息
    follows = Follow.objects.all().filter(follower=user)
    # 当前用户关注列表
    follows_list = []
    for i in follows:
        follows_list.append(i.followed)

    # 如果推荐用户在当前用户的关注表中,则不推荐
    for i in users_list:
        if i in follows_list:
            continue
        else:
            data.append(i)

    return data

@register.simple_tag
def get_interest_news():
    client = MongoClient(host='127.0.0.1', port=27017)
    formatted_today = datetime.date.today().strftime('%y%m%d')
    collection = client['news']['news_{}'.format(formatted_today)]
    list_collection_news = list(collection.find())
    list_news =[]
    for news in list_collection_news:
        dict_news = {}
        dict_news['url'] = str(news['url']).replace('[', '')
        dict_news['url'] = dict_news['url'].replace(']', '')
        dict_news['url'] = dict_news['url'].replace("'", "")
        dict_news['title'] = str(news['title']).replace('[', '')
        dict_news['title'] = dict_news['title'].replace(']', '')
        dict_news['title'] = dict_news['title'].replace("'", "")
        list_news.append(dict_news)

    return list_news

