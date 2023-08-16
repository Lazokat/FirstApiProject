from django.test import TestCase
from rest_framework.test import *
from .models import *
class Test(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo=Todo.objects.create(title='Hello',body='This is hello')
    def test_model_content(self):
        self.assertEquals(self.todo.title,'Hello')
        self.assertEquals(self.todo.body,'This is hello')
        self.assertEquals(str(self.todo),'Hello')