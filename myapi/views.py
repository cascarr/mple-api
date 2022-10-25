from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post

import requests

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

def home(request):
    response = requests.get('http://127.0.0.1:8000/posts/')
    data = response.json()
    context = {
         'data': data 
    }

    return render(request, 'home.html', context)