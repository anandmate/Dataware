from django.db import models

# Create your models here.


class Php(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    class Meta:
        db_table = 'php'


    def __str__(self):
        return self.question


class Html(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    class Meta:
        db_table = 'html'


class Css(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    class Meta:
        db_table = 'css'


class Wordpress(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    class Meta:
        db_table = 'wordpress'


class Bootstrap(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    class Meta:
        db_table = 'bootstrap'


class Rtool(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    class Meta:
        db_table = 'Rtool'


class Python(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    class Meta:
        db_table = 'python'


class Stat(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    class Meta:
        db_table = 'stat'


class Machine(models.Model):
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    class Meta:
        db_table = 'machine'

