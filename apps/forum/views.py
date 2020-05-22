from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Comments, Forum, Section, Subject


class ForumsListView(ListView):
    model = Section
    template_name = 'forum/forum.html'

class ForumsDetailView(DetailView):
    model = Forum
    template_name = 'forum/forums.html'

def subject_details(request, slug):
    subject = Subject.objects.get(slug=slug)
    answers_list = subject.comments_set.all()
    paginator = Paginator(answers_list, 1)
    page = request.GET.get('page', 1)
    answers = paginator.get_page(page)
    context = {
        'subject': subject,
        'answers': answers
    }
    return render(request, 'forum/subject.html', context)