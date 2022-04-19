from django.urls import path

from . import views

#  ~/login/regist_user를 통해 POST로 요청을 날리면 DB에 데이터를 쌓을 수 있습니다.
urlpatterns = [
    path('regist_user', views.RegistUser.as_view(), name='regist_user'),
]
