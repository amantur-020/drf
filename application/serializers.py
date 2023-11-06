from rest_framework import serializers
from .models import Post
from rest_framework.renderers import JSONRenderer




# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()
#     author = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.author = validated_data.get('author', instance.author)
#         instance.created_at = validated_data.get('created_at', instance.created_at)
#         instance.save()
#         return instance



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

