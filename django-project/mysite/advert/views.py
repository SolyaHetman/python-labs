from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from advert.models import Advert

# Create your views here.
class Advertlist(ListView):
    template_name  = 'advert_list.html'
    context_object_name = 'adverts'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Advert.objects.all()
        else:
            return Advert.objects.filter(is_public = True)

class AdvertCreate(LoginRequiredMixin, CreateView):
    template_name  = 'advert_create.html'
    model = Advert
    fields = ('name', 'content')

    def form_valid(self, form):
        advert = form.save(commit=False)
        advert.user = self.request.user
        advert.save()
        return super(AdvertCreate, self).form_valid(form)

    def get_success_url(self):
        return '/advets'


class AdvertUpdate(LoginRequiredMixin, UpdateView):
    template_name  = 'advert_create.html'
    model = Advert
    fields = ('name', 'content')

    def get_success_url(self):
        return '/advets'


class AdvertDelete(LoginRequiredMixin, DeleteView):
    template_name  = 'advert_delete.html'
    model = Advert
    fields = ('name', 'content')

    def get_success_url(self):
        return '/advets'

def index(request):
    return render (request, 'user_example/index.html')