from django.urls import path
from .views import *
urlpatterns=[
    path('',CreateTodo.as_view(),name='create'),
    path('<int:pk>/',EditTodo.as_view(),name='edit')
]