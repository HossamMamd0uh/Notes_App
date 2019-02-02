from django import forms
from .models import Note , Steps
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import gettext_lazy as _
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
                'title',
                'problem',
                'problem_solve',
                'difficulty',
                'prerequisites',
                'components',
                'the_end',
                'cost',
                'purchase_places',
                'tools_using',
                'tags',
                'code',
        ]
        labels = {
                'title' : _('العنوان'),
                'problem' : _('المشكلة'),
                'problem_solve' : _('حل المشكلة'),
                'difficulty' : _('الصعوبة'),
                'prerequisites' : _('الخبرة المسبقة'),
                'components' : _('المكونات'),
                'the_end' : _('النهاية'),
                'cost' : _('تكلفة المشروع'),
                'purchase_places' : _('اماكن شراء الادوات'),
                'tools_using' : _(' اماكن استخدام الادوات'),
                'tags' : _('الاشارات'),
                'code' : _('ملف الكود')
        }

class Steps(forms.ModelForm):
    class Meta:
        model = Steps
        fields = [
                'step_title',
                'step_photo',
                'step_photo_caption',
                'step_content',
        ]
        labels = {
                'step_title' : _('عنوان الخطوة'),
                'step_photo' : _('صورة الخطوة'),
                'step_photo_caption' : _('وصف الصورة'),
                'step_content' : _('الخطوة')
        }
