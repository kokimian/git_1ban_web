from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp' # line 10 에서 라우트 할때 accountapp/xxx.html 의 앞부분 accoutapp 설정하는게 이것이다

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    # 위에선 함수형 view 이기 때문에 hello_world로 바로 불러오지만. 클래스형 view를 가져올때는 as_view를 붙여야한다. 이정도만 알자.
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # pk는 primary key 고유값
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]