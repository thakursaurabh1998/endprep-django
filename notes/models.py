from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


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


class File(models.Model):
    name = models.CharField(max_length=200)
    file_name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    time = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
