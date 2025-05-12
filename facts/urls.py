from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:category_slug>/', views.category_facts, name='category_facts'),
] 