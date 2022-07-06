import telebot
from base import db_add,cursor

bot = telebot.TeleBot("5518859686:AAGbauZZ8cwN7kWD2e3NiV6I6dh51S8mmbg")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id,"Привет, " + message.from_user.first_name + ", я - помощник Аскара,отправь мне сообщение и укажи ник того,кто это сообщение должен получить (Первое сообщение-username человека, второе сообщение - сообщение для пользователя) Для продолжения напиши continue ")

@bot.message_handler(commands=['help'])
def send_info(message):
    bot.send_message(message.from_user.id,"Я - помощник Аскара,отправь мне сообщение и укажи ник того,кто это сообщение должен получить (Первое сообщение-username человека, второе сообщение - сообщение для пользователя) Для продолжения напиши continue ")

@bot.message_handler(content_types = ['text'])
def get_text_message(message):
    if message.text == "continue":
        username = bot.send_message(message.chat.id,'Введите username')
        bot.register_next_step_handler(username,first_step)

    else:
        bot.send_message(message.from_user.id,"Хей!, напиши /help для того, чтобы я тебе рассказал о себе")



def first_step(message):
    global answers
    answers = []

    username = message.text
    answers.append(username)

    user_message = bot.send_message(message.chat.id, 'Введите сообщение')
    bot.register_next_step_handler(user_message, second_step)

def second_step(message):
    user_message = message.text
    answers.append(user_message)

    us_id = message.from_user.id
    username_sender =  message.from_user.username

    db_add(user_id = us_id ,username_sender= username_sender , username =  answers[0] , user_message = answers[1])

    bot.send_message(chat_id=-638707590,text="hello,world!")

    rowid = cursor.lastrowid

    cursor.execute("""SELECT * FROM requests WHERE id = ? """,(rowid, ))

    result = cursor.fetchone()

    bot.send_message(chat_id=-638707590,text="@" + result[3] + " " + result[4])




bot.polling(none_stop=True, interval=0)


