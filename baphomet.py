## BAPHOMET BOT , tora bible codes , jeremiah edition 0.1
import modules.imports as i
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,ConversationHandler)


import modules.config as config

import modules.msg as msg
import modules.files as files
import modules.txt as txt2
import logging


import os.path
from os import path
import os as os
## MAIN SOURCE

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


logger = logging.getLogger(__name__)


START  = range(1)

def menu(update, context):
        chatid=0
        #print (update)
        try:
            user = update.message.from_user

            ##LOGGING DEBUG
            print (user)
            print (user.id)
            print(update.message.chat.id)
        except:
            pass

        btdat=""
        try:
            query = update.callback_query
            query.answer()
            btdat=query.data
            try:
                chatid=btdat.split(" ")[1]
            except:
                pass
        except:
            pass
        txt=""
        try:
            chatid = update.message.chat.id 
            txt = update.message.text
            print(txt)
            

        except:
            pass
        
        
        try:
            # TEXT
            files.save_txt("datos/"+str(chatid)+"/"+user.first_name+".userdata",str(user),chatid)
            files.save_txt("datos/"+str(chatid)+"/"+user.first_name+".log", "\n\n"+txt,chatid) 
        except:
            pass



        ## LOAD MODULES
        if "None" !=str(txt):
        
#            identity.load(chatid,txt,btdat)


        return (range(1))

def cancel(update, context):
    user = update.message.from_user
    logger.info("The user %s stops conversations.", user.first_name)
    update.message.reply_text('See you soon.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def nada() :
    return ""



def main():
    ## main process
    updater = Updater(config.TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', menu)],

        states={
            START: [MessageHandler(Filters.regex('.') | Filters.location | Filters.photo, menu)]
        },fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(CallbackQueryHandler(menu))
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()



def is_validated(chatid):
    #check if user has been validated

    return (path.exists("datos/"+str(chatid)+"/mrcert_"+chatid+".pem"))




def mainload(chatid,txt,btdat,update):


      if ""=="" :
            if "/ayuda_bot" in txt or "/ayuda_bot" in btdat:
                print(update.message)
                update.message.reply_text(
                    'Baphomet Bot\n\n'
                    '/search \n\n'
                    '/searchnum \n\n'
                    '/talk sentence \n\n'
                    '/help \n\n'
                    '/start \n\n'
                    )

            if "/restart" == txt or "/restart" in btdat or "/start" in txt:

              #  reply_keyboard = [['/ayuda_emergencia'],["/diagnostico_rapido"],["/ayuda_economica"],["/ayuda_bot"]]

                keyboard = [[InlineKeyboardButton("Search", callback_data='/search '+str(chatid)),
                    InlineKeyboardButton("searchnum", callback_data='/searchnum '+str(chatid))],                    [InlineKeyboardButton("Talk", callback_data='/talk '+str(chatid))],[InlineKeyboardButton("Help", callback_data='/help '+str(chatid))]]
                
                reply_markup = InlineKeyboardMarkup(keyboard)
                print(update)
                check_new_user(update.message.chat.first_name,chatid)
                
                update.message.reply_text(
                    txt2.inicio+"\n\n"+txt2.presentacion,
                    reply_markup=reply_markup, one_time_keyboard=True)

                return (range(1)) 
                

            if "/search" in txt or "/search" in btdat:
                
                pndg = validate_register(chatid)
                if pndg==True:
                    msg.sendmsg(chatid,txt2.finalizar_kyc,False)
                else:
                    msg.sendmsg(chatid,txt2.pending+"\n\n"+pndg,False)


            if "/searchnum" in txt or "/video" in btdat:

                s = files.get_random("modules/asimov_sentences.db")

                msg.sendmsg(chatid,txt2.challange+"\n\n"+s+" \n\n Isaac Asimov . Escritor.",False)


            if "/talk" in txt or "/talk" in btdat or "/talk" in btdat or "talk" in btdat:
                msg.sendmsg(chatid,txt2.registro_enfermos,False)
                
                keyboard = [[InlineKeyboardButton("Envía tu foto", callback_data='/foto '+str(chatid))],[InlineKeyboardButton("Envía tu localización", callback_data='/localizacion '+str(chatid))],[InlineKeyboardButton("Video", callback_data='/video '+str(chatid))],[InlineKeyboardButton("Foto Cédula", callback_data="/cedula "+str(chatid))],[InlineKeyboardButton("Comparte Robot",callback_data="/robot "+str(chatid) )],[InlineKeyboardButton("Finalizar", callback_data='/finalizar_kyc '+str(chatid))]]
               
                reply_markup = InlineKeyboardMarkup(keyboard)

                msg.sendmsg(chatid,"Seleccione una opción",reply_markup)




            if "/cancel" in txt:
                #os.popen("killall ")
                update.message.reply_text("Servico parado")
                

            return range(1)

      else:
        update.message.reply_text("Not Allow")




