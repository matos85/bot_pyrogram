# User Bot для Telegram

Этот проект реализует User-бота для Telegram, который собирает статистику о полученных текстовых сообщениях. 
Бот записывает информацию о пользователях, времени отправки и содержании сообщения. Пользователь может получить отчет о своей активности, отправив команду `/statistics`.

## Описание

- Бот отслеживает текстовые сообщения, которые он получает.
- Сохраняет данные о каждом сообщении в локальный список.
- Позволяет пользователю получить отчет в виде текстового файла по команде `/statistics`.

## Установка и запуск

Следуйте этим шагам, чтобы установить и запустить бота:

1. **Установка зависимостей**:
   Убедитесь, что у вас установлен Python (рекомендуется версия 3.7 или выше). Используйте `pip` для установки необходимых библиотек:

   ```bash
   pip install pyrogram
   pip install TgCrypto
   ```

2. **Создание учетной записи разработчика в Telegram**:
   - Перейдите на сайт [Telegram API](https://my.telegram.org).
   - Создайте приложение, получите свой API ID и API Hash.

3. **Настройка конфигурации**:
   - Откройте файл с кодом и замените значения `API_ID`, `API_HASH` и `PHONE_NUMBER` на ваши собственные данные:

   ```python
   API_ID = "YOUR_API_ID"  # Ваш API ID
   API_HASH = "YOUR_API_HASH"  # Ваш API HASH
   PHONE_NUMBER = "YOUR_PHONE_NUMBER"  # Ваш номер телефона в формате международного кода
   ```

4. **Запуск бота**:
   - Выполните следующий команду в терминале, находясь в каталоге с кодом бота:

   ```bash
   python имя_вашего_файла.py
   ```

   - При первом запуске вам будет предложено ввести код аутентификации из Telegram для завершения авторизации.

## Использование

- **Отправка сообщений**: Просто отправляйте текстовые сообщения в любой чат, где добавлен бот. Бот будет записывать все сообщения.
- **Получение статистики**: Чтобы получить ваши сообщения в виде файла, просто отправьте `/statistics` в чат с ботом. Бот отправит файл `statistics.txt`, который будет содержать статистику сообщений.

## Логирование

Бот будет вести логирование событий с помощью `logging`. Вы можете изменить уровень логирования в коде:

```python
logging.basicConfig(level=logging.INFO)
```

## Зависимости

- Python 3.7+
- pyrogram
- TgCrypto

## Лицензия

Этот проект открыт и доступен для использования по лицензии MIT. Вы можете свободно изменять и распространять его.
