from django.shortcuts import render

# Create your views here.
from django.views.generic import UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password

# if user_id 가 특수문자인지.. 숫자인지.. 한글인지.. 이런것들을 전부 처리해줘야함.

class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")
        user = LoginUser.objects.filter(user_id=user_id).first()
        if user is None:
            return Response(dict(msg="해당 ID의 사용자가 없습니다."))
        if check_password(user_pw, user.user_pw):
            return Response(dict(msg="로그인 성공"))
        else:
            return Response(dict(msg="로그인 실패. 패스워드 불일치"))



class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "") # 클라이언트에서 올리는 user_id
        user_pw = request.data.get('user_pw', "") # 클라이언트에서 올리는 user_pw
        user_pw_crypted = make_password(user_pw)


        if LoginUser.objects.filter(user_id=user_id).exists():
            data = dict(
                msg="이미 존재하는 아이디입니다."
            )
            return Response(data)


        LoginUser.objects.create(user_id=user_id, user_pw=user_pw_crypted) # LoginUser 모델에 새로운 object 생성

        # 클라이언트한테 내려줄 데이터 정의
        data = dict(
            user_id=user_id,
            user_pw=user_pw_crypted
        )


        return Response(data=data)
