
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    
    path('BlogCreateList/',views.BlogCreateListView.as_view()),
    path('BlogCreateList/<int:pk>',views.BlogUpdateRetriveDestroyed.as_view()),

]
