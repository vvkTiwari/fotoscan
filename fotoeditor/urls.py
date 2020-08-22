from django.urls import path

from . import views

urlpatterns = [
    path('my-editor', views.image_display_editor, name='display_editor'),
]