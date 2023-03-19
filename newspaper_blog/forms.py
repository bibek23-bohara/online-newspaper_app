from django import forms
from newspaper_blog.models import Contact, Comment, Post, Tag, Category


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


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Name of tag...",
                }
            ),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Name of category...",
                }
            ),
        }