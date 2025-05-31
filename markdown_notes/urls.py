from django.urls import path
from .views import index_view, new, save_note, view_note

urlpatterns = [
    # path('<str:username>/<int:pk>/', public_note_view, name='public_note_view'),
    path('index/', index_view, name='index'),
    path('new/', new, name='new'),
    path('save_note/', save_note, name='save_note'),
    path('note/<int:note_id>/', view_note, name='view_note')
]
