import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Инициализация User-бота с вашими API ID и API HASH
API_ID = "яяяяяяяя"  # Ваш API ID
API_HASH = "нннннннннннннннннннннн"  # Ваш API HASH
PHONE_NUMBER = "+7хххххххххх"  # Ваш номер телефона в формате международного кода
app = Client("my_user_bot", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)

# Хранилище для статистики
user_stats = []

@app.on_message(filters.text & ~filters.command("statistics"))
async def count_messages(client: Client, message: Message):
    # Получаем информацию о пользователе
    user_info = message.from_user
    if user_info.username:
        user_identifier = user_info.username
    else:
        user_id = user_info.id
        first_name = user_info.first_name or ""
        user_identifier = f"{user_id} {first_name}"

    message_time = message.date.strftime("%Y-%m-%d %H:%M:%S")
    message_content = message.text

    # Добавляем информацию о сообщении в список
    user_stats.append(f"{user_identifier}   {message_time}   {message_content}\n\n")

@app.on_message(filters.command("statistics"))
async def statistics(client: Client, message: Message):
    if not user_stats:
        await message.reply_text("У вас нет сообщений для статистики.")
        return

    txt_file = "statistics.txt"

    # Записываем статистику в текстовый файл
    try:
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.writelines(user_stats)
    except Exception as e:
        await message.reply_text("Не удалось создать файл со статистикой.")
        return

    # Проверяем, существует ли файл перед отправкой
    if os.path.exists(txt_file):
        try:
            await message.reply_document(document=txt_file, caption="Вот ваша статистика!")
            os.remove(txt_file)  # Удаляем файл после отправки
        except Exception as e:
            await message.reply_text("Не удалось отправить файл со статистикой.")
    else:
        await message.reply_text("Файл не найден, создание не удалось.")

if __name__ == '__main__':
    app.run()
