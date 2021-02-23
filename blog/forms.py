from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','intro','category','coverimage','content','tags']

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','intro','category','coverimage','tags','content',]

    
