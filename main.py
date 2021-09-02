from src.telegramBot import TelegramBot
from src.driveBot import driveBot

#bot = TelegramBot()
#bot.start()

driveBot = driveBot()
print(driveBot.get_data())