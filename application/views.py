from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny,IsAdminUser
from .permissions import IsAdminOrReadOnly



#APIView
class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({'posts': serializer.data})
    

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Вы не указали id'})
        
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({'error': 'Объект не найден'})
        
        serializer = PostSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
    

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Вы не указали id'})
        
        try:
            post = Post.objects.get(pk=pk)
        except:
            return Response({'error': 'Объект не найден'})
        
        post.delete()

        return Response({'post': 'Удален пост  '+ str(pk)})
    permission_classes = (IsAdminOrReadOnly,)
        

    
#ListAPIView
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)



#ListCreateAPIView
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



#UpdateAPIView
class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)




#RetrieveUpdateDestroyAPIView
class PostCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)


#ModelViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)

