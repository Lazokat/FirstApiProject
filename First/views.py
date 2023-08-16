from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *
# Create your views here.

class CreateTodo(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = PostSerializer
class EditTodo(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = PostSerializer