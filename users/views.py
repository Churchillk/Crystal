from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.views.generic import *
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def register(request):
    if request.method == "POST":
        form = UserReg(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f"account created for {user} successfuly")
            return redirect("login")
        else:
            messages.error(request, "account not created")
    else:
        form = UserReg()
            
    template = loader.get_template("users/register.html")
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

class jobs(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = ("index/jobs_list.html")
    context_object_name = 'users_jobs'
    paginate_by = 4
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=False)
        return queryset
    
class jobspec(LoginRequiredMixin, DetailView):
    model = Jobs
    template_name = ("index/jobspec.html")
    context_object_name = 'jobs_specs'
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = True
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('jobs_spec', kwargs={'pk': self.object.pk}))
    
class Addjob(LoginRequiredMixin, CreateView):
    model = Jobs