from django.db import models

# Create your models here.
CHoices=((True,'Completed'),(False,'Not Completed'))
class Todo(models.Model):
    title=models.CharField(max_length=50,verbose_name='Todo title',help_text='Enter title',unique=True)
    body=models.TextField(verbose_name='Post body',help_text='Write about details of your to-do')
    Completed=models.BooleanField(verbose_name='Is it Completed?',help_text='If you complete,then click',choices=CHoices,default=False)

    def __str__(self):
        return self.title

