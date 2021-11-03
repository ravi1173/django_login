from rest_framework import serializers
from .models import my_images

class ImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = my_images
        fields = "__all__"
