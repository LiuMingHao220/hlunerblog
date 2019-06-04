from django.shortcuts import render,redirect,get_object_or_404,reverse
from blog import models
from notifications.models import Notification



def home(request):
    articles = models.Article.objects.all().order_by('-visiting')[:3]
    # 寻找名为page的GET参数，默认值为1。

    return render(request,'blog/home.html',locals())


def my_notifications(request):

    return render(request,'blog/my_notifications.html',locals())


def my_notification(request, my_notification_pk):
    my_notification = get_object_or_404(Notification, pk=my_notification_pk)
    my_notification.unread = False
    my_notification.save()
    return redirect(my_notification.data['url'])

def delete_my_read_notifications(request):
    notifications = request.user.notifications.read()
    notifications.delete()
    return redirect(reverse('my_notifications'))