from django.db import models


# Create your models here.


class Category(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Project(models.Model):
    # id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    project_aim = models.TextField()
    desription = models.TextField()
    file = models.FileField()
    innovastion_part = models.TextField()
    location = models.TextField()

    def __str__(self):
        return self.name
