from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from app.models import BlogPost
from app.serializers import BlogSerializer



class BlogCreateListView(generics.ListCreateAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogSerializer


    def delete(self,*args,**kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogUpdateRetriveDestroyed(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=BlogPost.objects.all()
    serializer_class=BlogSerializer
    
