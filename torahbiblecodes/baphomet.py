## BAPHOMET BOT , tora bible codes , jeremiah edition 0.1
import modules.resources.imports as i
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,ConversationHandler)
import threading, time
from queue import Queue
#import resources.func.functions as torah
from resources.func.torah import *
#import modules.resources.xgboost as xgb
import modules.resources.config as config
from resources.func.thread import *
import modules.resources.msg as msg
import modules.resources.txt as txt2
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

#langin = 'en'
langout = 'en'
ptrans = 'true'
threads = 10
tracert = 'false'

torah = Torah()
jobstrans = Jobs()
books.load()
msgqueue = {}

def predict(arrayIn):
    xgb.predict(arrayIn)


def ttranslator():
    global langout, ptrans, totalvalue, tracert, totalresult, jobstrans, msgqueue

    while True:#not jobstrans.empty():
        #print('\nFound', int(jobstrans.queue.qsize()))
        tchunk = jobstrans.get()
        tchunk = tchunk.split('*')
        dchunk = tchunk[0]
        n = 2000
        text_chunk = [dchunk[i:i+n] for i in range(0, len(dchunk), n)]
        lenchunk = len(text_chunk)
        text_trans = ''
        nch = 0
        chatid = int(tchunk[2])
        langOut = tchunk[3]
        print(chatid)
        try:
            #print(GREEN, 'chunk size: ', lenchunk, END)
            #print('\nBook:',tchunk[1])
            for chunks in range(0, lenchunk):
                #print(ORANGE + chunks + END+ '\n')
                nch = nch +1
                #jobstrans.add(dchunk[chunks]+'*'+value)
                #print(BLUE, 'n', str(nch), END, 'chunk', text_chunk[chunks])
                rett = torah.func_translate('iw', langOut, text_chunk[chunks])
                retp = torah.func_ParseTranslation(rett,langOut, ptrans)
                #retp = text_chunk[chunks]
                if not retp == 0 and not retp == '': 
                    text_trans = str(text_trans) + str(retp)
                    #totalresult = totalresult+1
            #print('\nBook:',tchunk[1])
                    #print('\nn',nch)
                    print(ORANGE + str(retp) + END)
            print(GREEN + str(text_trans) + END+'\n')
           # print(BLUE + str(text_chunk[chunks]) + END)
            if not retp == 0:
                #print(retp)
                AS=''
                msgqueue[chatid] = msgqueue[chatid] + '\n' +str(text_trans)
            jobstrans.done()
        except Exception as e:
            print('ee t')
            print(e)
            jobstrans.done()
            pass


def searchAll(q, number, chatid, langOut):
    global langout, ptrans, msgqueue, jobstrans
    #if not q.empty():
    #print('init '+ str(number))
    #print(langOut)
    retp = ''
    while not q.empty():
        try:
            value = q.get()
            ret, tvalue = torah.els(value, number, tracert=tracert)


            jobstrans.add(str(ret)+'*'+value+'*'+str(chatid)+'*'+str(langOut))
            jobstrans.join()
            q.task_done()

            #dchunk = ret
            #n = 2000
            #text_chunk = [dchunk[i:i+n] for i in range(0, len(dchunk), n)]
            #lenchunk = len(ret)
            #print(lenchunk)
            
            #rett = torah.func_translate('iw', langOut, ret)
           # retp = torah.func_ParseTranslation(rett,langOut, ptrans)
            #print(retp)
            #if not retp == 0:
                #print(retp)
            #    msgqueue[chatid] = msgqueue[chatid] + '\n' +retp
            #    q.task_done()
            #else:
            #    q.task_done()
        except Exception as e:
            print('ERROR:', e)
            q.task_done()
            pass

def search(text, chatid, update):
    global langout, threads, msgqueue
    jobs = Queue()
    msgqueue[chatid] = ''
    listform = ''
    user = update.message.from_user
    langin = user['language_code']
    print(langin)
    options = text.split(' ')
    
    if len(options) > 1:
        for string in options:
            listform = listform+' '+string
        if langin == 'iw':
            sed = gematria_to_int(listform)
        else:
            sed = torah.gematrix(listform)
    else:
        #print(options[0])
        if langin == 'iw':
            sed = gematria_to_int(u''+options[0].strip())
        else:
            sed = torah.gematria(options[0].strip())

    for i in books.booklist():
        jobs.put(i)

    for i in range(int(threads)):
        worker = threading.Thread(target=searchAll, args=(jobs, sed, chatid, langin,))
        worker.start()

    print("waiting for ", str(jobs.qsize())+'/43', "tasks")
    jobs.join()
    if not msgqueue[chatid] == '':
        dchunk = msgqueue[chatid]
        n = 3000

        text_chunk = [dchunk[i:i+n] for i in range(0, len(dchunk), n)]
        lenchunk = len(text_chunk)
        for chunks in range(0, lenchunk):
            msg.sendmsg(chatid,text_chunk[chunks]+"\n\n",False, update)
    print('Done.')
    msg.sendmsg(chatid,'Done.'+"\n\n",False, update)

def searchnumber(number,chatid, update):
    global jobs, langout, threads, msgqueue
    jobs = Queue()
    msgqueue[chatid] = ''
    user = update.message.from_user
    langin = user['language_code']
    for i in books.booklist():
        jobs.put(i)

    for i in range(int(threads)):
        worker = threading.Thread(target=searchAll, args=(jobs, number, chatid, langin,))
        worker.start()

    print("waiting for ", str(jobs.qsize())+'/43', "tasks")
    jobs.join()
    if not msgqueue[chatid] == '':
        dchunk = msgqueue[chatid]
        n = 3000

        text_chunk = [dchunk[i:i+n] for i in range(0, len(dchunk), n)]
        lenchunk = len(text_chunk)
        for chunks in range(0, lenchunk):
            msg.sendmsg(chatid,text_chunk[chunks]+"\n\n",False, update)
    print('Done.')
    msg.sendmsg(chatid,'Done.'+"\n\n",False, update)


def mainload(chatid,txt,btdat,update):


      if ""=="" :
            if "/help" in txt or "/help" in btdat:
                #print(update.message)
                msg.sendmsguser(chatid,txt2.presentacion+'\n\n'+'Baphomet Bot\n\n'+'/search text\n\n'+'/searchnum num\n\n'+'/help \n\n'+'/start \n\n',False)

            if "/restart" == txt or "/restart" in btdat or "/start" in txt:


                keyboard = [[InlineKeyboardButton("search", callback_data='/search '+str(chatid))],[InlineKeyboardButton("number search", callback_data='/numsearch '+str(chatid))],[InlineKeyboardButton("help", callback_data='/help '+str(chatid))]]

                #keyboard = [[InlineKeyboardButton("Ayuda Emergencia", callback_data='/ayuda_emergencia '+str(chatid)),
                 #   InlineKeyboardButton("Ayuda Económica", callback_data='/ayuda_economica '+str(chatid))],                    [InlineKeyboardButton("Trámites municipio", callback_data='/municipio '+str(chatid))],[InlineKeyboardButton("Identidad Digital", callback_data='/identidad '+str(chatid))],[InlineKeyboardButton("Monedero", callback_data='/monedero '+str(chatid))],[InlineKeyboardButton("Diagnóstico Médico", callback_data='/diagnostico_rapido '+str(chatid))]]
                
                reply_markup = InlineKeyboardMarkup(keyboard)
                print(update)
                
                update.message.reply_text(
                    txt2.inicio+"\n\n"+txt2.presentacion,
                    reply_markup=reply_markup)


                #reply_markup = InlineKeyboardMarkup(keyboard)

               # update.message.reply_text(txt2.inicio+"\n\n"+txt2.presentacion)

                return (range(1))


            if "/search" in txt or "/search" in btdat:
                text_user = 0
                if len(txt) > len(btdat):
                    
                    text_user = txt.replace('/search ','')
                    text_user = text_user.replace('/search','')
                    text_user = text_user.replace(str(chatid),'')

                else:

                    text_user = btdat.replace('/search ','')
                    text_user = text_user.replace('/search','')
                    text_user = text_user.replace(str(chatid),'')

                if len(text_user) > 0:
                #print(text_user)
                    
                    msg.sendmsguser(chatid,"Calculating...Wait...\n\n",False)
                    workmsg = threading.Thread(target=search, args=(text_user, chatid, update))
                    workmsg.start()
                #data_search = search(text_user)
                else:
                    msg.sendmsguser(chatid,"Error: Need string...\n\n",False)


            if "/numsearch" in txt or "/numsearch" in btdat:
                text_user = 0
                if len(txt) > len(btdat):
                    text_user = txt.replace('/numsearch ','')
                    text_user = text_user.replace('/numsearch','')
                    text_user = text_user.replace(str(chatid),'')
                else:
                    text_user = btdat.replace('/numsearch ','')
                    text_user = text_user.replace('/numsearch','')
                    text_user = text_user.replace(str(chatid),'')
                if len(text_user) > 0:
            
                    msg.sendmsguser(chatid,"Calculating...Wait...\n\n",False)
                    workmsg = threading.Thread(target=searchnumber, args=(text_user, chatid, update))
                    workmsg.start()
                else:
                    msg.sendmsguser(chatid,"Error: Need number...\n\n",False)



            if "/talk" in txt or "/talk" in btdat or "/talk" in btdat or "talk" in btdat:
                                # get last ask and train with user response
                # get last user ask and train with the best response

                ## take decision
                ## sum all times appears sentence words , this is the word weight
                ## get all entries who sum near word sums +- precision margin
                ## get word with less word lenght in input and in output
                ## sum to all entries the minimum weight in input and outputs

                ## when input is ambiguous ... is nor refered to a subject , word with less weight , output will be ambiougus, no subjects in the outputs
                ## when is not ambious , subjects in input and output will be balanced
                ## global input weight will generate hipotesis of global ouput weight

                ## when output is similar to holy writings sentence, baphumet replace the sentence by holy writing sentenc plus cordenates to find in holy writings.


                msg.sendmsg(chatid,txt2.inicio,False, update)




            if "/cancel" in txt:
                #os.popen("killall ")
                update.message.reply_text("Servico parado")



            return range(1)

      else:
        update.message.reply_text("Not Allow")



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
        #if "None" !=str(txt):
        
        mainload(chatid,txt,btdat,update)


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


worker = Threads(func=ttranslator, ntask=50)
worker.start()


if __name__ == '__main__':
    main()


main()

def is_validated(chatid):
    #check if user has been validated

    return (path.exists("datos/"+str(chatid)+"/mrcert_"+chatid+".pem"))




