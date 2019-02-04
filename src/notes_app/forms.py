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
        ]
        labels = {
                'title' : _('العنوان'),
                'about' : _('وصف المشروع'),
        }

class Steps(forms.ModelForm):
    class Meta:
        model = Steps
        fields = [
                'step_assign',
                'step_title',
                'step_photo',
                'step_photo_caption',
                'step_content',
                'code',
        ]
        labels = {
                'step_assign' : _('ربط الخطوة'),
                'step_title' : _('عنوان الخطوة'),
                'step_photo' : _('صورة الخطوة'),
                'step_photo_caption' : _('وصف الصورة'),
                'step_content' : _('الخطوة'),
                'code' : _('ملف الخطوة')
        }
