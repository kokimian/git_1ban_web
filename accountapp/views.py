from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})

#accountapp/hello_world.html


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # line 23 reverse과의 차이. 로 바로 받았지만 여기선 lazy가 붙는다. 함수에서 불러오는 방식과 클래스에서 불러오는 방식이 다르다고 생각하자. 깊게 들어가면 복잡.
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'