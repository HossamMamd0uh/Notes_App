from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import login , authenticate
from .models import Profile
from django.shortcuts import get_object_or_404
from .forms import UserForm , ProfileForm
from . models import Profile
from django.contrib import messages
from notes_app.models import Note
from notes_app.views import detail
from django.contrib.auth import get_user_model
# Create your views here.
def all_accounts(request):
    all_accounts = Profile.objects.all()
    context = {
        'all_accounts' : all_accounts
    }
    return render(request , 'accounts.html' , context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username , password=password)
            login(request , user)
            messages.success(request, 'Welcome On Board!')
            return redirect('/notes')
    else:
        form = UserCreationForm

    context = {
        'form' : form ,
    }

    return render(request , 'signup.html' , context)


def profile(request , slug):
    profile = get_object_or_404(Profile , slug=slug)
    blogs = Note.objects.filter(slug=slug).values_list('id', flat=True)
    context = {
        'profile' : profile,
        'blogs' : blogs,
    }
    return render(request , 'profile.html' , context)


def edit_profile(request , slug):
    profile = get_object_or_404(Profile , slug=slug)
    if request.method == 'POST':
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST , request.FILES ,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            new_profile=profile_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            messages.success(request, 'Your Profile Updated Successfully.')
            return redirect('/notes')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form' : user_form ,
        'profile_form' : profile_form
    }

    return render(request , 'edit_profile.html' , context)



def change_password(request , slug):
    profile = get_object_or_404(Profile , slug=slug)

    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user , request.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect('/notes')

    else:
        password_form = PasswordChangeForm(request.user)

    context = {
        'password_form' : password_form
    }

    return render(request , 'change_password.html' , context)
