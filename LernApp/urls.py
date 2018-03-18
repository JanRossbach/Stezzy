from django.urls import path
from LernApp.views import (IndexView, LernKarteCreate, LernKarteDetail,
                           LernKarteUpdate, LernKarteDelete, ProjectListView,
                           ProjectCreateView, LernKartenListView, ProjectUpdate,
                           ProjectDelete, AboutView)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<pk>/lernkarten/', LernKartenListView.as_view(), name='lernkarten'),
    path('projects/new/', ProjectCreateView.as_view(), name='new_project'),
    path('lernkarte/new/', LernKarteCreate.as_view(), name='create'),
    path('lernkarte/<pk>/', LernKarteDetail.as_view(), name='lernkarte_detail'),
    path('lernkarte/<pk>/edit/', LernKarteUpdate.as_view(), name='update'),
    path('lernkarte/<pk>/delete/', LernKarteDelete.as_view(), name='delete'),
    path('projects/<pk>/edit/', ProjectUpdate.as_view(), name='project_update'),
    path('projects/<pk>/delete/', ProjectDelete.as_view(), name='project_delete'),
]
