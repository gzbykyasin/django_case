from .models import Post
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template,Context


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def Pricing(request):
    return render(request=request, template_name='pricing.html')

def Contact(request):
    return render(request=request, template_name='contact.html')