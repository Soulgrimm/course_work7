import requests
from config import settings
import logging

logger = logging.getLogger(__name__)


def send_telegram_message(chat_id, message):
    url = f'{settings.URL_TELEGRAM}{settings.API_TELEGRAM_TOKEN}/sendMessage'
    params = {
        'text': message,
        'chat_id': chat_id
    }
    response = requests.get(url, params=params)
    if not response.ok:
        logger.warning('Сообщение не отправлено, chat_id= %s', chat_id)
