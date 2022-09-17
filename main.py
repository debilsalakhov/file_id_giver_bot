import telebot
import pandas as pd
import SECRET


bot = telebot.TeleBot(SECRET.BOT_TOKEN)  # @file_id_giver_bot


def append_table_csv(file_id: str, type: str):
    df = pd.read_csv('file_id_table.csv')
    df.loc[-1, ['file_id']] = file_id
    df.loc[-1, ['type']] = type
    df.to_csv('file_id_table.csv', index=False)


# ---------------------------------------
@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    txt_message = 'Привет. Пришли мне файл, и я дам тебе его file_id.'
    bot.send_message(chat_id, text=txt_message)


# ---------------------------------------
@bot.message_handler(content_types=['photo'])
def give_file_id(message):
    chat_id = message.chat.id
    append_table_csv(message.photo[2].file_id, 'photo')
    bot.send_message(chat_id, text=message.photo[2].file_id)


# ---------------------------------------
@bot.message_handler(content_types=['video'])
def give_file_id(message):
    chat_id = message.chat.id
    append_table_csv(message.video.file_id, 'video')
    bot.send_message(chat_id, text=message.video.file_id)


# ---------------------------------------
@bot.message_handler(content_types=['sticker'])
def give_file_id(message):
    chat_id = message.chat.id
    append_table_csv(message.sticker.file_id, 'sticker')
    bot.send_message(chat_id, text=message.sticker.file_id)


# ---------------------------------------
@bot.message_handler(content_types=['document'])
def give_file_id(message):
    chat_id = message.chat.id
    append_table_csv(message.document.file_id, 'document')
    bot.send_message(chat_id, text=message.document.file_id)


# ---------------------------------------
@bot.message_handler(content_types=['audio'])
def give_file_id(message):
    chat_id = message.chat.id
    append_table_csv(message.audio.file_id, 'audio')
    bot.send_message(chat_id, text=message.audio.file_id)


# ---------------------------------------


bot.polling(none_stop=True, interval=0)
