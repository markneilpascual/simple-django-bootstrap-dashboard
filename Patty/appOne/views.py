from django.shortcuts import render

from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


# Create your views here.

class pattyprojectpage(TemplateView):
    template_name = 'project.html'