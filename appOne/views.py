from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from django.shortcuts import render


# Create your views here.

class projectpage_view(TemplateView):
    template_name = 'project.html'
