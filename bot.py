import os, sys
from PIL import Image, ImageDraw, ImageFont
import random, time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = '1466961621:AAEuwZEqVnIA3PrnOe4hDzcDuZm2FXQcJF0'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

channelId = -1001390673326
user_dict = {}


def ImgTextWriter(ext):
    IMAGES = [
        'juma1.jpg',
        'juma2.jpg',
        'juma3.jpg',
        'juma4.jpg',
        'juma5.jpg',
        'juma6.jpg',
        'juma7.jpg'
    ]
    try:
        img = random.choice(IMAGES)
    except:
        time.sleep(2)
        img = random.choice(IMAGES)
    # get an image
    base = Image.open(img).convert("RGBA")
    ext = ext.upper()
    text = ext
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255,255,255,0))
    # get a font
    fnt = ImageFont.truetype("OpenSans-Italic.ttf", 40)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(((800)/4, 330), text, font=fnt, fill=(231,195,113,255), anchor='mb')

    out = Image.alpha_composite(base, txt)
    
    filename = random.randint(1,20)
    g = out.save(f'{filename}.png')
    return filename

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Azo bo'ling", callback_data="cb_yes", url='t.me/onideal'),
                               InlineKeyboardButton("Tasdiqlash", callback_data="cb_no"))
    return markup

def getUserFromChannel(userId):
    u = bot.get_chat_member(channelId, userId)
    return u.status

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_no":
        u = getUserFromChannel(call.from_user.id)
        if u == 'member':
            msg = bot.send_message(call.from_user.id, """\
            Juda soz!!!, Do'stingizni ismini yozing
            """)
            bot.register_next_step_handler(msg, process_name_step)
        else:
            bot.send_message(call.from_user.id, f"Salom {call.from_user.first_name}, Kanalimizga a'zo bo'ling va A'zolikni tekshirish buyrug'ini tanlang", reply_markup=gen_markup())

def process_name_step(message):
    try:
        name = message.text
        name = name.upper()
        myfile = ImgTextWriter(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f"{name} : Juma Ayyom muborak aziz dindoshim🕌🌙\
            \nSizni Sayyid-ul Ayyom bilan qutlayman🌙\
            \n@onideal // @JumaTabriklarbot"
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    us = getUserFromChannel(message.chat.id)

    if us == 'member':
        msg = bot.send_message(message.chat.id, """\
                Juda soz!!!, Do'stingizni ismini yozing
                """)
        bot.register_next_step_handler(msg, process_name_step)
    else:
        bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}, kanallarga a'zo bo'ling va A'zolikni tekshirish buyrug'ini tanlang", reply_markup=gen_markup())


bot.polling(none_stop=True)
