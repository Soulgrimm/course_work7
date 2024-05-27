from habits.apps import HabitsConfig
from django.urls import path

from habits.views import HabitCreateView, HabitListView, HabitUpdateView, HabitDestroyView, \
    HabitAuthorListView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateView.as_view(), name='habit-create'),
    path('habit/list/', HabitListView.as_view(), name='habit-list'),
    path('habit/list/author/', HabitAuthorListView.as_view(), name='habit-author-list'),
    # path('habit/view/<int:pk>/', HabitRetrieveView.as_view(), name='habit-get'),
    path('habit/update/<int:pk>/', HabitUpdateView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyView.as_view(), name='habit-delete'),
]
