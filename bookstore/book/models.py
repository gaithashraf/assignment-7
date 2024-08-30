from django.db import models

# Create your models here.
class Book(models.Model):
    category_choices = (("Computer", "Computer"), ("Engineering", "Engineering"), ("Food", "Food"), ("Art", "Art"))
    RATES = (("*", "*"), ("**", "**"), ("***", "***"), ("****", "****"), ("*****", "*****"))
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    category = models.CharField(choices=category_choices, max_length= 100)
    description= models.CharField(max_length=700)
    rating = models.CharField(choices=RATES, null=False, max_length= 100)

    def __str__(self):
        return self.name

