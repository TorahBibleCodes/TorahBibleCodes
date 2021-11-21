import argparse
import os
import sys
import subprocess

def coreOptions():
    options = [["filelist", "set file for add to db in format (1.1.1.1,80)", "file"], ["namelist", "name for save list on db ", "microtik_v2"]]
    return options






def core(moduleOptions):

	filelist = moduleOptions[0][2]
	namelist = moduleOptions[1][2]
	with open(filelist, 'r') as reader:
			for x in reader:
				spl = x.split(":")
				ip = spl[0]
				geoip(ip, namelist)
