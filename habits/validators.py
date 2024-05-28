from rest_framework.serializers import ValidationError


class ChooseRewardAssociatedHabit:

    def __init__(self, associated_habit, reward):
        self.field1 = associated_habit
        self.field2 = reward

    def __call__(self, value):
        associated_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if associated_habit and reward:
            raise ValidationError('Нельзя одновременно использовать связанную привычку и вознаграждение')


class LeadTimeHabit:

    def __init__(self, complete_time):
        self.field = complete_time

    def __call__(self, value):
        complete_time = dict(value).get(self.field)

        if complete_time and complete_time > 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд.')


class IncludeHabitWithSignPleasant:

    def __init__(self, associated_habit, sign_pl_habit):
        self.field1 = associated_habit
        self.field2 = sign_pl_habit

    def __call__(self, value):
        associated_habit = dict(value).get(self.field1)
        sign_pl_habit = dict(value).get(self.field2)

        if associated_habit and not sign_pl_habit:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки')


class AssociatedHabitValidator:

    def __init__(self, sign_pl_habit, associated_habit, reward):
        self.field1 = sign_pl_habit
        self.field2 = associated_habit
        self.field3 = reward

    def __call__(self, value):
        sign_pl_habit = dict(value).get(self.field1)
        associated_habit = dict(value).get(self.field2)
        reward = dict(value).get(self.field2)

        if sign_pl_habit and associated_habit and reward:
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class CheckPerformHabit:

    def __init__(self, periodicity):
        self.field = periodicity

    def __call__(self, value):
        periodicity = dict(value).get(self.field)

        if periodicity and periodicity > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
