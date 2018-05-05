from django.db import models
import datetime
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=250)
    picture = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    about = models.CharField(max_length=500)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class File(models.Model):
    name = models.CharField(max_length=200)
    file_name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    time = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name


class Comment(models.Model):
    data = models.CharField(max_length=500)
    time = models.CharField(max_length=200, default=datetime.datetime.now())
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.data


class Topic(models.Model):
    title = models.CharField(max_length=200)
    file_id = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
