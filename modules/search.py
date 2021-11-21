import argparse
import os
import sys
import subprocess
import shlex
import p_els


# search data pattern
def search(options):
    ## distance ELS
    searchterm = options[0]
    mins = options[1]
    maxs = options[2]

    ListOfLetters = options[0].split("")

    return p_els.mod_9GetNumberValues.fn_GetNumberValues(ListOfLetters,ListOfLetters)


## get data from loaded dictionary
def get(options):
    a = options[0]
    b = options[1]
    c = options[2]

    return p_els.D[a,b,c]


def coreOptions():
    options = [["query", "query db ", "nostromo"], ["modelist", "(simple, full) ", "full"]]
    return options

## Extend command usage instructions 
def ExtendCommands():
    commands = [["search","search \"search term hebrew\""]]
    return commands




def core(moduleOptions):

	query = moduleOptions[0][2]
	modelist = moduleOptions[1][2]
	

