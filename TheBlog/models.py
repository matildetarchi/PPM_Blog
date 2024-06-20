from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/profile/')

    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255, default="Blog")
    category = models.CharField(max_length=255, default="Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default="No description")
    body = RichTextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article', args=(str(self.id)))


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)