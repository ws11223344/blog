#进行user子应用的试图路由
from django.urls import path
from users.views import RegisterView
urlpatterns = [
    #path第一个参数 路由
    #path第二个参数 视图函数
    path('register/',RegisterView.as_view(),name='register'),
]