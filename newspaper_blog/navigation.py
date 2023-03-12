from django.db.models import F, Sum


from newspaper_blog.models import Category,Tag,Post

def navigation(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()[:7]
    top_categories = (
        Post.objects.values("category__pk", "category__name")
        .annotate(
            pk=F("category__pk"), name=F("category__name"),max_views=Sum("views_count")
        )
        .order_by("-max_views")
        .values("pk","name","max_views")
    )
    return{
        "categories":categories,
        "tags":tags,
        "top_categories":top_categories,
    }