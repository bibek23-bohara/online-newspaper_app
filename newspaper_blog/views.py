from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView, View)

from newspaper_blog.forms import CommentForm, ContactForm, PostForm, TagForm, CategoryForm
from newspaper_blog.models import Category,Post,Tag
PAGINATE_BY = 1


class Homeview(ListView):
    name = Post
    template_name="zennews/home.html"
    context_object_name="posts"
    queryset = Post.objects.filter(status="active", published_at__isnull=False)

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["featured_post"]=(
            Post.objects.filter(status="active", published_at__isnull=False)
            .order_by("-published_at")
            .first()
        )
        context["slider_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-published_at")[:5]
        context["post_grids"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[4:5]
        context["post_right_grids"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[2:5]
        context["post_left_grids"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-created_at")[3:5]
        context["trandings"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-published_at")[:5]
        context["politics_left_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[4:5]
        context["politics_left_down_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[3:5]
        context["politics_left_up_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[6:7]
        context["politics_right_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[:5]
        context["bussiness_right_categories"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[4:5]
        context["bussiness_left_up_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[4:5]
        context["bussiness_left_down_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[4:5]
        context["bussiness_right_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[4:5]
        context["bussiness_left_categories"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[2:7]
        context["politics_left_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[6:7]
        context["politics_left_down_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[6:7]
        context["politics_left_up_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[5:6]
        context["politics_left_middle_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("published_at")[:3]
        context["politics_right_left_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[1:3]
        context["politics_right_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[2:7]
        context["footer_categories"]=Category.objects.all()[:6]
        context["recent_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-published_at")[:4]
        return context





class PostDetailView(DetailView):
    model = Post
    template_name ="zennews/detail.html"
    context_object_name="post"


    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        obj = self.get_object()
        context["trending_posts"]=(
            Post.objects.filter(status="active", published_at__isnull=False)
            .order_by("-views_count")[:5]
    )
        context["latest_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-published_at")[:5]
        context["popular_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-tag")[:5]
        context["footer_categories"]=Category.objects.all()[:6]
        context["recent_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-published_at")[:4]
        return context
    

class PostCategoryView(ListView):
    model = Post
    template_name = "zennews/category_post.html"
    context_object_name ="posts"
    queryset = Post.objects.filter(status="active", published_at__isnull=False).order_by("-published_at")[:8]
    paginate_by = 1

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["trending_posts"]=(
            Post.objects.filter(status="active", published_at__isnull=False)
            .order_by("-views_count")[:5]
        )
        context["latest_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-published_at")[:5]
        context["popular_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-tag")[:5]
        context["category_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-published_at")
        return context

class PostByCategoryView(ListView):
    model = Post
    template_name = "zennews/category_post.html"
    context_object_name ="posts"
    paginate_by = 1
    def get_queryset(self):
        super().get_queryset()
        queryset =Post.objects.filter(status="active", published_at__isnull=False, category=self.kwargs["cat_id"]).order_by("-published_at").all()
        return queryset
    

class PostByTagView(ListView):
    model = Post
    template_name = "zennews/category_post.html"
    context_object_name ="posts"
    paginate_by = 1
    def get_queryset(self):
        super().get_queryset()
        queryset =Post.objects.filter(status="active", published_at__isnull=False, category=self.kwargs["tag_id"]).order_by("-published_at").all()
        return queryset
    

class AboutView(TemplateView):
    template_name ="zennews/about.html"
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["latest_about_posts"]=(
            Post.objects.filter(status="active", published_at__isnull=False)
            .order_by("-published_at")[:1]
        )
        context["footer_categories"]=Category.objects.all()[:6]
        context["recent_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-published_at")[:4]
        return context
    
class ContactView(View):
    template_name = "zennews/contact.html"
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully submitted your Query. We will contact you soon."

            )
        else:
            messages.success(
                request, "Sorry your Query Cannot be submitted. Please check agin and try again."

            )
        return render(
            request,
            self.template_name,
            {"form":form},
        )
    
class CommentView(View):
    from_class = CommentForm
    template_name = "zennews/detail.html"

    def post(self, request, *args, **kwargs):
        form = self.from_class(request.POST)
        post = request.POST["post"]
        if form.is_valid():
            form.save()
            return redirect("post-detail", post)
        else:
            post = Post.objects.get(pk=post)
            return render(
                request,
                self.template_name,
                {"post":post, "form":form},
            )


class DraftDetailView(DetailView):
    model= Post
    template_name ="news_admin/draft_detail.html"
    context_object_name ="post"
    


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model =Post
    success_url = reverse_lazy("post-list")

    def form_valid(self,form):
        messages.success(self.request, "post was successfully deleted")
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    template_name = "news_admin/post_list.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(
        status="published", published_at__isnull=False
    ).order_by("-published_at")
    paginate_by = 1

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "news_admin/post_create.html"
    success_url = reverse_lazy("draft-list")

    def form_valid(self, form):
        form.instance.author = self.request.user  # logged in user
        return super().form_valid(form)

class PostPublishView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        post.status = "published"
        post.published_at = timezone.now()
        post.save()
        return redirect("home")
        

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model= Post
    form_class =PostForm
    template_name ="news_admin/post_create.html"
    success_url = reverse_lazy("post-list")

class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "news_admin/post_list.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(published_at__isnull=True)
    paginate_by = PAGINATE_BY
    

def handler404(request,exception, template_name="404.html"):
    return render(request, template_name, status=404)

class TagDetailView(DetailView):
    model = Tag
    template_name = "news_admin/tag_detail.html"
    context_object_name = "tags"


class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = "news_admin/tag_list.html"
    context_object_name = "tags"


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = TagForm
    template_name = "news_admin/tag_create.html"
    success_url = reverse_lazy("tag-list")


class TagDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=pk)
        tag.delete()
        return redirect("tag-list")


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "news_admin/tag_create.html"
    success_url = reverse_lazy("home")


class CategoryDetailView(DetailView):
    model = Category
    template_name = "news_admin/category_detail.html"
    context_object_name = "category"


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "news_admin/category_list.html"
    context_object_name = "category-detail"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CategoryForm
    template_name = "news_admin/category_create.html"
    success_url = reverse_lazy("category-list")


class CategoryDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect("category-list")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "news_admin/category_create.html"
    success_url = reverse_lazy("home")