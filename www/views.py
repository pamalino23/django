from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Wydzial, Kierunek, Student

from .forms import WydzialForm, KierunekForm, StudentForm

wydzialy = Wydzial.objects.all()
kierunki = Kierunek.objects.all()
studenci = Student.objects.all()


# Create your views here.
def index(request):
    
    return render(request, 'www/index.html', {
        'wydzialy': wydzialy,
        'kierunki': kierunki,
        'studenci': studenci,
        })

def bootstrap(request):
    
    return render(request, 'www/bootstrap.html', {
        'studenci': studenci
        })

def detail_wydzial(request, pk):
    wydzial = get_object_or_404(Wydzial, pk=pk)
    return render(request, 'www/detail-wydzial.html', {
        'wydzial': wydzial, 
        'pk':pk
        })

def detail_kierunek(request, pk):
    kierunek = get_object_or_404(Kierunek, pk=pk)
    return render(request, 'www/detail-kierunek.html', {
        'kierunek':kierunek, 
        'pk':pk
        })

def detail_student(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'www/detail-student.html', {
        'student': student, 
        'pk':pk
        })

def wydzialy_lista(request):
    return render(request, 'www/wydzialy.html', {
        'wydzialy': wydzialy
        })

def kierunki_lista(request):
    return render(request, 'www/kierunki.html', {
        'kierunki': kierunki
        })

def studenci_lista(request):
    return render(request, 'www/studenci.html', {
        'studenci': studenci
        })

def dodaj_wydzial(request):
    if request.method == 'POST':
        form = WydzialForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = WydzialForm()

    return render(request, 'www/dodaj-wydzial.html', {'form': form})
    

def dodaj_kierunek(request):
    if request.method == 'POST':
        form = KierunekForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = KierunekForm()

    return render(request, 'www/dodaj-kierunek.html', {'form': form})


def dodaj_studenta(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = StudentForm()

    return render(request, 'www/dodaj-studenta.html', {'form': form})


def zapisano(request):
    return render(request, 'www/zapisano.html')