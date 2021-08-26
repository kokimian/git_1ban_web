from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


# @login_required(login_url=reverse_lazy('accountapp:login'))
from articleapp.models import Article


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # success_url = reverse_lazy('accountapp:hello_world') # line 23 reverse과의 차이. 로 바로 받았지만 여기선 lazy가 붙는다. 함수에서 불러오는 방식과 클래스에서 불러오는 방식이 다르다고 생각하자. 깊게 들어가면 복잡.
    template_name = 'accountapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,
                                        **kwargs)


has_ownership = [account_ownership_required, login_required]


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    #success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user: # and 문 추가. 로그인만 되어있으면 다른 사용자의 페이지에 접속 가능한 것을 막기위해.
    #         return super().get(request, *args, **kwargs)    # self.get_object() : self는 현재 AccountUpdateView 에서 사용되고있는 object 즉, urls에서 보면 <int:pk> 를 받는다. pk에 해당되는 object를 가져온다. 만약 6번이라고 하면 (update/6) 그 객체를 가져오는 것. 즉, target_user와 동일하다고 보면 무방
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()


# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().post(request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()