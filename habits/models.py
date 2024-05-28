from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель')
    place = models.CharField(max_length=100, verbose_name="место")
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=100, verbose_name="действие")
    sign_pl_habit = models.BooleanField(default=False, verbose_name="признак приятной привычки")
    associated_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, verbose_name="связанная привычка",
                                         **NULLABLE)
    periodicity = models.PositiveSmallIntegerField(default=1, verbose_name="периодичность")
    reward = models.CharField(max_length=100, verbose_name="вознаграждение", **NULLABLE)
    complete_time = models.DurationField(verbose_name="время на выполнение", **NULLABLE)
    sign_publication = models.BooleanField(default=False, verbose_name='признак публичности')
    next_send_date = models.DateField(verbose_name="дата следующей отправки", **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('pk',)
