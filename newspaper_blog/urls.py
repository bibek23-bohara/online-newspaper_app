
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
        views.post_create,
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
    


         


]
