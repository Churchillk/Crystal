from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from users.models import *
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class home(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = 'index/home.html'
    context_object_name = "home_jobs"
    paginate_by = 4
    
    # def get_queryset(self):
    #     # Filter the queryset based on the current user
    #     return super().get_queryset().filter(author=self.request.user)
    

class History(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = "index/history.html"
    context_object_name = "done_jobs"
    paginate_by = 4
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user, status=True)
        return queryset
    