from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=40,unique=True)
    def __self__(self):
        return Category
class Post(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reated_at = models.DateTimeField(
        auto_now_add=True)
    def __self__(self):
        return Post
class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __self__(self):
        return Comment