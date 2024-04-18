from django.db import models

# Create your models here.

class Wydzial(models.Model):
    nazwa = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images')
    utworzono = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Wydział'
        verbose_name_plural = 'Wydziały'

    def __str__(self):
        return self.nazwa
    
class Kierunek(models.Model):
    nazwa = models.CharField(max_length=250)
    #wydzial = models.ForeignKey(Wydzial, on_delete=models.CASCADE)    w przypadku gdy związek jest typu jeden do wielu
    wydzialy = models.ManyToManyField(Wydzial)
    utworzono = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Kierunki'

    def __str__(self):
        return self.nazwa

class Student(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    nr_albumu = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    kierunki = models.ManyToManyField(Kierunek)
    zdjecie = models.ImageField(upload_to='images')
    utworzono = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Studenci'

    def __str__(self):
        return self.nazwisko + " " + self.imie
    
