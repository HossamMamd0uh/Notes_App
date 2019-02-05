from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'notes_app'
urlpatterns = [
    path('' , views.all_notes , name='all_notes'),
    path('<slug:slug>/' , views.detail , name='note_detail'),
    path('<slug:slug>/' , views.step , name='step'),
    path('add_note' , views.note_add , name='add_note'),
    path('add_step/<note>/' , views.add_step , name='add_step'),
    path('steps_view' , views.all_steps , name='steps_view'),
    path('<slug:slug>/edit' , views.edit_note , name='note_edit'),
]
