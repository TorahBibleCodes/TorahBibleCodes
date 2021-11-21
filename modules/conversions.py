import argparse
import os
import sys
import subprocess
import shlex
import p_els

## search query

import re

def search(options):
    exp = options[0]
    print(exp)
    #print(p_els.D)
    for (z,b,y) in p_els.D:
        m = re.search(exp, p_els.D[z,b,y])
        #print (p_els.D[z,b,y])
        try:
            print(m.group(0))
            print(p_els.D[z,b,y])
        except:
            pass

def els(options):
    space = options[1]
    i=1

    for (z,b,y) in p_els.D:
        #m = re.search(exp, p_els.D[z,b,y])
        #print (p_els.D[z,b,y])
        try:
         #   print(m.group(0))
            #print(p_els.D[z,b,y])
            res=""
            for char in p_els.D[z,b,y]:
                if (i % int(space)) == 0:
                    res=(char)+res

                i=i+1
            print(res)
        except:
            pass

# get data from letters
def tonum(options):
    ListOfLetters = options[0].split(",")

    print (p_els.mod_9GetNumberValues.fn_GetNumberValues(ListOfLetters,ListOfLetters))


## get data from loaded dictionary
def get(options):
    a = options[0]
    b = options[1]
    c = options[2]
    print(p_els.D[int(a),int(b),int(c)])


def coreOptions():
    options = [["query", "query db ", "El"], ["modelist", "(simple, full) ", "full"]]
    return options

## Extend command usage instructions 
def ExtendCommands():
    commands = [["els","els words space"],["search","search termsexp"],["get","get book verse number"],["tonum","tonum (sentence or word)"],["toword","toword \"1,2,3,4,5\""]]
    return commands




def core(moduleOptions):

	query = moduleOptions[0][2]
	modelist = moduleOptions[1][2]
	

