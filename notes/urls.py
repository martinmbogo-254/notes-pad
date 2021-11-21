from django.urls import path
from . import views
from .views import home,NoteDetail, NoteCreate, NoteDeleteView, NoteUpdateView

urlpatterns = [
    path('', views.home, name='home'),
    path('note/<str:pk>/', views.NoteDetail, name='detail'),
    path('note/new_note', views.NoteCreate, name='new_note'),

    # path('note/new_note', NoteCreateView.as_view(),name = 'new_note'),
    path('note/<int:pk>/update', NoteUpdateView.as_view(), name='update'),
    path('note/<int:pk>/delete', NoteDeleteView.as_view(), name='delete'),

]
