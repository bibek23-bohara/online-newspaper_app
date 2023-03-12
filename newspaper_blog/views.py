from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView, View
from newspaper_blog.models import Post, Category, Tag
from django.utils import timezone
from django.db.models import Q
from datetime import timedelta
from newspaper_blog.forms import ContactForm, CommentForm
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
        context["politics_left_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[4:5]
        context["politics_left_down_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[3:5]
        context["politics_left_up_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[6:7]
        context["politics_right_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[:5]
        context["bussiness_right_categories"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[4:5]
        context["bussiness_left_up_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-created_at")[4:5]
        context["bussiness_left_down_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("category")[4:5]
        context["bussiness_right_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-tag")[4:5]
        context["bussiness_left_categories"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[2:7]
        context["politics_left_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[6:7]
        context["politics_left_down_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[6:7]
        context["politics_left_up_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[5:6]
        context["politics_left_middle_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[4:6]
        context["politics_right_left_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[1:3]
        context["politics_right_posts"]=Post.objects.filter(status="active", published_at__isnull=False).order_by("-views_count")[2:7]
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
    
class PostSearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("query")
        post_list = Post.objects.filter(
            (Q(status = "active")& Q(published_at__isnull= False))
        &(Q(title_icontains=query) |Q(content_icontains = query)),
        )
        return render(
            request,
            "zennews/header/header.hmtl",
            {"page_obj":post_list, "query":query},
        )
    



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

