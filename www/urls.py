from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wydzialy/', views.wydzialy_lista, name='wydzialy-lista'),
    path('kierunki/', views.kierunki_lista, name='kierunki-lista'),
    path('studenci/', views.studenci_lista, name='studenci-lista'),
    path('dodaj-wydzial/', views.dodaj_wydzial, name='dodaj-wydzial'),
    path('dodaj-kierunek/', views.dodaj_kierunek, name='dodaj-kierunek'),
    path('dodaj-studenta/', views.dodaj_studenta, name='dodaj-studenta'),
    path('zapisano/', views.zapisano, name='zapisano'),
    path('wydzial/<int:pk>/', views.detail_wydzial, name='detail-wydzial'),
    path('kierunek/<int:pk>/', views.detail_kierunek, name='detail-kierunek'),
    path('student/<int:pk>/', views.detail_student, name='detail-student'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
]