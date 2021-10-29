from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.TodoCreate.as_view(), name='todos_create'),
    path('delete/<int:pk>/', views.TodoDelete.as_view(), name='todo_delete')
]