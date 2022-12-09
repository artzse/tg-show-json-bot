from aiogram import Bot, Dispatcher, executor
from environs import Env

##### LOAD ENVIRONS #####
env = Env()
env.read_env("./data/.env")
BOT_TOKEN = env("BOT_TOKEN")
OWNER_ID = env("OWNER_ID")

##### LOAD AIOGRAM #####
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp)
