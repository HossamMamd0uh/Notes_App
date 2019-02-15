from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'notes_app'
urlpatterns = [
    path('' , views.all_notes , name='all_notes'),
    path('notes_list' , views.notes_list , name='notes_list'),
    path('story_list' , views.story_list , name='story_list'),
    path('about_list' , views.about_list , name='about_list'),
    path('news_list' , views.news_list , name='news_list'),
    path('<slug:slug>/' , views.detail , name='note_detail'),
    path('story/<slug:slug>/' , views.detail_story , name='detail_story'),
    path('news/<slug:slug>/' , views.detail_new , name='detail_new'),
    path('add_note' , views.note_add , name='add_note'),
    path('story_add' , views.story_add , name='story_add'),
    path('add_step/<note>/' , views.add_step , name='add_step'),
    path('<slug:slug>/edit' , views.edit_note , name='note_edit'),
]
