from django.db import models

# Create your models here.

class Person(models.Model):
    email = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.person_text


class Test(models.Model):
    test_name = models.CharField(max_length=300)

    def __str__(self):
        return self.test_name

class Person_Test(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.PROTECT) #should i put on_delete here?
    #test_date = model.DateTimeField() #is this what i should put here
    #test_score =
    #test_interpretation =

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, null=True)


    class DASS21(models.IntegerChoices):
        Never = 0
        Sometimes = 1
        Often = 2
        Almost_always = 3

    dass21 = models.IntegerField(choices=DASS21.choices, null=True)
    def __str__(self):
        return self.dass21

    class DERS(models.IntegerChoices):
        Almost_never = 1
        Sometimes = 2
        About_half_the_time = 3
        Most_of_the_time = 4
        Almost_always = 5

    ders = models.IntegerField(choices=DERS.choices, null=True)

    def __str__(self):
        return self.ders
