from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsAuthor
from habits.serializers import HabitSerializer


class HabitCreateView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.is_author = self.request.user
        new_habit.save()


class HabitListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator


class HabitAuthorListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        return Habit.objects.filter(is_author=self.request.user)


# class HabitRetrieveView(generics.RetrieveAPIView):
#     serializer_class = HabitSerializer
#     queryset = Habit.objects.all()
#     permission_classes = [IsAuthenticated]


class HabitUpdateView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]


class HabitDestroyView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]
