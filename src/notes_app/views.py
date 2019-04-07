from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.forms import modelformset_factory
# Create your views here.
from . models import Note , Steps , Story , About , News , Images
from . forms import NoteForm , StepsForm , StoryForm , AboutForm , ImageForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def all_notes(request):
    all_notes = Note.objects.all()
    all_story = Story.objects.all()
    context = {
        'all_notes' : all_notes,
        'all_story' : all_story
    }
    return render(request , 'notes.html' , context)

def notes_list(request):
    notes_list = Note.objects.all()
    context = {
        'notes_list' : notes_list
    }
    return render(request , 'all_notes.html' , context)

def story_list(request):
    story_list = Story.objects.all()
    context = {
        'story_list' : story_list
    }
    return render (request , 'story_list.html' , context)

def about_list(request):
    about_list = About.objects.all()
    context = {
        'about_list' : about_list
    }
    return render (request , 'about_list.html' , context)

def news_list(request):
    news_list = News.objects.all()
    context = {
        'news_list' : news_list
    }
    return render (request , 'news_list.html' , context)

def detail_new(request , slug):
    new = News.objects.get(slug=slug)
    context = {
        'new' : new,
    }
    return render(request , 'one_new.html' , context)


def detail(request , slug):
    note = Note.objects.get(slug=slug)
    steps = Steps.objects.filter(step_assign__slug = slug)
    context = {
        'note' : note,
        'steps' : steps
    }
    return render(request , 'one_note.html' , context)

def detail_story(request , slug):
    story = Story.objects.get(slug=slug)
    context = {
        'story' : story,
    }
    return render(request , 'one_story.html' , context)

@login_required
def note_add(request):
    ImageFormSet = modelformset_factory(Images,form=ImageForm, extra=3)
    if request.method == 'POST':
        form = NoteForm(request.POST , request.FILES)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if form.is_valid() and formset.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(post=form, image=image)
                    photo.save()
            messages.success(request, 'Note Created Successfully.')
            return redirect('/notes/add_step/' + str(new_form.pk) +'/')

    else:
        form = NoteForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    context = {
        'form' : form,
        'formset' : formset
    }
    return render(request , 'add.html' , context)

@login_required
def add_step(request,note):
    if request.method == 'POST':
        steps = StepsForm(request.POST , request.FILES)

        if steps.is_valid():
            new_form = steps.save(commit=False)
            new_form.step_assign = Note.objects.get(pk=note)
            #new_form.step_title = "rwgrg"
            new_form.save()
            messages.success(request, 'step added')
            return redirect('/notes/add_step/' + note + '/' )
    else:
        steps = StepsForm()

    context = {
        'steps' : steps
    }
    return render(request , 'steps.html' , context)

@login_required
def edit_note(request , slug):
    if request.user.has_perm('Note.change_note'):
        note = get_object_or_404(Note , slug=slug)
        if request.method == 'POST':
            form = NoteForm(request.POST , request.FILES , instance = note )
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.save()
                messages.success(request, 'Note Updated Successfully.')
                return redirect('/notes')

        else:
            form = NoteForm(instance = note)

        context = {
            'form' : form
        }
        return render(request , 'create.html' , context)
    else:
        messages.error(request, 'You Are Not Allowed.')
        return redirect('/notes')

@login_required
def story_add(request):
    if request.method == 'POST':
        form = StoryForm(request.POST , request.FILES)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Story Created Successfully.')
            return redirect('/notes')

    else:
        form = StoryForm()

    context = {
        'form' : form
    }
    return render(request , 'add_story.html' , context)
