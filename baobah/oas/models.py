from django.db import models
class Oas(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default='Anônimo')
    email = models.EmailField(blank = True)
    describe = models.TextField(default = 'Descrição')
    tempo = models.IntegerField()
    language = models.CharField(max_length = 30)
    link = models.CharField(max_length = 50)
    connectivity = models.BooleanField(default = True)

    def __str__(self):
        return self.name