from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    # 그냥 comment를 달면 db 테이블에 article_id, writer_id 가 null 으로 게시글과 작성자를 알수 없다. 그래서 아래 코드.
    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.article_id =                        self.request.POST.get('article_pk') #article_id 로 db에 바로 넣는 것. article_pk 는 create에서 hidden으로 날렸다.
        # form.instance.article   = Article.objects.get(pk=self.request.POST.get('article_pk'))

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
        #self.object 는 comment 이고 그 comment의 article의 pk 받는 것


@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})