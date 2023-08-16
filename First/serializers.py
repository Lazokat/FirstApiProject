from .models import *
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model=Todo
        fields='__all__'