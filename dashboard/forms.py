from django import forms
from .models import *

class my_image_form(forms.ModelForm):
    class Meta:
        model = my_images
        fields = ('img', 'username')
        
