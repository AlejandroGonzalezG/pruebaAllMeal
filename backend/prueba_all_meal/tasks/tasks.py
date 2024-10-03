from celery.schedules import crontab
from celery import shared_task
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from meals.models import Menu, WeekDays
from django.utils import timezone

@shared_task
def sending_menu():
    client = WebClient(token="YOUR_SLACK_BOT_TOKEN")

    current_day = timezone.now().weekday()
    current_weekday = WeekDays(current_day)
    
    menus = Menu.objects.filter(day_of_week=current_weekday)

    message = ''
    message_parts = []

    if menus.exists():
        for menu in menus.all():
            message_parts.append(f"{menu.entree} - {menu.main_dish} - {menu.dessert}")
        message = f'Saludos YOUR_CHANNEL_NAME, este día tenemos los siguientes menus disponible:\n{"".join(message_parts)}\n.Esperamos sus respuesta!'
    else:
        message = "No hay menús disponibles hoy."
    try:
        response = client.chat_postMessage(
            channel="YOUR_CHANNEL_NAME",
            text=message
        )
        print(f"Message sent successfully: {response}")
    except SlackApiError as e:
        print(f"Error sending message: {e}")

# beat_schedule = {
#     'sending_menu': {
#         'task': 'sending_menu',
#         'schedule': crontab(minute='*/1'),
#     },
# }