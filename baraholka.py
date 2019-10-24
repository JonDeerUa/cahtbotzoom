import datetime
import constants
import text
import telebot
from telebot import types
s = 0
d = 0
z = 0
o = 0
p = 0

bot = telebot.TeleBot(constants.token)
# БОТ ---------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def handle_start(message):
    kbo = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_zm = types.InlineKeyboardButton(text=text.but_zam)
    button_nz = types.InlineKeyboardButton(text=text.tx_no)
    button_inf = types.InlineKeyboardButton(text=text.tx_inf)
    kbo.add(button_zm)
    kbo.add(button_nz, button_inf)
    bot.send_message(message.chat.id, text.start_bot, reply_markup=kbo)


@bot.message_handler(func=lambda message: message.text == text.but_zam)
def button_adm(message):
    global z
    global d
    global o
    global p
    z = 0
    d = 0
    o = 0
    p = 0
    bot.send_message(message.chat.id, text.zl)
    global s
    s = 1
    message.chat.id = 0
    @bot.message_handler(func=lambda m: s == 1)
    def button_zgl(m):
        global z
        z = m.text
        bot.send_message(m.chat.id, text.zg + z)
        bot.send_message(m.chat.id, text.zl2)
        global s
        s = 2
        m.chat.id = 0
        @bot.message_handler(func=lambda fg: s == 2)
        def button_o(op):
            global o
            o = op.text
            bot.send_message(op.chat.id, text.zg + z + '\n' + text.ln + '\n' + text.op + o)
            bot.send_message(op.chat.id, text.pr_ent)
            global s
            s = 3
            op.chat.id = 0
            @bot.message_handler(func=lambda pf: s == 3)
            def button_pr(pr):
                global d
                global p
                p = pr.text
                now = datetime.date.today()
                d = pr.message_id + 1
                bot.send_message(pr.chat.id, {text.zg + z + '\n' + text.ln +
                                              '\n' + text.op + o +
                                              '\n' + text.ln + '\n' + text.pr + p + '\n' +
                                              text.cont + '@' + message.from_user.username +
                                              '\n' + text.ln +
                                              '\n' + text.idp + str(d) +
                                              '\n' + text.tm + str(now)
                                              })
                key = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                but_y = types.InlineKeyboardButton(text=text.tx_yes)
                but_n = types.InlineKeyboardButton(text=text.tx_no)
                key.add(but_y, but_n)
                bot.send_message(pr.chat.id, text.send, reply_markup=key)
                pr.chat.id = 0


@bot.message_handler(func=lambda message: message.text == text.tx_yes)
def button_zak(message):
    global d
    global s
    kbo = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_zm = types.InlineKeyboardButton(text=text.but_zam)
    button_nz = types.InlineKeyboardButton(text=text.tx_no)
    button_inf = types.InlineKeyboardButton(text=text.tx_inf)
    kbo.add(button_zm)
    kbo.add(button_nz, button_inf)
    bot.forward_message(constants.id_chat, message.chat.id, message_id=d)
    bot.send_message(message.chat.id, text.send_ok, reply_markup=kbo)
    d = 0
    s = 0


@bot.message_handler(func=lambda message: message.text == text.tx_no)
def button_zak(message):
    kbo = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_zm = types.InlineKeyboardButton(text=text.but_zam)
    button_nz = types.InlineKeyboardButton(text=text.tx_no)
    button_inf = types.InlineKeyboardButton(text=text.tx_inf)
    kbo.add(button_zm)
    kbo.add(button_nz, button_inf)
    bot.send_message(message.chat.id, text.start_bot, reply_markup=kbo)
    global d
    global s
    d = 0
    s = 0
# MENU ДОПОМОГА--------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_inf)
def button_zak(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_og = types.InlineKeyboardButton(text=text.b_pog, callback_data=text.b_pog)
    but_pr = types.InlineKeyboardButton(text=text.b_pr, callback_data=text.b_pr)
    key.add(but_og, but_pr)
    bot.send_message(message.chat.id, text.inf_dop, reply_markup=key)

# MENU КНОПКИ ОТВЕТА ДОПОМОГА--------------------------------------------------------------


@bot.callback_query_handler(func=lambda c: True)
def fin(c):
    if c.data == text.b_pog:
        bot.send_message(c.message.chat.id, text.start_bot)
    if c.data == text.b_pr:
        bot.send_message(c.message.chat.id, text.inf_pr)


@bot.message_handler(content_types='photo')
def button_ft(message):
    u = str('AgADAgADG6wxG2cTeUnrtw-aJuohk1fhtw8ABAEAAwIAA20AA9aoBQABFgQ')
    bot.send_photo(message.chat.id, u, text.no_phono)


bot.polling(none_stop=True, interval=1)
