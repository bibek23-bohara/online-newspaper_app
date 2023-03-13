from django import forms
from newspaper_blog.models import Contact, Comment, Post
# from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
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
        
          
     #      widgets = {
     #        "title":forms.TextInput(
     #        attrs={
     #        "class":"form-control",
     #        "placeholder": "enter your title of your post...",
     #        "required":True,
     #        }
     #        ),
     #        'content': SummernoteWidget(),
     #        "status": forms.Select(
     #        attrs={
     #        "class":"form-control",

     #        }
     #        ),
     #        "category": forms.Select(
     #        attrs={
     #        "class":"form-control",
     #        }
     #        ),
     #        "tag": forms.SelectMultiple(
     #        attrs={
     #        "class": "form-control",
     #        "required":True,
     #        }
     #        ),

     #    }

class ContactForm(forms.ModelForm):
     class Meta:
          model = Contact
          fields ="__all__"


class CommentForm(forms.ModelForm):
     class Meta:
          model = Comment
          fields ="__all__"


