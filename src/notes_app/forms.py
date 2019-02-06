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
                'step_title',
                'step_photo',
                'step_photo_caption',
                'step_content',
                'code',
                'step_code',
                'step_code_link',
        ]
        labels = {
                'step_title' : _('عنوان الخطوة'),
                'step_photo' : _('صورة الخطوة'),
                'step_photo_caption' : _('وصف الصورة'),
                'step_content' : _('الخطوة'),
                'code' : _('ملف الخطوة'),
                'step_code' : _('الكود المستخدم'),
                'step_code_link' : _('لينك الكود')
        }
