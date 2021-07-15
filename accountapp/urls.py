from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create')
    # 위에선 함수형 view 이기 때문에 hello_world로 바로 불러오지만. 클래스형 view를 가져올때는 as_view를 붙여야한다. 이정도만 알자.
]