from django.db import models

class TimeStampModel(models.Model):
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class  Meta:
        abstract = True
        

class Category(TimeStampModel):
    name = models.CharField(max_length=20)

    def __str__(self) :
        return self.name


class Tag(TimeStampModel):
    name = models.CharField(max_length=20)
    def __str__(self) :
        return self.name


class Post(TimeStampModel):
    STATUS_CHOICES =[
        ("active", "Active"),
        ("in_active","Inactive"),
    ]
    title =models.CharField(max_length=250)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    published_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    views_count=models.PositiveBigIntegerField(default=0)
    def __str__(self) :
        return self.title
    


    @property
    def latest_comments(self):
        comments = Comment.objects.filter(post=self).order_by("-created_at")
        return comments


class Contact(TimeStampModel):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
class Comment(TimeStampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.comment[:50]