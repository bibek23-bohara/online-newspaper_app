
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
    "post-search/",
    views.PostSearchView.as_view(),
    name="post-search",
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


]
