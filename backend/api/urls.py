from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    # path('filter', TaskFilterOrSearch.as_view()),
    path('task-list/', taskList, name='task-list'),
    path('task-detail/<str:slug>/', taskDetail, name='task-detail'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-update/<str:slug>/', taskUpdate, name='task-update'),
    path('task-delete/<str:slug>/', taskDelete, name='task-delete'),
]
