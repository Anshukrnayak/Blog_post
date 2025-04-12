from django.urls import path
from django.urls import  reverse_lazy

from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('',views.PostListView.as_view(),name='home'),
    path('post/',views.PostView.as_view(),name='post'),
    path('update/<int:pk>/',views.PostUpdate.as_view(),name='update_post'),
    path('delete/<int:pk>/',views.PostDeleteView.as_view(),name='delete_post')

]
