from django.urls import path
from . import views as UserViews
from django.contrib.auth import views as AuthViews

urlpatterns = [
    path("register/", UserViews.register, name = "register"),
    path("login/", AuthViews.LoginView.as_view(template_name = "users/login.html"), name = "login"),
    path('logout/', AuthViews.LogoutView.as_view(template_name = "users/logou.html", next_page = "users/logout.html"), name='logout'),
    path("jobs/", UserViews.jobs.as_view(), name = "all_jobs"),
    path("jobs/<int:pk>/", UserViews.jobspec.as_view(), name = "jobs_spec"),
]
