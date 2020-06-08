from django.urls import path

from .views import ForumsDetailView, ForumsListView, subject_details, create_subject
urlpatterns = [
    path('', ForumsListView.as_view(), name='forum'),
    path('<slug:slug>/', ForumsDetailView.as_view(), name='forums_detail'),
    path('subjects/<slug:slug>/', subject_details, name='subject_detail'),
    path('new_subject/<slug:slug>/', create_subject, name='create_subject'),
]