from django import forms
from .models import Note , Steps , Story , About , News
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import gettext_lazy as _
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
                'title',
                'about',
                'about_photo',
                'vid',
                'comp',
                'comp_photo',
                'tools',
                'tools_photo',
                'project_cost',
                'purchase_place',
                'tools_usage',
                'the_end',
                'fin_photo',
                'fin_vid',
                'poject_code',
                'tags',
        ]
        labels = {
                'title' : _('العنوان'),
                'about' : _('مقدمة المشروع'),
                'about_photo' : _('اضف صورة'),
                'vid' : _('ارفع فيديو'),
                'comp' : _('المكونات'),
                'comp_photo' : _('صورة المكونات'),
                'tools' : _('الادوات'),
                'tools_photo' : _('صورة الادوات'),
                'project_cost' : _('التكلفة الشاملة للمشروع'),
                'purchase_place' : _('اماكن شراء الادوات والمكونات'),
                'tools_usage' : _('اماكن استخدام المكن'),
                'the_end' : _('التصميم'),
                'fin_photo' : _('ارفع صورة'),
                'fin_vid' : _('لينك الفيديو'),
                'poject_code' : _('ارفع ملف'),
                'tags' : _('الاشارات'),
        }

class StepsForm(forms.ModelForm):
    class Meta:
        model = Steps
        fields = [
                'title',
                'step_photo',
                'step_photo_caption',
                'step_content',
                'code',
                'step_code',
                'step_code_link',
        ]
        labels = {
                'title' : _('عنوان الخطوة'),
                'step_photo' : _('صورة الخطوة'),
                'step_photo_caption' : _('وصف الصورة'),
                'step_content' : _('الخطوة'),
                'code' : _('ملف الخطوة'),
                'step_code' : _('الكود المستخدم'),
                'step_code_link' : _('لينك الكود')
        }

class StoryForm(forms.ModelForm):
    story_content = forms.CharField(widget=CKEditorWidget(), label='المقال')
    class Meta:
        model = Story
        fields = [
            'title',
            'story_photo_caption',
            'story_photo',
            'story_content'
        ]
        labels = {
            'title' : _('العنوان'),
            'story_photo_caption' : _('وصف الصورة'),
            'story_photo' : _('الصورة')
        }

class AboutForm(forms.ModelForm):
    about_content = forms.CharField(widget=CKEditorWidget(), label='احنا مين')
    class Meta:
        modle = About
        fields = [
            'title',
            'about_photo',
            'about_content'
        ]
        labels = {
            'title' : _('العنوان'),
            'about_content' : _('احنا مين'),
            'story_photo' : _('الصورة')
        }

class NewsForm(forms.ModelForm):
    news_content = forms.CharField(widget=CKEditorWidget(), label='احنا مين')
    class Meta:
        modle = News
        fields = [
            'title',
            'news_photo',
            'news_content'
        ]
        labels = {
            'title' : _('العنوان'),
            'news_content' : _('ايه الجديد'),
            'news_photo' : _('الصورة')
        }
