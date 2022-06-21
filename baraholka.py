import datetime
import constants
import text
import telebot
from telebot import types
s = 0
psl = 0  # посилання на канал
pdp = 0  # кількість ПДП
prg = 0  # кількість преглядів
frm = 0  # формат

bot = telebot.TeleBot(constants.token)
bot.send_message(constants.id_group, text.start_bot)


@bot.message_handler(content_types=['new_chat_members'])
def handler_text(message):
    mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_photo(message.chat.id, open(constants.bot_sms_img, 'rb'),  f"{mention} " + text.new_user + text.tx_pravilo
                   + text.start_bot, parse_mode="HTML")


@bot.message_handler(content_types=['left_chat_member'])
def handler_text(message):
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(func=lambda message: message.chat.id == -1001465383382, content_types=['photo', 'text'])
def but_ft(message):
    mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
    if message.from_user.first_name != 'Telegram':
        st = ['creator', 'administrator', 'member']
        for ch in st:
            if ch == bot.get_chat_member(chat_id=constants.id_group, user_id=message.from_user.id).status:
                break
        else:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, f"{mention} " + text.bl_user.format(message.from_user.first_name) +
                             constants.ch_name, parse_mode="HTML")


# БОТ ---------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def handle_start(message):
    kbo = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_zm = types.InlineKeyboardButton(text=text.but_zam)
    button_nz = types.InlineKeyboardButton(text=text.tx_no)
    button_inf = types.InlineKeyboardButton(text=text.tx_inf)
    button_prod = types.InlineKeyboardButton(text=text.prod)
    kbo.add(button_zm)
    kbo.add(button_nz, button_inf)
    kbo.add(button_prod)
    bot.send_message(message.chat.id, text.start_bot, reply_markup=kbo)


@bot.message_handler(func=lambda message: message.text == text.but_zam)
def button_adm(message):
    global s
    psl = 0
    pdp = 0
    prg = 0
    frm = 0
    bot.send_message(message.chat.id, text.zl)
    s = 1
    message.chat.id = 0

    @bot.message_handler(func=lambda m: s == 1)  # посилання на канал
    def button_zgl(m):
        global psl, s
        psl = m.text
        bot.send_message(m.chat.id, text.zl0 + text.zg + psl, disable_web_page_preview=True)
        bot.send_message(m.chat.id, text.zl2)
        s = 2
        m.chat.id = 0

        @bot.message_handler(func=lambda fg: s == 2)  # кількість ПДП
        def button_pdp(op):
            global pdp, s
            pdp = op.text
            bot.send_message(op.chat.id, text.zl0 + text.zg + psl + text.pdp + pdp, disable_web_page_preview=True)
            bot.send_message(op.chat.id, text.zl3)
            s = 3
            op.chat.id = 0

            @bot.message_handler(func=lambda fg: s == 3)  # кількість преглядів
            def button_prg(pg):
                global prg, pdp, s
                prg = pg.text
                bot.send_message(pg.chat.id, text.zl0 + text.zg + psl + text.pdp + pdp + text.prg + prg,
                                 disable_web_page_preview=True)
                bot.send_message(pg.chat.id, text.zl4)
                s = 4
                pg.chat.id = 0

            @bot.message_handler(func=lambda fg: s == 4)  # ФОРМАТ реклами
            def button_prg(fr):
                global frm, s, pdp, prg
                frm = fr.text
                bot.send_message(fr.chat.id, text.zl0 + text.zg + psl + text.pdp + str(pdp) + text.prg + str(prg) +
                                 text.fr + str(frm), disable_web_page_preview=True)
                bot.send_message(fr.chat.id, text.pr_ent)
                s = 5
                fr.chat.id = 0

            @bot.message_handler(func=lambda pf: s == 5)  # ціна
            def button_pr(pr):
                global frm, prg
                key = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                but_y = types.InlineKeyboardButton(text=text.tx_yes)
                but_n = types.InlineKeyboardButton(text=text.tx_no)
                key.add(but_y, but_n)
                prs = pr.text
                now = datetime.date.today()
                dk = pr.message_id
                bot.send_message(pr.chat.id, text.zl0 + text.zg + psl + text.pdp + str(pdp) + text.prg + str(prg) +
                                 text.fr + str(frm) + text.pr + str(prs) + text. wal + text.ln + text.cont + text.us +
                                 pr.from_user.username + text.ln + text.idp + str(dk) + text.tm + str(now) + text.icn +
                                 constants.ch_name, reply_markup=key, disable_web_page_preview=True)


@bot.message_handler(func=lambda message: message.text == text.tx_yes)
def button_zak(message):
    global s
    df = int(message.message_id - 1)
    kbo = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_zm = types.InlineKeyboardButton(text=text.but_zam)
    button_nz = types.InlineKeyboardButton(text=text.tx_no)
    button_inf = types.InlineKeyboardButton(text=text.tx_inf)
    button_prod = types.InlineKeyboardButton(text=text.prod)
    kbo.add(button_zm)
    kbo.add(button_nz, button_inf, button_prod)
    bot.forward_message(constants.id_group, message.chat.id, message_id=df)
    bot.send_message(message.chat.id, text.send_ok, reply_markup=kbo)
    s = 0


@bot.message_handler(func=lambda message: message.text == text.tx_no)
def button_zak(message):
    kbo = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_zm = types.InlineKeyboardButton(text=text.but_zam)
    button_nz = types.InlineKeyboardButton(text=text.tx_no)
    button_inf = types.InlineKeyboardButton(text=text.tx_inf)
    button_prod = types.InlineKeyboardButton(text=text.prod)
    kbo.add(button_zm)
    kbo.add(button_nz, button_inf)
    kbo.add(button_prod)
    bot.send_message(message.chat.id, text.start_bot, reply_markup=kbo)
    global s
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
# MENU КНОПКИ Проекти--------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.prod)
def button_bot(message):
    bot.send_message(message.chat.id, text.info_prod, parse_mode='HTML', disable_web_page_preview=True)


bot.polling(none_stop=True, interval=1)
