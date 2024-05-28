from rest_framework import serializers

from habits.models import Habit
from habits.validators import ChooseRewardAssociatedHabit, LeadTimeHabit, IncludeHabitWithSignPleasant, \
    AssociatedHabitValidator, CheckPerformHabit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            ChooseRewardAssociatedHabit(associated_habit='associated_habit', reward='reward'),
            LeadTimeHabit(complete_time='complete_time'),
            IncludeHabitWithSignPleasant(associated_habit='associated_habit', sign_pl_habit='sign_pl_habit'),
            AssociatedHabitValidator(sign_pl_habit='sign_pl_habit', associated_habit='associated_habit', reward='reward'),
            CheckPerformHabit(periodicity='periodicity')
        ]
