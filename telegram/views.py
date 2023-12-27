from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
import telebot
from .control import bot
import logging
from telebot.types import Message

@csrf_exempt
def index(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse("Telegram Bot")
    if request.method == 'POST':
        update = telebot.types.Update.de_json(
            request.body.decode("utf-8"))
        try:
            bot.process_new_updates([update])
        except Exception as e:
            logging.error(e)
        return HttpResponse(status=200)
    
    


@bot.message_handler(commands=['start'])
def start(msg:Message):
    bot.send_message(msg.chat.id, 'Assalomu alaykum hurmatli webhook foydalanuvchilari !')