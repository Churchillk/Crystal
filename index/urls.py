from django.urls import path
from . import views as IndexView

urlpatterns = [
    path("", IndexView.home.as_view(), name = "home"),
    path("history/", IndexView.History.as_view(), name = "history"),
]
