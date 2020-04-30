from django.urls import path
from . import views

app_name = "circles"

urlpatterns = [
    path("", views.EventList.as_view(), name="list"),
    path("host", views.EventHost.as_view(), name="host"),
    path("join/<int:id>", views.EventJoin.as_view(), name="join"),
]
