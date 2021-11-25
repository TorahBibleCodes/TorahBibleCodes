import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,ConversationHandler)
import modules.config as config
import modules.files as files

def sendmsg(chatid,msg,btns):

    sendmsg_internal(chatid,msg,btns)
    sendmsg_internal(config.chat_id["admin"],"Mensage a chatid :"+str(chatid)+" NickName:  "+files.get_username(chatid)+" \n\n"+msg,btns)

def sendmsg_internal(chatid,msg,btns):
    bot = telegram.Bot(config.TOKEN)
    if btns==False:
        bot.send_message(chat_id=chatid, text=msg)
    else:
        bot.send_message(chat_id=chatid, text=msg,reply_markup=btns)
