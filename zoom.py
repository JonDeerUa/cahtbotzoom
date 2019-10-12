import constants
import text
import telebot
from telebot import types
count = 0
n = 0
s = 0
r = 1
p = 10
t = 0
pl = 0
nw = 0
p1 = 0
sp = 0
i = 0

ADM_ID = 477513583  # ID админа групы -----------------------------------------------
bot = telebot.TeleBot(constants.token)
bot.send_message(constants.chat_id, text.start)
# NEW USER ---------------------------------------------------------------------------


@bot.message_handler(content_types=['new_chat_members'])
def handler_text(message):
    h = open('tx_n.txt', 'r')
    ntx = h.read()
    h.close()
    h = open('n_seven_days.txt', 'r')
    ztx = h.read()
    h.close()
    bot.reply_to(message, text.new_user.format(message.from_user.first_name) + text.tx_zk1 + ntx + text.tx_zk + text.new_user_pr + text.ps_pr + ztx + text.sev_d + text.z_c)
    # USER DELETE --------------------------------------------------------------------------


# @bot.message_handler(content_types=['left_chat_member'])
# def handler_text(message):
#    h = open('tx_zak.txt', 'r')
#    ztx = h.read()
#    h.close()
#    h = open('z_one_day.txt', 'r')
#    opr = h.read()
#    h.close()
#    f = open('z_seven_days.txt', 'r')
#    spr = f.read()
#    f.close()
#    bot.delete_message(message.chat.id, message.message_id)
#    bot.send_message(message.chat.id, text.info_but_zak + ztx + text.info_lin + text.post_pr + opr + text.on_d + text.ps_pr + spr + text.sev_d)
# Spam  2 SMS Реклама Плюс --------------------------------------------------------------------


GROUP_ID = -1001149334895  # ID чата------------------------------------------------------------


@bot.message_handler(func=lambda message:  message.chat.id == GROUP_ID)
def set_ro(message):
    global n
    global count
    global s
    global r
    global i
    if i == 1:
        idp = message.message_id
        bot.send_message(constants.chat_r_id, message.text)
        bot.send_message(constants.chat_r_id, idp)
        i = 0
        int(idp)
        f = open('id_post.txt', 'w')
        f.write(str(idp))
        f.close()
        bot.send_message(constants.chat_r_id, text.info_save)
    if r < message.message_id:
        h = open('id_post.txt', 'r')
        plus_id = h.read()
        h.close()
        bot.forward_message(message.chat.id, message.chat.id, message_id=plus_id)
        r = message.message_id + 10
    if count == 0:
        n = n+1
        s = message.from_user.id
        count = message.from_user.id
        return
    if count == message.from_user.id:
        s = message.from_user.id
        n = n+1
    if s != message.from_user.id:
        count = message.from_user.id
        n = 1
        return
    if n == 2:
        h = open('tx_s.txt', 'r')
        stx = h.read()
        h.close()
        h = open('s_seven_days.txt', 'r')
        ztx = h.read()
        h.close()
        bot.send_message(message.chat.id, text.spam_post.format(message.from_user.first_name) + text.tx_zk1 + stx + text.tx_zk + text.new_user_pr + text.ps_pr + ztx + text.sev_d + text.z_c)
        return
    if n >= 3:
        bot.delete_message(message.chat.id, message.message_id)
        return
# ---------------------ЧАТ БОТА------------------------------------------------------------
# Главное меню кнопки------------------------------------------------


@bot.message_handler(commands=['start'])
def handle_start(message):
    kbo = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_pv = types.InlineKeyboardButton(text=text.text_button_pra)
    button_b = types.InlineKeyboardButton(text=text.text_button_bot)
    button_sl = types.InlineKeyboardButton(text=text.text_button_sal)
    button_cl = types.InlineKeyboardButton(text=text.text_button_cha)
    button_s = types.InlineKeyboardButton(text=text.text_button_set)
    button_st = types.InlineKeyboardButton(text=text.text_button_stat)
    button_vps = types.InlineKeyboardButton(text=text.text_button_vs)
    but_adm = types.InlineKeyboardButton(text=text.text_but_adm)
    kbo.add(button_st, button_sl, button_pv, button_b, button_vps)
    kbo.add(button_cl, button_s)
    user_adm = 477513583  # ID - АДМИНА БОТА ------------------------------------------------
    if message.chat.id == user_adm:
        kbo.add(but_adm)
    bot.send_photo(message.chat.id, photo=open(constants.bot_img, 'rb'))
    bot.send_message(message.chat.id, text.chat_new_user.format(message.from_user.first_name), reply_markup=kbo)
# Кнопка --ВОЗРАТ В ГЛАВНОЕ МЕНЮ-----------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_but_gm)
def button_adm(message):
    global t
    t = 1
    kbo = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_pv = types.InlineKeyboardButton(text=text.text_button_pra)
    button_b = types.InlineKeyboardButton(text=text.text_button_bot)
    button_sl = types.InlineKeyboardButton(text=text.text_button_sal)
    button_cl = types.InlineKeyboardButton(text=text.text_button_cha)
    button_s = types.InlineKeyboardButton(text=text.text_button_set)
    button_st = types.InlineKeyboardButton(text=text.text_button_stat)
    button_vps = types.InlineKeyboardButton(text=text.text_button_vs)
    but_adm = types.InlineKeyboardButton(text=text.text_but_adm)
    kbo.add(button_st, button_sl, button_pv, button_b, button_vps)
    kbo.add(button_cl, button_s)
    if message.chat.id == 477513583:  # ID - АДМИНА БОТА ------------------------------------------------
        kbo.add(but_adm)
    bot.send_message(message.chat.id, text.tx_wl, reply_markup=kbo)
# MENU 🚀 Заказ рекламы---------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_button_stat)
def button_stat(message):
    zr = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    but_zak = types.InlineKeyboardButton(text=text.text_but_zak)
    but_new = types.InlineKeyboardButton(text=text.text_but_new)
    but_spam = types.InlineKeyboardButton(text=text.text_but_spam)
    but_pros = types.InlineKeyboardButton(text=text.text_but_pros)
    but_plus = types.InlineKeyboardButton(text=text.text_but_plus)
    button_t3 = types.InlineKeyboardButton(text=text.text_but_gm)
    zr.add(but_zak)
    zr.add(but_plus, but_new, but_spam, but_pros, button_t3)
    bot.send_message(message.chat.id, text.inf_but_st, reply_markup=zr)
# МЕНЮ-💰 Заработать-------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_button_sal)
def button_sal(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text=text.text_but_1, callback_data=text.text_but_1)
    but_3 = types.InlineKeyboardButton(text=text.text_but_3, callback_data=text.text_but_3)
    but_4 = types.InlineKeyboardButton(text=text.text_but_4, callback_data=text.text_but_4)
    but_2 = types.InlineKeyboardButton(text=text.text_but_2, callback_data=text.text_but_2)
    key.add(but_4, but_3, but_2, but_1)
    bot.send_message(message.chat.id, text.text_info, reply_markup=key)
# MENU 📃 Правила чата----------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_button_pra)
def button_pra(message):
    bot.send_message(message.chat.id, text.info_button_pra)
# MENU 🤖 Что я умею----------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_button_bot)
def button_bot(message):
    bot.send_message(message.chat.id, text.info_button_bot)
# MENU 💬 Обратная связь----------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_button_vs)
def button_vs(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_pay = types.InlineKeyboardButton(text=text.text_but_pay, callback_data=text.text_but_pay)
    but_cont = types.InlineKeyboardButton(text=text.text_vp, url=constants.cont)
    key.add(but_pay, but_cont)
    bot.send_message(message.chat.id, text.info_button_vs, reply_markup=key)
    bot.send_message(constants.chat_r_id, text.text_button_vs)
# МЕНЮ 📣 Каталог каналов------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_button_cha)
def button_cha(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_rch = types.InlineKeyboardButton(text=text.text_vh, url=constants.pic_url)
    key.add(but_rch)
    bot.send_photo(message.chat.id, photo=open(constants.pic_img, 'rb'))
    bot.send_message(message.chat.id, text.info_1000, reply_markup=key)
# МЕНЮ 🎯 Рекламный чат------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_button_set)
def button_set(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_rch = types.InlineKeyboardButton(text=text.text_vh, url=constants.best_url)
    key.add(but_rch)
    bot.send_photo(message.chat.id, photo=open(constants.best_img, 'rb'))
    bot.send_message(message.chat.id, text.info_bc, reply_markup=key)

    key = types.InlineKeyboardMarkup(row_width=1)
    but_zoom = types.InlineKeyboardButton(text=text.text_vh, url=constants.zoom_url)
    key.add(but_zoom)
    bot.send_photo(message.chat.id, photo=open(constants.zoom_img, 'rb'))
    bot.send_message(message.chat.id, text.info_zc, reply_markup=key)

    key = types.InlineKeyboardMarkup(row_width=1)
    but_ua = types.InlineKeyboardButton(text=text.text_vh, url=constants.ua_url)
    key.add(but_ua)
    bot.send_photo(message.chat.id, photo=open(constants.ua_img, 'rb'))
    bot.send_message(message.chat.id, text.info_ua, reply_markup=key)
# МЕНЮ 🔓 АДМИНКА------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_but_adm)
def button_adm(message):
    kbo = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_t1 = types.InlineKeyboardButton(text=text.tx_z_red)
    button_t2 = types.InlineKeyboardButton(text=text.tx_pl_red)
    button_t4 = types.InlineKeyboardButton(text=text.tx_n_red)
    button_t5 = types.InlineKeyboardButton(text=text.tx_s_red)
    button_t6 = types.InlineKeyboardButton(text=text.tx_1_red)
    button_t7 = types.InlineKeyboardButton(text=text.text_but_vid)
    button_t3 = types.InlineKeyboardButton(text=text.text_but_gm)
    kbo.add(button_t1, button_t2, button_t4, button_t5, button_t6, button_t7, button_t3)
    bot.send_message(message.chat.id, text.tx_wl_bos, reply_markup=kbo)
# Кнопка АДМИНКА КНОПКА НАЗАД ---------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_but_nz)
def button_nz(message):
    kbo = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_t1 = types.InlineKeyboardButton(text=text.tx_z_red)
    button_t2 = types.InlineKeyboardButton(text=text.tx_pl_red)
    button_t4 = types.InlineKeyboardButton(text=text.tx_n_red)
    button_t5 = types.InlineKeyboardButton(text=text.tx_s_red)
    button_t6 = types.InlineKeyboardButton(text=text.tx_1_red)
    button_t7 = types.InlineKeyboardButton(text=text.text_but_vid)
    button_t3 = types.InlineKeyboardButton(text=text.text_but_gm)
    kbo.add(button_t1, button_t2, button_t4, button_t5, button_t6, button_t7, button_t3)
    bot.send_message(message.chat.id, text.tx_wl, reply_markup=kbo)
# Кнопка МЕНЮ 🚀 Заказ рекламы--------------------------------------------------------------->>>>
# Кнопка 📌 Ваш пост в закрепе ЗАКАЗ-------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_but_zak)
def button_sd(message):
    global t
    h = open('tx_zak.txt', 'r')
    ztx = h.read()
    h.close()
    h = open('z_one_day.txt', 'r')
    opr = h.read()
    h.close()
    f = open('z_seven_days.txt', 'r')
    spr = f.read()
    f.close()
    bot.send_message(message.chat.id, text.info_but_zak + ztx + text.info_lin + text.post_pr + opr + text.on_d + text.ps_pr + spr + text.sev_d)
    bot.send_message(constants.chat_r_id, text.text_but_zak)
    h = open('zak_status.txt', 'r')
    z = h.read(1)
    h.close()
    if z == '-':
        t = 1
        h = open('zak_status.txt', 'r')
        ds = h.read()
        bot.send_message(message.chat.id, text.info_zak_no + '\n' + ds)
        h.close()
    if z == '+':
        t = 0
        kzz = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        b_gm = types.InlineKeyboardButton(text=text.text_but_gm)
        kzz.add(b_gm)
        bot.send_message(message.chat.id, text.info_zak_yes_1, reply_markup=kzz)

        @bot.message_handler(func=lambda a: t == 0)
        def send_z_zak(m):
            global p
            p = message.chat.id
            bot.send_message(constants.chat_r_id, m.from_user.username)
            bot.send_message(constants.chat_r_id, p)
            bot.send_message(constants.chat_r_id, m.text)
            bot.send_message(p, text.info_zak_yes_2.format(message.from_user.first_name) + text.inf_g + text.inf_p)
            key = types.InlineKeyboardMarkup(row_width=1)
            but_pay = types.InlineKeyboardButton(text=text.text_but_pay, callback_data=text.text_but_pay)
            key.add(but_pay)
            bot.send_message(p, text.in_un + message.from_user.username, reply_markup=key)
            zkr = open('zak_status.txt', 'w')
            zkr.write('-\n' + text.status_1)
            zkr.close()
            ks = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            b_gs = types.InlineKeyboardButton(text=text.text_but_gm)
            ks.add(b_gs)
            global t
            t = 1
# Кнопка ➕ Реклама плюс ЗАКАЗ----------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_but_plus)
def button_pl(message):
    global pl
    h = open('pl_one_day.txt', 'r')
    opl = h.read()
    h.close()
    f = open('pl_seven_days.txt', 'r')
    spr = f.read()
    f.close()
    bot.send_message(constants.chat_r_id, text.text_but_plus)
    bot.send_message(message.chat.id, text.info_but_plus + text.ps_pr + opl + text.on_d + text.ps_pr + spr + text.sev_d)
    h = open('pl_status.txt', 'r')
    d = h.read(1)
    h.close()
    if d == '-':
        pl = 1
        h = open('pl_status.txt', 'r')
        ds = h.read()
        bot.send_message(message.chat.id, text.info_zak_no + '\n' + ds)
        h.close()
    if d == '+':
        pl = 0
        kzz = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        b_gm = types.InlineKeyboardButton(text=text.text_but_gm)
        kzz.add(b_gm)
        bot.send_message(message.chat.id, text.info_zak_yes_1, reply_markup=kzz)

        @bot.message_handler(func=lambda a: pl == 0)
        def send_z_zak(m):
            global p
            p = message.chat.id
            bot.send_message(constants.chat_r_id, m.from_user.username)
            bot.send_message(constants.chat_r_id, p)
            bot.send_message(constants.chat_r_id, m.text)
            bot.send_message(p, text.info_zak_yes_2.format(message.from_user.first_name) + text.inf_g + text.inf_p)
            key = types.InlineKeyboardMarkup(row_width=1)
            but_pay = types.InlineKeyboardButton(text=text.text_but_pay, callback_data=text.text_but_pay)
            key.add(but_pay)
            bot.send_message(p, text.in_un + message.from_user.username, reply_markup=key)
            fpl = open('pl_status.txt', 'w')
            fpl.write('-\n' + text.status_1)
            fpl.close()
            ks = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            b_gs = types.InlineKeyboardButton(text=text.text_but_gm)
            ks.add(b_gs)
            global pl
            pl = 1
# Кнопка 👥 Новый учасник--ЗАКАЗ-------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_but_new)
def button_new(message):
    global nw
    h = open('n_seven_days.txt', 'r')
    ntx = h.read()
    h.close()
    bot.send_photo(message.chat.id, photo=open(constants.new_img, 'rb'))
    bot.send_message(message.chat.id, text.info_but_new + text.ps_pr + ntx + text.sev_d)
    bot.send_message(constants.chat_r_id, text.text_but_new)
    h = open('n_status.txt', 'r')
    b = h.read(1)
    h.close()
    if b == '-':
        nw = 1
        h = open('n_status.txt', 'r')
        ds = h.read()
        bot.send_message(message.chat.id, text.info_zak_no + '\n' + ds)
        h.close()
    if b == '+':
        nw = 0
        kzz = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        b_gm = types.InlineKeyboardButton(text=text.text_but_gm)
        kzz.add(b_gm)
        bot.send_message(message.chat.id, text.info_zak_spam, reply_markup=kzz)

        @bot.message_handler(func=lambda a: nw == 0)
        def send_z_zak(m):
            global p
            p = message.chat.id
            bot.send_message(constants.chat_r_id, m.from_user.username)
            bot.send_message(constants.chat_r_id, p)
            bot.send_message(constants.chat_r_id, m.text)
            bot.send_message(p, text.info_zak_yes_2.format(message.from_user.first_name) + text.inf_g + text.inf_p)
            key = types.InlineKeyboardMarkup(row_width=1)
            but_pay = types.InlineKeyboardButton(text=text.text_but_pay, callback_data=text.text_but_pay)
            key.add(but_pay)
            bot.send_message(p, text.in_un + message.from_user.username, reply_markup=key)
            fpl = open('n_status.txt', 'w')
            fpl.write('-\n' + text.status_1)
            fpl.close()
            ks = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            b_gs = types.InlineKeyboardButton(text=text.text_but_gm)
            ks.add(b_gs)
            global nw
            nw = 1
# Кнопка 🔕 Анти спам--ЗАКАЗ-------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_but_spam)
def button_new(message):
    global sp
    h = open('s_seven_days.txt', 'r')
    ntx = h.read()
    h.close()
    bot.send_photo(message.chat.id, photo=open(constants.spam_img, 'rb'))
    bot.send_message(message.chat.id, text.info_but_new + text.ps_pr + ntx + text.sev_d)
    bot.send_message(constants.chat_r_id, text.text_but_spam)
    h = open('s_status.txt', 'r')
    b = h.read(1)
    h.close()
    if b == '-':
        sp = 1
        h = open('s_status.txt', 'r')
        ds = h.read()
        bot.send_message(message.chat.id, text.info_zak_no + '\n' + ds)
        h.close()
    if b == '+':
        sp = 0
        kzz = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        b_gm = types.InlineKeyboardButton(text=text.text_but_gm)
        kzz.add(b_gm)
        bot.send_message(message.chat.id, text.info_zak_spam, reply_markup=kzz)

        @bot.message_handler(func=lambda a: sp == 0)
        def send_z_zak(m):
            global p
            p = message.chat.id
            bot.send_message(constants.chat_r_id, m.from_user.username)
            bot.send_message(constants.chat_r_id, p)
            bot.send_message(constants.chat_r_id, m.text)
            bot.send_message(p, text.info_zak_yes_2.format(message.from_user.first_name) + text.inf_g + text.inf_p)
            key = types.InlineKeyboardMarkup(row_width=1)
            but_pay = types.InlineKeyboardButton(text=text.text_but_pay, callback_data=text.text_but_pay)
            key.add(but_pay)
            bot.send_message(p, text.in_un + message.from_user.username, reply_markup=key)
            fpl = open('s_status.txt', 'w')
            fpl.write('-\n' + text.status_1)
            fpl.close()
            ks = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            b_gs = types.InlineKeyboardButton(text=text.text_but_gm)
            ks.add(b_gs)
            global sp
            sp = 1
# Кнопка 👁 1.000--ЗАКАЗ-------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.text_but_pros)
def button_new(message):
    global p1
    h = open('pr_1000.txt', 'r')
    ntx = h.read()
    h.close()
    bot.send_message(message.chat.id, text.info_but_1000)
    bot.send_message(message.chat.id, text.ps_pr + ntx + text.tx_1)
    bot.send_message(constants.chat_r_id, text.text_but_pros)
    h = open('1_status.txt', 'r')
    b = h.read(1)
    h.close()
    if b == '-':
        bot.send_message(message.chat.id, text.info_1000_no)
        bot.send_message(constants.chat_r_id, text.text_but_pros)
    if b == '+':
        p1 = 0
        kzz = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        b_gm = types.InlineKeyboardButton(text=text.text_but_gm)
        kzz.add(b_gm)
        bot.send_message(message.chat.id, text.info_zak_yes_1, reply_markup=kzz)

        @bot.message_handler(func=lambda a: p1 == 0)
        def send_z_zak(m):
            global p
            p = message.chat.id
            bot.send_message(constants.chat_r_id, m.from_user.username)
            bot.send_message(constants.chat_r_id, p)
            bot.send_message(constants.chat_r_id, m.text)
            bot.send_message(p, text.info_zak_yes_2.format(message.from_user.first_name) + text.inf_g + text.inf_p)
            key = types.InlineKeyboardMarkup(row_width=1)
            but_pay = types.InlineKeyboardButton(text=text.text_but_pay, callback_data=text.text_but_pay)
            key.add(but_pay)
            bot.send_message(p, text.in_un + message.from_user.username, reply_markup=key)
            fpl = open('s_status.txt', 'w')
            fpl.write('-\n' + text.status_1)
            fpl.close()
            ks = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            b_gs = types.InlineKeyboardButton(text=text.text_but_gm)
            ks.add(b_gs)
            global p1
            p1 = 1
# MENU КНОПКИ ОТВЕТА ГЛАВНОГО МЕНЮ--------------------------------------------------------------


@bot.callback_query_handler(func=lambda c: True)
def fin(c):
    if c.data == text.text_but_1:
        bot.send_message(c.message.chat.id, text.info_button_sal)
        bot.send_message(constants.chat_r_id, text.text_but_1)
    if c.data == text.text_but_3:
        markup = types.InlineKeyboardMarkup()
        btn_mg = types.InlineKeyboardButton(text=text.text_vh, url=constants.cat_url)
        markup.add(btn_mg)
        bot.send_photo(c.message.chat.id, photo=open(constants.cat_img, 'rb'))
        bot.send_message(c.message.chat.id, text.tx_bot_tmo, reply_markup=markup)
        bot.send_message(constants.chat_r_id, text.text_but_3)
    if c.data == text.text_but_2:
        markup = types.InlineKeyboardMarkup()
        btn_mg = types.InlineKeyboardButton(text=text.text_vh, url=constants.wmz_url)
        markup.add(btn_mg)
        bot.send_photo(c.message.chat.id, photo=open(constants.wmz_pic, 'rb'))
        bot.send_message(c.message.chat.id, text.inf_gr, reply_markup=markup)
        bot.send_message(constants.chat_r_id, text.text_but_2)
    if c.data == text.text_but_4:
        key = types.InlineKeyboardMarkup(row_width=1)
        but_bonus = types.InlineKeyboardButton(text=text.text_bonus, callback_data=text.text_bonus)
        key.add(but_bonus)
        bot.send_message(c.message.chat.id, text.info_bot_4, reply_markup=key)
        bot.send_message(constants.chat_r_id, text.text_but_4)
    if c.data == text.text_bonus:
        key = types.InlineKeyboardMarkup(row_width=1)
        but_bon = types.InlineKeyboardButton(text=text.text_zak, callback_data=text.text_zak)
        key.add(but_bon)
        bot.send_message(c.message.chat.id, text.info_sponsor, reply_markup=key)
        bot.send_message(constants.chat_r_id, text.text_bonus)
    if c.data == text.text_zak:
        kzz = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bot.send_message(c.message.chat.id, text.tx_no_z, reply_markup=kzz)
    if c.data == text.text_but_pay:
        kzz = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        bot.send_message(c.message.chat.id, text.tx_wall, reply_markup=kzz)
        bot.send_message(c.message.chat.id, text.tx_w1, reply_markup=kzz)
        bot.send_message(c.message.chat.id, text.tx_w2, reply_markup=kzz)
        bot.send_message(c.message.chat.id, text.tx_w3, reply_markup=kzz)
# Кнопка 📌 Ред. закреп------------------------------------------------------->>>>>>>>>


@bot.message_handler(func=lambda message: message.text == text.tx_z_red)
def button_zak(message):
    kzr = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    b_z_yes = types.InlineKeyboardButton(text=text.tx_z_on)
    b_z_no = types.InlineKeyboardButton(text=text.tx_z_off)
    b_z_tx = types.InlineKeyboardButton(text=text.tx_z_rtx)
    b_z_pr = types.InlineKeyboardButton(text=text.tx_z_rpr)
    b_z_sms = types.InlineKeyboardButton(text=text.tx_z_sms)
    b_z_nd = types.InlineKeyboardButton(text=text.text_but_nz)
    kzr.add(b_z_yes, b_z_no, b_z_tx, b_z_pr, b_z_sms, b_z_nd)
    h = open('tx_zak.txt', 'r')
    ztx = h.read()
    h.close()
    h = open('z_one_day.txt', 'r')
    opr = h.read()
    h.close()
    f = open('z_seven_days.txt', 'r')
    spr = f.read()
    f.close()
    bot.send_message(message.chat.id, text.info_but_zak + ztx + text.info_lin + text.post_pr + opr + text.on_d + text.ps_pr + spr + text.sev_d)
    bot.send_message(message.chat.id, text.inf_red, reply_markup=kzr)
# Меню ред.закреп - кнопка 📌 Свободно------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_z_on)
def button_sd(message):
    global t
    t = 1
    h = open('zak_status.txt', 'w')
    h.write('+')
    h.close()
    bot.send_message(message.chat.id, text.info_save)
# Меню ред.закреп - кнопка 📍 Занято------------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_z_off)
def button_sd(message):
    h = open('zak_status.txt', 'w')
    h.write('-')
    h.close()
    bot.send_message(message.chat.id, text.inf_date)

    @bot.message_handler(func=lambda f: message.chat.id == ADM_ID)
    def send_dt(m):
        dt = m.text
        date = open('zak_status.txt', 'a')
        date.write('\n' + dt)
        date.close()
        bot.send_message(constants.chat_r_id, dt)
        bot.send_message(constants.chat_r_id, text.info_save)
        message.chat.id = 0
# Меню ред.закреп - кнопка 📝 Ред. текст (📌)---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_z_rtx)
def button_sd(message):
    h = open('tx_zak.txt', 'r')
    ztx = h.read()
    h.close()
    bot.send_message(message.chat.id, text.info_but_zak + ztx + '\n' + text.info_lin)
    bot.send_message(message.chat.id, 'Введіть новий текст')

    @bot.message_handler(func=lambda f: message.chat.id == ADM_ID)
    def send_dt(m):
        dtp = m.text
        date = open('tx_zak.txt', 'w')
        date.write(dtp)
        date.close()
        bot.send_message(constants.chat_r_id, dtp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню ред.закреп - кнопка 📈 Ред. цену (📌) ВЫБОР  дней---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_z_rpr)
def button_sd(message):
    h = open('z_one_day.txt', 'r')
    opr = h.read()
    h.close()
    f = open('z_seven_days.txt', 'r')
    spr = f.read()
    f.close()
    kzp = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    b_z_1 = types.InlineKeyboardButton(text=text.pr_one)
    b_z_7 = types.InlineKeyboardButton(text=text.pr_sev)
    b_z_nd = types.InlineKeyboardButton(text=text.text_but_nz)
    kzp.add(b_z_1, b_z_7, b_z_nd)
    bot.send_message(message.chat.id, text.info_lin + text.post_pr + opr + text.on_d + text.ps_pr + spr + text.sev_d)
    bot.send_message(message.chat.id, text.tx_wtf, reply_markup=kzp)
# Меню ред.закреп - кнопка 📈 Ред. цену (📌) РЕДАКТОР 💰 цена за 1 день---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.pr_one)
def button_one(message):
    bot.send_message(message.chat.id, text.pr_one_v)

    @bot.message_handler(func=lambda pr: message.chat.id == ADM_ID)
    def send_dt(m):
        dtp = m.text
        date = open('z_one_day.txt', 'w')
        date.write(dtp)
        date.close()
        bot.send_message(constants.chat_r_id, dtp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню ред.закреп - кнопка 📈 Ред. цену (📌) РЕДАКТОР 💰 цена за 7 дн---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.pr_sev)
def button_one(message):
    bot.send_message(message.chat.id, text.pr_sev_v)

    @bot.message_handler(func=lambda pr: message.chat.id == ADM_ID)
    def send_dt(m):
        dtp = m.text
        date = open('z_seven_days.txt', 'w')
        date.write(dtp)
        date.close()
        bot.send_message(constants.chat_r_id, dtp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню ред.закреп - кнопка 📨 Повідомити (📌)---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_z_sms)
def button_sd(message):
    bot.send_message(message.chat.id, text.id_zam)

    @bot.message_handler(func=lambda d: message.chat.id == ADM_ID)
    def send_sms(m):
        h = open('zak_status.txt', 'r')
        ztx = h.read()
        h.close()
        sd = m.text
        message.chat.id = sd
        bot.send_message(message.chat.id, text.tx_sms_zak + ztx)
        bot.send_message(constants.chat_r_id, text.tx_sms_zak + ztx)
        message.chat.id = 0
# Кнопка РЕД Реклама ПЛЮС ➕ Реклама плюс------------------------------------------------------->>>>>


@bot.message_handler(func=lambda message: message.text == text.tx_pl_red)
def button_zak(message):
    h = open('pl_one_day.txt', 'r')
    opl = h.read()
    h.close()
    f = open('pl_seven_days.txt', 'r')
    spr = f.read()
    f.close()
    kzr = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    b_z_yes = types.InlineKeyboardButton(text=text.tx_pl_on)
    b_z_no = types.InlineKeyboardButton(text=text.tx_pl_off)
    b_z_tx = types.InlineKeyboardButton(text=text.tx_pl_rtx)
    b_z_pr = types.InlineKeyboardButton(text=text.tx_pl_light)
    b_id_post = types.InlineKeyboardButton(text=text.tx_id_post)
    b_sms_pl = types.InlineKeyboardButton(text=text.tx_pl_sms)
    b_z_nd = types.InlineKeyboardButton(text=text.text_but_nz)
    kzr.add(b_z_yes, b_z_no, b_z_tx, b_z_pr, b_id_post, b_sms_pl, b_z_nd)
    bot.send_message(message.chat.id, text.info_but_plus + text.ps_pr + opl + text.on_d + text.ps_pr + spr + text.sev_d)
    bot.send_message(message.chat.id, text.inf_red, reply_markup=kzr)
# Меню ред.реклама ПЛЮС - кнопка ➕ Свободно ------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_pl_on)
def button_sd(message):
    h = open('pl_status.txt', 'w')
    h.write('+')
    h.close()
    bot.send_message(message.chat.id, text.info_save)
# Меню ред.реклама ПЛЮС - кнопка 🔚 Занято (➕)-----------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_pl_off)
def button_sd(message):
    h = open('pl_status.txt', 'w')
    h.write('-')
    h.close()
    bot.send_message(message.chat.id, text.inf_date)

    @bot.message_handler(func=lambda f: message.chat.id == ADM_ID)
    def send_dt(m):
        dtp = m.text
        date = open('pl_status.txt', 'a')
        date.write('\n' + dtp)
        date.close()
        bot.send_message(constants.chat_r_id, dtp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню ред.реклама плюс - кнопка 💰 цена за 1 день(➕)---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_pl_rtx)
def button_one(message):
    bot.send_message(message.chat.id, text.pr_one_v)

    @bot.message_handler(func=lambda pr: message.chat.id == ADM_ID)
    def send_dt(m):
        dl = m.text
        plo = open('pl_one_day.txt', 'w')
        plo.write(dl)
        plo.close()
        bot.send_message(constants.chat_r_id, dl)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню ред.реклама плюс - кнопка 💰 цена за 7 дн(➕)---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_pl_light)
def button_one(message):
    bot.send_message(message.chat.id, text.pr_sev_v)

    @bot.message_handler(func=lambda pr: message.chat.id == ADM_ID)
    def send_dt(m):
        dp = m.text
        dpl = open('pl_seven_days.txt', 'w')
        dpl.write(dp)
        dpl.close()
        bot.send_message(constants.chat_r_id, dp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню ред.реклама плюс - кнопка 🆔 ID post-------------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_id_post)
def button_sd(m):
    bot.send_message(constants.chat_r_id, text.inf_for_pl)
    global i
    i = 1
    m.i = 1
# Меню ред.реклама плюс - кнопка 📨 Повідомити ---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_pl_sms)
def button_sd(message):
    bot.send_message(message.chat.id, text.id_zam)

    @bot.message_handler(func=lambda d: message.chat.id == ADM_ID)
    def send_sms(m):
        h = open('pl_status.txt', 'r')
        ztx = h.read()
        h.close()
        sd = m.text
        message.chat.id = sd
        bot.send_message(message.chat.id, text.tx_sms_pl + ztx)
        bot.send_message(constants.chat_r_id, text.tx_sms_pl + ztx)
        message.chat.id = 0
# Кнопка 👥 Новый учасник--РЕДАКТОР------------------------------------------------------------>>>>


@bot.message_handler(func=lambda message: message.text == text.tx_n_red)
def button_new(message):
    h = open('n_seven_days.txt', 'r')
    ntx = h.read()
    h.close()
    kzr = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    b_n_yes = types.InlineKeyboardButton(text=text.tx_n_on)
    b_n_no = types.InlineKeyboardButton(text=text.tx_n_off)
    b_n_pr = types.InlineKeyboardButton(text=text.tx_n_rpr)
    b_n_rp = types.InlineKeyboardButton(text=text.tx_n_rp)
    b_n_sms = types.InlineKeyboardButton(text=text.tx_n_sms)
    b_z_nd = types.InlineKeyboardButton(text=text.text_but_nz)
    kzr.add(b_n_yes, b_n_no, b_n_pr, b_n_rp, b_n_sms, b_z_nd)
    bot.send_message(message.chat.id, text.inf_red + text.ps_pr + ntx + text.sev_d, reply_markup=kzr)
# Меню ред.Новий учасник - кнопка  🔛 Свободно(👥)-----------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_n_on)
def button_sd(message):
    global nw
    nw = 1
    h = open('n_status.txt', 'w')
    h.write('+')
    h.close()
    h = open('tx_n.txt', 'w')
    h.write(str(text.no_rek))
    h.close()
    bot.send_message(message.chat.id, text.info_save)
# Меню ред.Новий учасник - кнопка 🔚 Занято(👥)-----------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_n_off)
def button_sd(message):
    h = open('n_status.txt', 'w')
    h.write('-')
    h.close()
    bot.send_message(message.chat.id, text.inf_date)

    @bot.message_handler(func=lambda f: message.chat.id == ADM_ID)
    def send_dt(m):
        dtp = m.text
        date = open('n_status.txt', 'a')
        date.write('\n' + dtp)
        date.close()
        bot.send_message(constants.chat_r_id, dtp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню ред.Новий учасник - кнопка 📈 Ред. цену(👥)---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_n_rpr)
def button_one(message):
    bot.send_message(message.chat.id, text.pr_sev_v)

    @bot.message_handler(func=lambda pr: message.chat.id == ADM_ID)
    def send_dt(m):
        dtp = m.text
        date = open('n_seven_days.txt', 'w')
        date.write(dtp)
        date.close()
        bot.send_message(constants.chat_r_id, dtp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню ред Новий учасник - кнопка 🚀 Доб.пост(👥)---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_n_rp)
def button_n(message):
    h = open('tx_n.txt', 'r')
    ntx = h.read()
    h.close()
    bot.send_message(message.chat.id, text.rek_post + ntx)
    bot.send_message(message.chat.id, text.new_tx)

    @bot.message_handler(func=lambda f: message.chat.id == ADM_ID)
    def send_dt(m):
        dtp = m.text
        date = open('tx_n.txt', 'w')
        date.write(dtp)
        date.close()
        bot.send_message(constants.chat_r_id, dtp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню Ред. Новий учасник - кнопка 📨 Повідомити ---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_n_sms)
def button_sd(message):
    bot.send_message(message.chat.id, text.id_zam)

    @bot.message_handler(func=lambda d: message.chat.id == ADM_ID)
    def send_sms(m):
        h = open('n_status.txt', 'r')
        ztx = h.read()
        h.close()
        sd = m.text
        message.chat.id = sd
        bot.send_message(message.chat.id, text.tx_sms_n + ztx)
        bot.send_message(constants.chat_r_id, text.tx_sms_n + ztx)
        message.chat.id = 0
# Кнопка 🔕 Ред. Анти спам--РЕДАКТОР------------------------------------------------------->>>>>>>>>>>>>>>>>>>>


@bot.message_handler(func=lambda message: message.text == text.tx_s_red)
def button_new(message):
    h = open('s_seven_days.txt', 'r')
    ntx = h.read()
    h.close()
    kzr = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    b_n_yes = types.InlineKeyboardButton(text=text.tx_s_on)
    b_n_no = types.InlineKeyboardButton(text=text.tx_s_off)
    b_n_pr = types.InlineKeyboardButton(text=text.tx_s_rpr)
    b_n_rp = types.InlineKeyboardButton(text=text.tx_s_rp)
    b_s_rp = types.InlineKeyboardButton(text=text.tx_s_sms)
    b_z_nd = types.InlineKeyboardButton(text=text.text_but_nz)
    kzr.add(b_n_yes, b_n_no, b_n_pr, b_n_rp, b_s_rp, b_z_nd)
    bot.send_message(message.chat.id, text.inf_red + text.ps_pr + ntx + text.sev_d, reply_markup=kzr)
# Меню ред.Анти спам - кнопка  🔛 Свободно(🔕)-----------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_s_on)
def button_sd(message):
    global sp
    sp = 1
    h = open('s_status.txt', 'w')
    h.write('+')
    h.close()
    h = open('tx_s.txt', 'w')
    h.write(str(text.no_rek))
    h.close()
    bot.send_message(message.chat.id, text.info_save)
# Меню ред.Анти спам - кнопка 🔚 Занято(🔕))-----------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_s_off)
def button_sd(message):
    h = open('s_status.txt', 'w')
    h.write('-')
    h.close()
    bot.send_message(message.chat.id, text.inf_date)

    @bot.message_handler(func=lambda f: message.chat.id == ADM_ID)
    def send_dt(m):
        dtp = m.text
        date = open('s_status.txt', 'a')
        date.write('\n' + dtp)
        date.close()
        bot.send_message(constants.chat_r_id, dtp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню ред.Анти спам - кнопка 📈 Ред. цену(🔕)---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_s_rpr)
def button_one(message):
    bot.send_message(message.chat.id, text.pr_sev_v)

    @bot.message_handler(func=lambda pr: message.chat.id == ADM_ID)
    def send_dt(m):
        dp = m.text
        dte = open('s_seven_days.txt', 'w')
        dte.write(dp)
        dte.close()
        bot.send_message(constants.chat_r_id, dp + text.sev_d)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0


# Меню ред Анти спам - кнопка 🚀 Доб.пост(🔕)---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_s_rp)
def button_n(message):
    h = open('tx_s.txt', 'r')
    ntx = h.read()
    h.close()
    bot.send_message(message.chat.id, text.rek_post + ntx)
    bot.send_message(message.chat.id, text.new_tx)

    @bot.message_handler(func=lambda f: message.chat.id == ADM_ID)
    def send_dt(m):
        dtp = m.text
        date = open('tx_s.txt', 'w')
        date.write(dtp)
        date.close()
        bot.send_message(constants.chat_r_id, dtp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню Ред. Анти спам - кнопка 🚀 📨 Повідомити ---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_s_sms)
def button_sd(message):
    bot.send_message(message.chat.id, text.id_zam)

    @bot.message_handler(func=lambda d: message.chat.id == ADM_ID)
    def send_sms(m):
        h = open('s_status.txt', 'r')
        ztx = h.read()
        h.close()
        sd = m.text
        message.chat.id = sd
        bot.send_message(message.chat.id, text.tx_sms_s + ztx)
        bot.send_message(constants.chat_r_id, text.tx_sms_s + ztx)
        message.chat.id = 0
# Кнопка 👁 Ред. 1.000--РЕДАКТОР------------------------------------------------------>>>>>>>>>>>>>


@bot.message_handler(func=lambda message: message.text == text.tx_1_red)
def button_new(message):
    h = open('pr_1000.txt', 'r')
    ntx = h.read()
    h.close()
    kzr = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    b_n_yes = types.InlineKeyboardButton(text=text.tx_1_on)
    b_n_no = types.InlineKeyboardButton(text=text.tx_1_off)
    b_n_pr = types.InlineKeyboardButton(text=text.tx_1_rpr)
    b_sms_pr = types.InlineKeyboardButton(text=text.tx_1_sms)
    b_z_nd = types.InlineKeyboardButton(text=text.text_but_nz)
    kzr.add(b_n_yes, b_n_no, b_n_pr, b_sms_pr, b_z_nd)
    bot.send_message(message.chat.id, text.inf_red + text.ps_pr + ntx + text.tx_1, reply_markup=kzr)
# Меню ред.👁 Ред. 1.000 - кнопка  🔛 Свободно(👁)-----------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_1_on)
def button_sd(message):
    global p1
    p1 = 1
    h = open('1_status.txt', 'w')
    h.write('+')
    h.close()
    bot.send_message(message.chat.id, text.info_save)
    message.chat.id = 0
# Меню ред.👁 Ред. 1.000 - кнопка 🔚 Занято(👁)-----------------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_1_off)
def button_sd(message):
    h = open('1_status.txt', 'w')
    h.write('-')
    h.close()
    bot.send_message(message.chat.id, text.info_save)
    message.chat.id = 0
# Меню ред.👁 Ред. 1.000 - кнопка 📈 Ред. цену(👁)---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_1_rpr)
def button_one(message):
    bot.send_message(message.chat.id, text.pr_1000)

    @bot.message_handler(func=lambda pr: message.chat.id == ADM_ID)
    def send_dt(m):
        dtp = m.text
        date = open('pr_1000.txt', 'w')
        date.write(dtp)
        date.close()
        bot.send_message(constants.chat_r_id, dtp)
        bot.send_message(message.chat.id, text.info_save)
        message.chat.id = 0
# Меню Ред. 👁 Ред. 1.000 📨 Повідомити ---------------------------------------------


@bot.message_handler(func=lambda message: message.text == text.tx_1_sms)
def button_sd(message):
    bot.send_message(message.chat.id, text.id_zam)

    @bot.message_handler(func=lambda d: message.chat.id == ADM_ID)
    def send_sms(m):
        message.chat.id = m.text
        bot.send_message(message.chat.id, text.tx_sms_p1)
        bot.send_message(constants.chat_r_id, text.tx_sms_p1)
        message.chat.id = 0
# Кнопка Відповісти довільна форма------------------------------------------------------>>>>>>>>>>>>>


@bot.message_handler(func=lambda message: message.text == text.text_but_vid)
def button_new(message):
    kzr = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    b_vp_id = types.InlineKeyboardButton(text=text.id_otr)
    b_vp_sms = types.InlineKeyboardButton(text=text.sms_zagal)
    b_vp_cl = types.InlineKeyboardButton(text=text.cl_zag)
    b_z_nd = types.InlineKeyboardButton(text=text.text_but_nz)
    kzr.add(b_vp_id, b_vp_sms, b_vp_cl, b_z_nd)
    bot.send_message(message.chat.id, text.vdp_zag, reply_markup=kzr)
# ID вводимо кому пишемо-------------------------
@bot.message_handler(func=lambda message: message.text == text.sms_zagal)
def button_sd(message):
    bot.send_message(message.chat.id, text.ent_tx)

    @bot.message_handler(func=lambda d: message.chat.id == ADM_ID)
    def send_sms(m):
        h = open('tx_id_sms.txt', 'r')
        vp = h.read()
        h.close()
        sms = m.text
        bot.send_message(vp, sms)
        message.chat.id = 0


@bot.message_handler(func=lambda message: message.text == text.id_otr)
def button_sd(message):
    bot.send_message(message.chat.id, text.id_zam)

    @bot.message_handler(func=lambda d: message.chat.id == ADM_ID)
    def send_sms(m):
        vp = m.text
        h = open('tx_id_sms.txt', 'w')
        h.write(str(vp))
        h.close()
        bot.send_message(constants.chat_r_id, text.st_ok)
        message.chat.id = 0


@bot.message_handler(func=lambda message: message.text == text.cl_zag)
def button_sd(message):
    h = open('tx_id_sms.txt', 'w')
    h.write(str(0))
    h.close()
    bot.send_message(message.chat.id, text.inf_cl)
    message.chat.id = 0


bot.polling(none_stop=True, interval=1)
