from datetime import timedelta

from rest_framework.serializers import ValidationError


class ChooseRewardAssociatedHabit:

    def __init__(self, field_1, field_2):
        self.field1 = field_1
        self.field2 = field_2

    def __call__(self, value):
        associated_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if associated_habit and reward:
            raise ValidationError('Нельзя одновременно использовать связанную привычку и вознаграждение')


class LeadTimeHabit:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        complete_time = dict(value).get(self.field)

        if complete_time and complete_time > 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд.')


class IncludeHabitWithSignPleasant:

    def __init__(self, field_1, field_2):
        self.field1 = field_1
        self.field2 = field_2

    def __call__(self, value):
        associated_habit = dict(value).get(self.field1)
        sign_pl_habit = dict(value).get(self.field2)

        if associated_habit and not sign_pl_habit:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки')


class AssociatedHabitValidator:

    def __init__(self, field_1, field_2, field_3):
        self.field1 = field_1
        self.field2 = field_2
        self.field3 = field_3

    def __call__(self, value):
        sign_pl_habit = dict(value).get(self.field1)
        associated_habit = dict(value).get(self.field2)
        reward = dict(value).get(self.field2)

        if sign_pl_habit and associated_habit and reward:
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class CheckPerformHabit:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get(self.field)

        if periodicity and periodicity > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
