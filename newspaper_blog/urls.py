
from django.urls import path
from newspaper_blog import views
urlpatterns = [
    path(
    "",
    views.Homeview.as_view(),
    name="home",
        ),
    path(
    "post-detail/<int:pk>/",
    views.PostDetailView.as_view(),
    name="post-detail",
        ),
     path(
    "post-catgtegory",
    views.PostCategoryView.as_view(),
    name="post-category",
        ),
    path(
    "post-by-category/<int:cat_id>/",
    views.PostByCategoryView.as_view(),
    name="post-by-category",
    ),
    path(
    "post-by-tag/<int:tag_id>/",
    views.PostByTagView.as_view(),
    name="post-by-tag",
    ),
    path(
    "about/",
    views.AboutView.as_view(),
    name="about",
    ),
    path(
    "contact/",
    views.ContactView.as_view(),
    name="contact",
    ),
    path(
    "comment/",
    views.CommentView.as_view(),
    name="comment",
    ),
    path("post-delete/<int:pk>/",
         views.PostDeleteView.as_view(),
         name="post-delete"),
        
     path("post-update/<int:pk>/",
        views.PostUpdateView.as_view(),
        name="post-update"
        ),
    path(
        "post-create/",
        views.PostCreateView.as_view(),
        name="post-create"
    ),
    path(
        "draft-list/",
        views.DraftListView.as_view(),
        name="draft-list",
    ),
    path("post-publish/<int:pk>/",
         views.PostPublishView.as_view(),
         name="post-publish"
    ),
    path("draft-detail/<int:pk>/",
         views.DraftDetailView.as_view(),
         name="draft-detail"
    ),
      path(
        "tag-detail/<int:pk>/",
        views.TagDetailView.as_view(),
        name="tag-detail",
    ),
    path(
        "tags/",
        views.TagListView.as_view(),
        name="tag-list",
    ),
    path(
        "tag-create/",
        views.TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tag-delete/<int:pk>/",
        views.TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path(
        "tag-update/<int:pk>/",
        views.TagUpdateView.as_view(),
        name="tag-update",
    ),
     path(
        "category-detail/<int:pk>/",
        views.CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path(
        "categories/",
        views.CategoryListView.as_view(),
        name="category-list",
    ),
    path(
        "category-create/",
        views.CategoryCreateView.as_view(),
        name="category-create",
    ),
    path(
        "category-delete/<int:pk>/",
        views.CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path(
        "category-update/<int:pk>/",
        views.CategoryUpdateView.as_view(),
        name="category-update",
    ),


         


]
