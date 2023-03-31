from django.urls import path

from alpine import views


urlpatterns = [path("", views.index, name="basic_html-home")]
