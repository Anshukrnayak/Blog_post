
from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import BlogForm,RegisterForm
from .models import Blog,CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout
from django.contrib import messages


class RegisterView(generic.CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = 'account/register.html'
    context_object_name = 'form'
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)

class LogoutView(LoginRequiredMixin,generic.View):
    def get(self,request):
        logout(request)
        return redirect('login')


class PostListView(LoginRequiredMixin, generic.ListView):
    template_name = 'home/index.html'
    model = Blog
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.all().order_by('-created_at')

class PostView(LoginRequiredMixin,generic.CreateView):
    template_name = 'home/create.html'
    model = Blog
    form_class = BlogForm
    context_object_name = 'form'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        blog=form.save(commit=False)
        blog.author=self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin,generic.View):

    def get(self,request,*args,**kwargs):

        try:
            instance=Blog.objects.get(id=kwargs['pk'])
        except Blog.DoesNotExist:
            messages.info(request,"Blog doestn't exist.... ")
            return reverse_lazy('home')

        form=BlogForm(instance=instance)
        return render(request,'home/create.html',{'form':form})

    def post(self,request,*args,**kwargs):
        try:
            instance=Blog.objects.get(id=kwargs['pk'])
        except Blog.DoestNotExist:
            messages.warning(request,"Blog not updated ")
            return redirect('home')

        form=BlogForm(instance=instance,data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        return render(request,'home/create.html',{'form':form})


class PostDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Blog
    template_name = 'home/delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)






