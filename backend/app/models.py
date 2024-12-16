from django.db import models

class BlogPost(models.Model):
    image=models.ImageField(upload_to='blog_image')
    title=models.CharField(max_length=50)
    content=models.TextField()
    pushlid_date=models.DateField(auto_now_add=True)

    def __str__(self): return self.title

    