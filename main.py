import telebot
import requests
from settings import TOKEN, WEATHER_API_KEY

tg_bot = telebot.TeleBot(TOKEN)


hello_ = ("""Приветсвую тебя, на данный момент я умею:
Показать погоду в Ижевске [/weather]
Скинуть фото собаки [/dog_image]
""" )
error = "Пока я не умею это делать"

@tg_bot.message_handler(commands=["start"])
def hello_human(message):
    tg_bot.send_message(message.chat.id, hello_)
    print(message)

@tg_bot.message_handler(commands=["weather"])
def send_weather(message):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={56.8498}&lon={53.2045}&appid={WEATHER_API_KEY}"
    weather = requests.get(url).json()
    tg_bot.send_message(message.chat.id, weather["weather"][0]["description"])

@tg_bot.message_handler(commands=["dog_image"])
def send_dog_image(message):
    url = "https://dog.ceo/api/breeds/image/random"
    image_dog = requests.get(url).json()
    tg_bot.send_message(message.chat.id, image_dog["message"])

tg_bot.polling()
