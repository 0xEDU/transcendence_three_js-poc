from django.contrib import admin
from django.urls import path
from .views import views

urlpatterns = [
    path('/', views.three_js_view, name='three_js_view'),
]
