from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
# Create your views here.
from . models import Note , Steps
from . forms import NoteForm , StepsForm
from django.contrib.auth.models import User
from django.contrib import messages
def all_notes(request):
    all_notes = Note.objects.all()
    context = {
        'all_notes' : all_notes
    }
    return render(request , 'notes.html' , context)

def detail(request , slug):
    note = Note.objects.get(slug=slug)
    steps = Steps.objects.filter(step_assign__slug = slug)
    context = {
        'note' : note,
        'steps' : steps
    }
    return render(request , 'one_note.html' , context)

def note_add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST , request.FILES)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Note Created Successfully.')
            return redirect('/notes/add_step/' + str(new_form.pk) +'/')

    else:
        form = NoteForm()

    context = {
        'form' : form
    }
    return render(request , 'add.html' , context)

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

def edit_note(request , slug):
    note = get_object_or_404(Note , slug=slug)
    if request.method == 'POST':
        form = NoteForm(request.POST , request.FILES , instance = note )
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Note Updated Successfully.')
            return redirect('/notes')

    else:
        form = NoteForm(instance = note)

    context = {
        'form' : form
    }
    return render(request , 'create.html' , context)
