from django.urls import path

from htmx import views


urlpatterns = [path("", views.index, name="htmx-home")]
