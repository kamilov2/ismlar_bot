import telebot
from telebot import types
from db import get_data_from_db,search_meaning_name

API_TOKEN = '5522911584:AAGVbmrya8r_U_paRbQRn0rrpnjfVnvjtvw'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start', 'names'])
def send_welcome(message):
    button_a = types.InlineKeyboardButton(text="a", callback_data="A")
    button_b = types.InlineKeyboardButton(text="b", callback_data="B")
    button_c = types.InlineKeyboardButton(text="c", callback_data="C")
    button_d = types.InlineKeyboardButton(text="d", callback_data="D")
    button_e = types.InlineKeyboardButton(text="e", callback_data="E")
    button_f = types.InlineKeyboardButton(text="f", callback_data="F")
    button_g = types.InlineKeyboardButton(text="g", callback_data="G")
    button_h = types.InlineKeyboardButton(text="h", callback_data="H")
    button_i = types.InlineKeyboardButton(text="i", callback_data="I")
    button_j = types.InlineKeyboardButton(text="j", callback_data="J")
    button_k = types.InlineKeyboardButton(text="k", callback_data="K")
    button_l = types.InlineKeyboardButton(text="l", callback_data="L")
    button_m = types.InlineKeyboardButton(text="m", callback_data="M")
    button_n = types.InlineKeyboardButton(text="n", callback_data="N")
    button_o = types.InlineKeyboardButton(text="o", callback_data="O")
    button_p = types.InlineKeyboardButton(text="p", callback_data="P")
    button_q = types.InlineKeyboardButton(text="q", callback_data="Q")
    button_r = types.InlineKeyboardButton(text="r", callback_data="R")
    button_s = types.InlineKeyboardButton(text="s", callback_data="S")
    button_t = types.InlineKeyboardButton(text="t", callback_data="T")
    button_u = types.InlineKeyboardButton(text="u", callback_data="U")
    button_v = types.InlineKeyboardButton(text="v", callback_data="V")
    button_w = types.InlineKeyboardButton(text="w", callback_data="W")
    button_x = types.InlineKeyboardButton(text="x", callback_data="X")
    button_y = types.InlineKeyboardButton(text="y", callback_data="Y")
    button_z = types.InlineKeyboardButton(text="z", callback_data="Z")

    # Sozdanie razmeshchennogo knopok bloka
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.row(button_a, button_b, button_c, button_d, button_e)
    inline_keyboard.row(button_f, button_g, button_h, button_i, button_j)
    inline_keyboard.row(button_k, button_l, button_m, button_n, button_o)
    inline_keyboard.row(button_p, button_q, button_r, button_s, button_t)
    inline_keyboard.row(button_u, button_v, button_w, button_x, button_y, button_z)

    bot.reply_to(message, """\
        Salom. Nima gap ?!Men ismlarni ma'nolari bilan ulashadigan botman !Harfni tanlasangiz ismlarni tashlayman !""", reply_markup=inline_keyboard)

buttons = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower(),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    button_a = types.InlineKeyboardButton(text="a", callback_data="A")
    button_b = types.InlineKeyboardButton(text="b", callback_data="B")
    button_c = types.InlineKeyboardButton(text="c", callback_data="C")
    button_d = types.InlineKeyboardButton(text="d", callback_data="D")
    button_e = types.InlineKeyboardButton(text="e", callback_data="E")
    button_f = types.InlineKeyboardButton(text="f", callback_data="F")
    button_g = types.InlineKeyboardButton(text="g", callback_data="G")
    button_h = types.InlineKeyboardButton(text="h", callback_data="H")
    button_i = types.InlineKeyboardButton(text="i", callback_data="I")
    button_j = types.InlineKeyboardButton(text="j", callback_data="J")
    button_k = types.InlineKeyboardButton(text="k", callback_data="K")
    button_l = types.InlineKeyboardButton(text="l", callback_data="L")
    button_m = types.InlineKeyboardButton(text="m", callback_data="M")
    button_n = types.InlineKeyboardButton(text="n", callback_data="N")
    button_o = types.InlineKeyboardButton(text="o", callback_data="O")
    button_p = types.InlineKeyboardButton(text="p", callback_data="P")
    button_q = types.InlineKeyboardButton(text="q", callback_data="Q")
    button_r = types.InlineKeyboardButton(text="r", callback_data="R")
    button_s = types.InlineKeyboardButton(text="s", callback_data="S")
    button_t = types.InlineKeyboardButton(text="t", callback_data="T")
    button_u = types.InlineKeyboardButton(text="u", callback_data="U")
    button_v = types.InlineKeyboardButton(text="v", callback_data="V")
    button_w = types.InlineKeyboardButton(text="w", callback_data="W")
    button_x = types.InlineKeyboardButton(text="x", callback_data="X")
    button_y = types.InlineKeyboardButton(text="y", callback_data="Y")
    button_z = types.InlineKeyboardButton(text="z", callback_data="Z")

    # Sozdanie razmeshchennogo knopok bloka
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.row(button_a, button_b, button_c, button_d, button_e)
    inline_keyboard.row(button_f, button_g, button_h, button_i, button_j)
    inline_keyboard.row(button_k, button_l, button_m, button_n, button_o)
    inline_keyboard.row(button_p, button_q, button_r, button_s, button_t)
    inline_keyboard.row(button_u, button_v, button_w, button_x, button_y, button_z)
    meaning = search_meaning_name(message.text)
    print(meaning)
    if meaning:
        bot.reply_to(message,f"<b>{meaning[0][0]}</b>\n<blockquote>{meaning[0][1]}</blockquote>",parse_mode="HTML")
    else:
        bot.reply_to(message,"Bu ism haqida men bilmayman !")


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    callback_data = call.data
    names = get_data_from_db(callback_data)
    for name,desc in names:
        bot.send_message(call.message.chat.id, f"<b>{name}</b>\n<blockquote>{desc}</blockquote>", parse_mode="HTML")



bot.infinity_polling()