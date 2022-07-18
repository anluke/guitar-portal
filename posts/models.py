from tinymce import HTMLField
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

# post view for when user is authenticated
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# post view for non-authenticated users
class AnonPostView(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title


## AUTHOR ##
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username


## CATEGORY ##
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


## COMMENT ##
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



## POST ##
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    comment_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = CloudinaryField('image', default='placeholder')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })
        
    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'pk': self.pk
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()


    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count() + AnonPostView.objects.filter(post=self).count()


