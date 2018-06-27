# бот адмін каналу
import telebot
import constants
bot = telebot.TeleBot(constants.token)
bot.send_message(constants.chat_id, constants.start)
# NEW USER
@bot.message_handler(content_types=['new_chat_members'])
def handle_text(message):
    bot.reply_to(message, constants.new_user.format(message.from_user.first_name))
# USER DELETE
@bot.message_handler(content_types=['left_chat_member'])
def handle_text(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, constants.del_user)
bot.polling(none_stop=True, interval=0)
