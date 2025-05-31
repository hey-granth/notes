# Markdown Notes Views file

from django.shortcuts import render, get_object_or_404, redirect
from markdown import markdown
from .models import Note
from django.contrib.auth.decorators import login_required, login_not_required
from django.contrib.auth.models import User
from django.contrib import messages


@login_not_required
def public_note_view(request, username, pk):
    user = get_object_or_404(User, username=username)
    note = get_object_or_404(Note, user=user, pk=pk, is_public=True)
    html_content = markdown(note.content)
    return render(request, 'notes/note.html', {'note': note, 'html_content': html_content})


@login_required(login_url='login')
def index_view(request):
    return render(request, 'notes/index.html')


@login_required(login_url='login')
def new(request):
    return render(request, 'notes/new.html')


# @login_required(login_url='login')
# def save_note(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         is_public = 'is_public' in request.POST
#
#         if title and content:
#             note = Note.objects.create(
#                 title=title,
#                 content=content,
#                 user=request.user,
#                 is_public=is_public
#             )
#             messages.success(request, 'Note saved successfully.')
#             return redirect('note', username=request.user.username, pk=note.pk)
#
#     messages.error(request, 'Both title and content are required.')
#     return render(request, 'notes/new.html', {'error': 'Title and content are required.'})


@login_required(login_url='login')
def save_note(request):
    print(f"save_note view called, method: {request.method}")

    if request.method == 'POST':
        print("POST request received")
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_public = 'is_public' in request.POST

        print(f"Title: '{title}'")
        print(f"Content: '{content[:50]}...' (first 50 chars)")
        print(f"Is public: {is_public}")

        if title and content:
            try:
                note = Note.objects.create(
                    title=title,
                    content=content,
                    user=request.user,
                    is_public=is_public
                )
                print(f"Note created successfully with ID: {note.pk}")
                messages.success(request, 'Note saved successfully.')

                # Simple redirect to index for now
                return redirect('index')

            except Exception as e:
                print(f"Error creating note: {e}")
                messages.error(request, f'Error saving note: {e}')
                return render(request, 'notes/new.html')
        else:
            print("Title or content is missing")

    print("Rendering new.html")
    return render(request, 'notes/new.html')

