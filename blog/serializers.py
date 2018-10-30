from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ['likes'] #__all__ for all fields
