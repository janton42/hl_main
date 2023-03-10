from django.urls import path

from .views import AppCreateView, ReleasesListView, ReleaseDetailView, ReleaseCreateView, NoteCreateView, \
    ConfirmCreateView, FeedbackCreateView

app_name = 'releases'
urlpatterns = [
    path('app/<int:app_pk>/releases', ReleasesListView.as_view(), name='index'),
    path('release/<int:pk>', ReleaseDetailView.as_view(), name='release_detail'),
    path('release/new', ReleaseCreateView.as_view(), name='release_create'),
    path('app/new', AppCreateView.as_view(), name='app_create'),
    path('release/<int:pk>/add_note', NoteCreateView.as_view(), name='note_create'),
    path('release/<int:pk>/confirm', ConfirmCreateView.as_view(), name='confirm_create'),
    path('feedback/submit', FeedbackCreateView.as_view(), name='submit_feedback'),
    path('app/feedback/confirm', ConfirmCreateView.as_view(), name='confirm_submit_feedback'),
    path('note/confirm', ConfirmCreateView.as_view(), name='confirm_note_create'),
    path('release/confirm', ConfirmCreateView.as_view(), name='confirm_release_create'),

]
