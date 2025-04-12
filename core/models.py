from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = None
    email=models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class Blog(BaseModel):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='blogs')
    title=models.CharField(max_length=50)
    content=models.TextField()

    def __str__(self):
        return self.title

