import telebot
import query
from telebot import types
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

welcome_message = (
        "Привет! Я бот To-Do List. Используй команды:\n"
        "/add - Добавить новую задачу\n"
        "/view - Посмотреть список задач\n"
        "/change - Изменить задачу\n"
        "/remove - Удалить задачу"
    )

@bot.message_handler(commands=["start"])
def say_hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Добавить задачу")
    btn2 = types.KeyboardButton("Удалить задачу")
    btn3 = types.KeyboardButton("Показать все задачи")
    btn4 = types.KeyboardButton("Изменить задачу")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,welcome_message,reply_markup=markup)
    query.user_add(message.from_user.id)

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text == "Добавить задачу":
        bot.send_message(message.chat.id,"Введите задачу")
        bot.register_next_step_handler(message,add_new_task)
    elif message.text == "Удалить задачу":
        bot.send_message(message.chat.id,"Введите какую задачу удалить")
        bot.register_next_step_handler(message,remove_process)
    elif message.text == "Показать все задачи":
        bot.send_message(message.chat.id,"Вот список ваших задач")
        bot.send_message(message.chat.id, query.view_task(message.from_user.id))
    elif message.text == "Изменить задачу":
        bot.send_message(message.chat.id,"Выберите номер задачи")
        bot.register_next_step_handler(message,change_text,message.text)

def add_new_task(message):
    user_id = message.from_user.id
    task = message.text
    query.add_task(user_id,task)
    bot.send_message(message.chat.id,"Задача успешно добавлена!")

def remove_process(message):
    user_id = message.from_user.id
    task = message.text
    query.remove_task(user_id,task)

def change_text(message,task_id):
    bot.send_message(message.chat.id,"Введите новую задачу")
    bot.register_next_step_handler(message,change,message.text)
def change(message,task_id):
    query.change_task(message.from_user.id,task_id,message.text)

bot.polling()
 