import glob
import os
import modules.resources.msg as msg
import logging

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


import random

#import modules.nlp as nlp

try:
    from PIL import Image
except ImportError:
    import Image
import math as math
# If you don't have tesseract executable in your PATH, include the following:


from PIL.ExifTags import TAGS, GPSTAGS

def get_exif(filename):
    exif = Image.open(filename)._getexif()

    if exif is not None:
        for key, value in exif.items():
            name = TAGS.get(key, key)
            exif[name] = exif.pop(key)

        if 'GPSInfo' in exif:
            for key in exif['GPSInfo'].keys():
                name = GPSTAGS.get(key,key)
                exif['GPSInfo'][name] = exif['GPSInfo'].pop(key)

    return exif




def get_decimal_coordinates(info):
    for key in ['Latitude', 'Longitude']:
        if 'GPS'+key in info and 'GPS'+key+'Ref' in info:
            e = info['GPS'+key]
            ref = info['GPS'+key+'Ref']
            info[key] = ( e[0][0]/e[0][1] +
                          e[1][0]/e[1][1] / 60 +
                          e[2][0]/e[2][1] / 3600
                        ) * (-1 if ref in ['S','W'] else 1)

    if 'Latitude' in info and 'Longitude' in info:
        return [info['Latitude'], info['Longitude']]


def get_random(filepath):
    d = get_file(filepath)
    return d[math.floor(random.uniform(0.0, 17.0))] 

def metadata(filepath):
    exif = get_exif(filepath)
    ex = get_decimal_coordinates(exif['GPSInfo'])
    return ex





def save_txt(filepath, dat,chatid):
    try:
        os.mkdir("datos/"+str(chatid))
    except OSError:
        pass
    else:
        print ("Successfully created the directory %s " % filepath)

    with open(filepath, "a") as myfile:
        myfile.write(dat)


def get_username(chatid):
    f = listfiles("datos/"+str(chatid)+"/*.balance")
    if f:
        return f[0].split(".")[0].split("/")[2]
    else:
        return "None"


def get_last_file(filepath):
    f = open(filepath, "r")
    return (f.readlines()[-1]) 


def get_fst_file(filepath):
    f = open(filepath, "r")
    return (f.readlines()[0]) 

def get_file(filepath):
    f = open(filepath,"r")
    return (f.readlines())


def sum_file(filepath):
    f = open(filepath, "r")
    
    total=0
    for x in f:
        try:
            total = total+int(x)
        except:
            pass

    return (total)


def rm_line(match,filepath):
    f = open(filepath, "r")
    result=""
    for x in f:
        if match!=x:
            result=result+x
        else:
            result=result

    return (result)


def listfiles(filepath):
    return (glob.glob(filepath))


