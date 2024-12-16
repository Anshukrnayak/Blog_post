
from rest_framework import serializers
from app.models import BlogPost


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields='__all__'

        