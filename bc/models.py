from enum import property
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=25)
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    registrate_date = models.DateField(auto_now=True)

    def calculated_balance(self) -> float:
        result = 0

        notes = Note.objects.filter(user=self)

        for note in notes:
            if note.category == 1:
                result -= note.price
            else:
                result += note.price
        return result



    def __str__(self):
        return self.f_name + ' ' + self.l_name


class Note(models.Model):
    category = [
        (1, 'Росход'),
        (2, 'Доход'),
    ]
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    category = models.IntegerField(choices=category)
    reason = models.CharField(max_length=75)
    price = models.IntegerField()
    date_time = models.DateTimeField(auto_now=True)


