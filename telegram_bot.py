import logging
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = "7114900586:AAEaqwTl3nMMmv-q7_xh6SFriY-lNnNL5EA"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обработчик всех сообщений в группе.
    Проверяет, содержит ли сообщение слова "да", "Да" или "ДА"
    и отвечает "Пизда!" если находит совпадение.
    """
    if update.message and update.message.text:
        message_text = update.message.text.strip()
        
        # Проверяем точное совпадение с нужными словами
        if message_text in ["да", "Да", "ДА"]:
            try:
                # Отвечаем именно на сообщение пользователя (reply)
                await update.message.reply_text("Пизда!")
                logger.info(f"Ответил на сообщение '{message_text}' от пользователя {update.effective_user.username or update.effective_user.first_name}")
            except Exception as e:
                logger.error(f"Ошибка при отправке ответа: {e}")

def main() -> None:
    """Запуск бота"""
    # Проверяем, что токен установлен
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ ОШИБКА: Необходимо установить токен бота!")
        print("1. Получите токен у @BotFather в Telegram")
        print("2. Замените YOUR_BOT_TOKEN_HERE на ваш токен в файле telegram_bot.py")
        print("3. Или установите переменную окружения BOT_TOKEN")
        return
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчик для всех текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 Бот запущен и готов к работе!")
    print("Добавьте бота в группу и дайте ему права на чтение сообщений")
    
    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    # Можно использовать переменную окружения для токена (более безопасно)
    token_from_env = os.getenv('BOT_TOKEN')
    if token_from_env:
        BOT_TOKEN = token_from_env
    
    main()
