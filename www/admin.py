from django.contrib import admin
from .models import Student, Wydzial, Kierunek

# Register your models here.
admin.site.register(Student)
admin.site.register(Wydzial)
admin.site.register(Kierunek)