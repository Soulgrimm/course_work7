from datetime import datetime, timedelta

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_reminder_about_habit():
    time_now = datetime.now().time()
    date_now = datetime.now().today()
    send_to_habits = Habit.objects.filter(sign_pl_habit=False)

    for habit in send_to_habits:
        if habit.author.chat_id and not habit.next_date:
            if habit.time < time_now or habit.next_send_date <= date_now:
                text = f"Я буду {habit.action} в {habit.time} в {habit.place}"
                send_telegram_message(habit.is_author.tg_chat_id, text)
                habit.next_date = date_now + timedelta(days=habit.periodicity)
                habit.save()
