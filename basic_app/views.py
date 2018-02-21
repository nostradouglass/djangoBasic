from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView)
from django.urls import reverse_lazy

from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context


class SchoolCreateView(CreateView):
    model = models.School
    fields = ("name", "principal", "location")

class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:schools")