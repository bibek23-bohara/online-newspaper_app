from django import forms
from newspaper_blog.models import Contact, Comment, Post


class PostForm(forms.ModelForm):
     class Meta:
          model = Post
          fields =("title",
                   "content", 
                   "featured_image", 
                   "status",
                    "category",
                     "tag",
                     )

    
     
class ContactForm(forms.ModelForm):
     class Meta:
          model = Contact
          fields ="__all__"


class CommentForm(forms.ModelForm):
     class Meta:
          model = Comment
          fields ="__all__"


