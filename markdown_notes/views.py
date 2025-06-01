# Markdown Notes Views file

from django.shortcuts import render, get_object_or_404, redirect
from markdown import markdown
from .models import Note
from django.contrib.auth.decorators import login_required, login_not_required
from django.contrib.auth.models import User
from django.contrib import messages


@login_required(login_url="login")
def index_view(request):
    notes = request.user.notes.all().order_by("-created_at")
    return render(request, "notes/index.html", {"notes": notes})


@login_required(login_url="login")
def new(request):
    return render(request, "notes/new.html")


@login_required(login_url="login")
def save_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        is_public = "is_public" in request.POST

        if not content:
            messages.error(request, "Content is required.")
            return render(request, "notes/new.html")

        if title and content:
            note = Note.objects.create(
                title=title, content=content, user=request.user, is_public=is_public
            )
            messages.success(request, "Note saved successfully.")
            return redirect("index")

    messages.error(request, "Both title and content are required.")
    return render(
        request, "notes/new.html", {"error": "Title and content are required."}
    )


@login_required(login_url="login")
def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    html_content = markdown(note.content)
    return render(
        request, "notes/note.html", {"note": note, "html_content": html_content}
    )


@login_required(login_url="login")
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    messages.success(request, "Note deleted successfully.")
    return redirect("index")
