import argparse
import os
import sys
import subprocess

def coreOptions():
    options = [["query", "query db ", "nostromo"], ["modelist", "(simple, full) ", "full"]]
    return options




def core(moduleOptions):

	query = moduleOptions[0][2]
	modelist = moduleOptions[1][2]
	

