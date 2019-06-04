from django.shortcuts import render,redirect,HttpResponse,reverse
from .forms import RegForm,ProfileForm
from django.contrib import auth
from .models import UserProfile,Follow
from django.contrib import messages
from django.http import JsonResponse
from likes.models import LikeRecord
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.



def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()

            # 注册成功,将用户登录，跳转回首页
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        reg_form = RegForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'registration/register.html', context={'reg_form': reg_form})


def user_info(request):

    return render(request,'blog/user_info.html')


def change_profile(request):
    if request.method == 'POST':
        # 上传文件需要使用request.FILES
        form = ProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            # 添加一条信息,表单验证成功就重定向到个人信息页面
            messages.add_message(request,messages.SUCCESS,'个人信息更新成功！')
            return redirect('user:user_info')
    else:
        # 不是POST请求就返回空表单
        form = ProfileForm(instance=request.user)
    return render(request,'blog/change_user_info.html',context={'form':form})


def set_follower(request,follower,followed):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    follower = UserProfile.objects.get(username=follower)# 关注人
    followed = UserProfile.objects.get(username=followed)# 被关注人
    follower_list = Follow.objects.all().filter(follower=follower) #获取当前用户的列表
    # print(follower_list)
    f_list = []
    for follower_user in follower_list:
            # 遍历列表,将列表中被关注人的信息存到f_list
            f_list.append(follower_user.followed)
    # 如果当前要关注的人不在已关注的列表中,那么存入数据库
    if not followed in f_list:
        follows = Follow(follower=follower,followed=followed)
        follows.save()
        # data['status'] = 'SUCCESS'
        message = '关注成功'

    else:
        # data['status'] = 'ERROR'
        message = '您已经关注了'



    return redirect(referer,locals())


def add_follower(request,follower,followed):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    follower = UserProfile.objects.get(username=follower)# 关注人
    followed = UserProfile.objects.get(username=followed)# 被关注人
    follower_list = Follow.objects.all().filter(follower=follower) #获取当前用户的列表
    # print(follower_list)
    f_list = []
    data={}
    for follower_user in follower_list:
            # 遍历列表,将列表中被关注人的信息存到f_list
            f_list.append(follower_user.followed)
    # 如果当前要关注的人不在已关注的列表中,那么存入数据库
    if not followed in f_list:
        follows = Follow(follower=follower,followed=followed)
        follows.save()
        data['status'] = 'SUCCESS'


    else:
        data['status'] = 'ERROR'


    return JsonResponse(data)

def get_follower(request):
    # 获取关注列表
    user = request.user
    follow = Follow()
    follow_list = follow.user_followed(user)
    return render(request,'blog/follow_list.html',locals())


def delete_follower(request,follower,followed):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    follower = UserProfile.objects.get(username=follower)  # 关注人
    followed = UserProfile.objects.get(username=followed)  # 被关注人
    follow = Follow.objects.all().filter(follower=follower,followed=followed)
    follow.delete()

    return redirect(referer)

