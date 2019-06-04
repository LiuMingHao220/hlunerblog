from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path(r'register/', views.register, name='register'),
    path('user_info/',views.user_info,name='user_info'),
    path('change_profile/',views.change_profile,name='change_profile'),
    path('set_follower/<slug:follower>/<slug:followed>',views.set_follower,name='set_follower'),
    path('add_follower/<slug:follower>/<slug:followed>',views.add_follower,name='add_follower'),

    path('get_follower/',views.get_follower,name='get_follower'),
    path('delete_follower/<slug:follower>/<slug:followed>',views.delete_follower,name='delete_follower'),
    # path('get_interest_user/',views.get_interest_user,name = 'get_interest_user'),

]