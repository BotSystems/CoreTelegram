from handlers.decorators import save_chanel_decorator
from handlers.keyboard import build_keyboard


@save_chanel_decorator
def send_welcome(bot, update, *args, **kwargs):
    message = "Твой первый шаг в мир кэшбэка начинается здесь. Отправь мне название магазина и я подскажу тебе информацию об актуальной ставке кэшбэка."
    bot.sendMessage(chat_id=update.message.chat_id, text=message, reply_markup=build_keyboard())
