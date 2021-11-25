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
            

            ## Check images and location

            locate = update.message.location
            if "None" == str(txt) and str(locate)=="None":
        
                ## check photos
                fa=files.photo(update,context)
                
                ## check faces in photos
                fa=files.faces("datos/"+str(chatid)+"/tmp.jpg")

                if fa == 2 or fa == 1:
                    msg.sendmsg(chatid,txt2.photo,False)
                    os.system("cp datos/"+str(chatid)+"/tmp.jpg datos/"+str(chatid)+"/selfie.jpg")

                if fa == 0:
                    msg.sendmsg(chatid,txt2.photo_no,False)

                if fa > 2:
                    msg.sendmsg(chatid,txt2.photo_mas,False)
                
                imst = str(files.imgstr("datos/"+str(chatid)+"/tmp.jpg")).strip()
                print("-"+imst+"-") 
                #print(files.metadata("datos/"+str(chainid)+"/tmp.jpg"))

                if imst !=str("") and fa==2 or fa==1:
                    msg.sendmsg(chatid,txt2.correcto+"\n\n"+str(imst),False)
                    os.system("cp datos/"+str(chatid)+"/tmp.jpg datos/"+str(chatid)+"/cedulaA.jpg")
                    os.system("cp datos/"+str(chatid)+"/tmp.jpg datos/"+str(chatid)+"/cedulaB.jpg")


            if str("None") == str(txt) and str(locate)!=str("None"):
                print ("Locate "+str(locate))
                files.save_txt("datos/"+str(chatid)+"/locate.db",str(locate),chatid) 
                msg.sendmsg(chatid,txt2.localizacion,False)
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
        
            emergencias.load(chatid,txt,btdat,update)
        
        
            municipio.load(chatid,txt,btdat)
        
        
            economicas.load(chatid,txt,btdat)
        
        
            sanidad.load(chatid,txt,btdat,update)
        
            mainload(chatid,txt,btdat,update)

            pay.load(chatid,txt,btdat)

            identity.load(chatid,txt,btdat)


        return (range(1))

def cancel(update, context):
    user = update.message.from_user
    logger.info("El usuario %s canceló la conversación.", user.first_name)
    update.message.reply_text('Nos vemos pronto.',
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


def validate_register(chatid):
    ## check
    ## cedula cara A, face & data
    ## cedula cara B, data
    ## localizacion, localizacion
    ## Selfie , face
    ## Video , time,and face
    userpath="datos/"+str(chatid)+"/"
    cedulaA=path.exists(userpath+"cedulaA.jpg")
    cedulaB=path.exists(userpath+"cedulaB.jpg")
    selfie =path.exists(userpath+"selfie.jpg")
    loca = path.exists(userpath+'locate.db')
    #videoface = path.exists(userpath+'videoface.mkv')

    listcheck = [("Cédula cara A",cedulaA),("Cédula cara B",cedulaB),("Selfie",selfie),("Localización",loca)]

    if cedulaA==True and cedulaB==True and selfie==True and loca==True:

        return True
    
    else:
        pending=""
        for (x,y) in listcheck:
            if y != True:
                pending+=x+"\n\n"
        print (pending)
        return pending

def check_new_user(fstname,chatid):
    
    pchk = path.exists("datos/"+str(chatid)+"/"+str(fstname)+".bonosolidario.balance")
    userpath="datos/"+str(chatid)+"/"
    if pchk != True:
        try:
            os.mkdir("datos/"+str(chatid))
        except OSError:
            pass
        
        files.save_txt(userpath+fstname+".bonosolidario.balance","0",chatid)
        files.save_txt(userpath+fstname+".monedero.balance","0",chatid)
        #files.save_txt(userpath+fstname+".municipio.balance","0",chatid)
        #files.save_txt(userpath+fstname+".parking.balance","0",chatid)



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




