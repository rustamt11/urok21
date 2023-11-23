from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book-list'),
    path('add_book/', views.add_book, name='add-book'),
    path('books/<slug:slug>/', views.book_detail, name='book-detail'),
    path('books/<slug:slug>/update/', views.update_book, name='update-book'),
    path('books/<slug:slug>/delete/', views.delete_book, name='delete-book'),
]
