
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    menu = InlineKeyboardMarkup()
    menu.add(InlineKeyboardButton("🎮 Demo Signal", callback_data="demo"))
    menu.add(InlineKeyboardButton("⭐ Lite / Premium", callback_data="premium"))
    bot.send_message(
        message.chat.id,
        "🚀 Welcome to Aviator Demo Bot!\n\nChoose an option below.\nDemo signals are examples, not real predictions.",
        reply_markup=menu
    )

@bot.callback_query_handler(func=lambda call: call.data == "demo")
def demo(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "🎮 DEMO SIGNAL\n\nExample only: 1.50x\nThis is random demo content, not a real prediction."
    )

@bot.callback_query_handler(func=lambda call: call.data == "premium")
def premium(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "⭐ Lite / Premium access information\n\nThis demo bot does not process payments."
    )

bot.infinity_polling()
                              
