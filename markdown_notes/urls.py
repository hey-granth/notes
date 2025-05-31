from django.urls import path
from .views import public_note_view, index_view, new, save_note


urlpatterns = [
    path('<str:username>/<int:pk>/', public_note_view, name='public_note_view'),
    path('index/', index_view, name='index'),
    path('new/', new, name='new'),
    path('save_note/', save_note, name='save_note'),
]
