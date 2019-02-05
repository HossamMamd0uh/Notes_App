from django import forms
from .models import Note , Steps
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import gettext_lazy as _
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
                'title',
                'about',
                'problem',
                'problem_solve',
                'how_problem_solve',
                'project_cost',
                'purchase_place',
                'tools_usage',
                'the_end',
                'tags',
        ]
        labels = {
                'title' : _('العنوان'),
                'about' : _('وصف المشروع'),
                'problem' : _('المشكلة'),
                'problem_solve' : _('حل المشكلة'),
                'how_problem_solve' : _('كيف قمت بحل المشكلة'),
                'project_cost' : _('تكلفة المشروع'),
                'purchase_place' : _('اماكن شراء الادوات'),
                'tools_usage' : _('اماكن استخدام الادوات'),
                'the_end' : _('النهاية'),
                'tags' : _('الاشارات')
        }

class StepsForm(forms.ModelForm):
    class Meta:
        model = Steps
        fields = [
                'step_title',
                'step_photo',
                'step_photo_caption',
                'step_content',
                'code',
        ]
        labels = {
                'step_title' : _('عنوان الخطوة'),
                'step_photo' : _('صورة الخطوة'),
                'step_photo_caption' : _('وصف الصورة'),
                'step_content' : _('الخطوة'),
                'code' : _('ملف الخطوة')
        }
