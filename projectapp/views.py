from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    # success_url = reverse_lazy('articleapp:list')
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})
        # self.object는 create view 에서 만들고 있는 객체 즉, model=Project


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 20

    # mixin되는 Project list가 담기는 개체는 기본적으로 object_list로 지정된다
    # 아래와 같이 오버라이드(detail.html 에서 사용할 문맥 정보들을 커스터마이징 하는 것)
    def get_context_data(self, **kwargs):
        user = self.request.user
        project = self.object

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,
                                                       project=project)

        else:
            subscription = None

        article_list = Article.objects.filter(project=self.object)
        # Article뷰의 객체중에 project가 self.object(지금 이 Project의 객체인 Project)와 같은 게시글들만
        return super().get_context_data(object_list=article_list,
                                        subscription=subscription,
                                        **kwargs)
        # Project의 context_object_name인 'target_project'는 DetailView에서 쓰고 object_list라는 context_object_name으로  article_list를 설정


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'  # 보통 만드는 방식(target-project) 아님. 게시판의 list를 담고 있다는 뜻??
    template_name = 'projectapp/list.html'
    paginate_by = 20