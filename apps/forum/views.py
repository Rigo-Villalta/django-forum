from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .forms import NewSubjectForm
from .models import Comments, Forum, Section, Subject


class ForumsListView(ListView):
    model = Section
    template_name = "forum/forum.html"


class ForumsDetailView(DetailView):
    model = Forum
    template_name = "forum/forums.html"


def subject_details(request, slug):
    subject = Subject.objects.get(slug=slug)
    answers_list = subject.comments_set.all()
    paginator = Paginator(answers_list, 1)
    page = request.GET.get("page", 1)
    answers = paginator.get_page(page)
    context = {"subject": subject, "answers": answers}
    return render(request, "forum/subject.html", context)


def create_subject(request, slug):
    forum = Forum.objects.get(slug=slug)
    if request.method == "POST":
        form = NewSubjectForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            current_user = request.user
            new_subject = Subject(
                author=current_user, title=form.cleaned_data["title"], text=form.cleaned_data["text"], forum=forum
            )
            new_subject.save()
            actual_slug = new_subject.slug
            return HttpResponseRedirect(reverse('subject_detail', kwargs={'slug': actual_slug,}))
    else:
        form = NewSubjectForm
    context = {
        "forum": forum,
        "form": form,
    }
    return render(request, "forum/new_subject.html", context)

