from .views import book_list, book_create, book_update, book_delete
from django.urls import path

app_name = 'book'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('create/book/', book_create, name='book_create'),
    path('update/book/<int:pk>/', book_update, name='book_update'),
    path('delete/book/<int:pk>/', book_delete, name='book_delete'),
]
