from django.shortcuts import render
from django.urls import reverse_lazy
from LernApp.models import LernKarte, Project
from LernApp.forms import LernModelForm
from django.views.generic import (CreateView, DetailView,
                                  UpdateView, DeleteView,
                                  TemplateView, ListView)

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ProjectListView(ListView):
    model = Project


class LernKartenListView(ListView):
    model = LernKarte


class LernKarteCreate(CreateView):
    model = LernKarte
    fields = ['name', 'tag', 'project', 'text']


class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', ]


class LernKarteDetail(DetailView):
    model = LernKarte
    form_class = LernModelForm


class LernKarteUpdate(UpdateView):
    model = LernKarte
    fields = ['name', 'tag', 'text']


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name', ]


class LernKarteDelete(DeleteView):
    model = LernKarte
    success_url = reverse_lazy('index')


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('index')
