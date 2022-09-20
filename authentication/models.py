# from django.db import models
#
# # Create your models here.
#
# from django.db import models
from django.contrib.auth import get_user_model
# import uuid
# from datetime import datetime
#
User = get_user_model()
#
# # Create your models here.
# # class Profile(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     id_user = models.IntegerField()
# #     bio = models.TextField(blank=True)
# #     profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
# #     location = models.CharField(max_length=100, blank=True)
# #
# #     def __str__(self):
# #         return self.user.username
#
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='post_images')
#     created_at = models.DateTimeField(default=datetime.now)
#     no_of_likes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title
#
# class LikePost(models.Model):
#     post_id = models.CharField(max_length=500)
#     username = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.username
#
# class FollowersCount(models.Model):
#     follower = models.CharField(max_length=100)
#     user = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.user
from django.db import models


class UploadImage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    hot = models.ManyToManyField(User, related_name='forhot')
    n_not = models.ManyToManyField(User, related_name='fornot')
    follower = models.ManyToManyField(User,related_name='follower')
    unfollower = models.ManyToManyField(User, related_name='unfollower')

