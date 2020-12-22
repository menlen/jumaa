import os, sys
from PIL import Image, ImageDraw, ImageFont
import random, time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types

TELEGRAM_TOKEN = '1466961621:AAEuwZEqVnIA3PrnOe4hDzcDuZm2FXQcJF0'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

channelId = -1001390673326
user_dict = {}
msgDict = [
    'اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ.\nАллоҳумма солли ъалаа муҳаммадив-ва ъалаа аали муҳаммад.',
    'صَلَّى اللهُ عَلَى مُحَمَّدٍ.\nСоллаллоҳу ъалаа муҳаммад.',
    'صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ.\nСоллаллоҳу ъалайҳи ва саллам.',
    'أَللَّهُمَّ صَلِّ وَسَلِّمْ وَبَارِكْ عَلَيْهِ.\nАллоҳумма солли ва саллим ва баарик ъалайҳ.',
    'اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِهِ وَسَلِّمْ.\nАллоҳумма солли ъалаа муҳаммадив-ва ъалаа аалиҳий ва саллим.',
    'صَلَّى اللهُ وَسَلَّمَ عَلَى نَبِيِّنَا مُحَمَّدٍ وَعَلَى آلِهِ وَأَصْحَابِهِ أَجْمَعِينَ.\nСоллаллоҳу ва саллама ъалаа набиййинаа муҳаммад, ва ъалаа аалиҳий ва асҳаабиҳий ажмаъийн.'
]
msgOne = random.choice(msgDict)

def UImgTextWriter(ext):
    IMAGES = [
        'juma01.jpg',
        'juma02.jpg',
        'juma03.jpg',
        'juma04.jpg',
        'juma05.jpg',
        'juma06.jpg',
        'juma07.jpg',
        'juma08.jpg',
        'juma09.jpg',
        'juma010.jpg',
        'juma011.jpg',
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
    
    filename = random.randint(30,45)
    g = out.save(f'{filename}.png')
    return filename

def ImgTextWriter(ext):
    IMAGES = [
        'juma1.jpg',
        'juma2.jpg',
        'juma3.jpg',
        'juma4.jpg',
        'juma5.jpg',
        'juma6.jpg',
        'juma7.jpg',
        'juma8.jpg',
        'juma9.jpg',
        'juma10.jpg',
        'juma11.jpg',
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
    
    filename = random.randint(1,15)
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
            \nSizni Sayyid-ul Ayyom bilan qutlayman🌙\n{msgOne}\
            \nO'zingiz yaxshi ko'rgan, jannatda xam birga bo'lishni istagan insonlaringizni O'z ismimlari bilan tabriklang. \n@JumaTabriklarbot"
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_uname_step(message):
    try:
        name = message.text
        name = name.upper()
        myfile = UImgTextWriter(name)
        photoSend = open(f'{myfile}.png', 'rb')
        caption = f"Juma Ayyom muborak aziz dindoshlarim🕌🌙\
            \nSizni Sayyid-ul Ayyom bilan qutlayman🌙,\n{msgOne}\
            \nO'zingiz yaxshi ko'rgan, jannatda xam birga bo'lishni istagan insonlaringizga yuboring \n@JumaTabriklarbot"
        bot.send_photo(message.chat.id, photoSend, caption=caption)
    except Exception as e:
        bot.reply_to(message, 'oooops')


@bot.message_handler(commands=['start','help'])
def start(message):
    us = getUserFromChannel(message.chat.id)
    if us == 'member':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Do'stimga")
        btn2 = types.KeyboardButton("O'zimga")
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id, "Assalomu Aleykum Do'stim", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}, Kanalimizga a'zo bo'ling va A'zolikni tekshirish buyrug'ini tasdiqlang", reply_markup=gen_markup())


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    us = getUserFromChannel(message.chat.id)
    if us == 'member':
        msg = bot.send_message(message.chat.id, """\
                Juda soz!!!, Do'stingizni ismini yozing. \nYoki /start /help ni bosing
                """)
        if message.text == "Do'stimga":
            bot.register_next_step_handler(msg, process_name_step)
        elif message.text == "O'zimga":
            bot.register_next_step_handler(msg, process_uname_step)
    else:
        bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}, kanallarga a'zo bo'ling va A'zolikni tekshirish buyrug'ini tanlang", reply_markup=gen_markup())


bot.polling(none_stop=True)
