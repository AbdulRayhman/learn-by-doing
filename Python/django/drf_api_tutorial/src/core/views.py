from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from  rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import Post
from .serializer import  PostSerializer
from django.contrib.auth.models import User
# User = get_user()
class TestView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
