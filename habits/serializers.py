from rest_framework import serializers

from habits.models import Habit
from habits.validators import ChooseRewardAssociatedHabit, LeadTimeHabit, IncludeHabitWithSignPleasant, \
    AssociatedHabitValidator, CheckPerformHabit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            ChooseRewardAssociatedHabit(field_1='associated_habit', field_2='reward'),
            LeadTimeHabit(field='complete_time'),
            IncludeHabitWithSignPleasant(field_1='associated_habit', field_2='sign_pl_habit'),
            AssociatedHabitValidator(field_1='sign_pl_habit', field_2='associated_habit', field_3='reward'),
            CheckPerformHabit(field='periodicity')
        ]
