#!/usr/bin/env python3
# -.- coding: utf-8 -.-

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
from lxml import html
import requests
  
  

try:
	import os
	import traceback
	import argparse
	import pathlib
	import time
	import signal
	import sys

	#import lib.nc as nc
	# MODULE IMPORT
	from modules import *
	#from active_modules import *
except KeyboardInterrupt:
	print(GREEN + "\n[I] Shutting down..." + END)
	raise SystemExit
except Exception as e:
	print(RED + "\n[!] Module crashed." + END)
	print(RED + "[!] Debug info:\n'")
	print(traceback.format_exc())
	print("\n" + END)
	print(RED + "\n[!] Module input failed. Please make sure to install the dependencies." + END)
	raise SystemExit

#allModules = []
#textToModule = []


allModules = [["conversions","conversions Torah"]]


textToModule = [["conversions", conversions]]

inModule = False
currentModule = ""
moduleOptions = []
moduleExtendCommands = []

#getCoreOptions = getattr(test, "caca")
#moduleOptions = getCoreOptions()
#print(moduleOptions)
"""
def vsvs():
	print('GGGGGGGGG')

getCoreOptions = getattr(test, "coreOptions", None)
moduleOptions = getCoreOptions()
currentModuleFile = currentModule
 """
def signal_handler(signal,frame):
	print('You pressed Ctrl+C!')
	#sys.exit(0)

#signal.signal(signal.SIGINT,signal_handler)


def del_char(string, indexes):

	return ''.join((char for idx, char in enumerate(string) if idx not in indexes))

def commandHandler(command):
	command = str(command)
	command = command.lower()

	global inModule
	global currentModule
	global moduleOptions
	global currentModuleFile
	global moduleExtendCommands

	# COMMANDS

	# HELP
	def helpPrint(name, desc, usage):
		print("\t" + YELLOW + name + GREEN + ": " + BLUE + desc + GREEN + " - '" + usage + "'" + END)
	if command == "help":
		print(GREEN + "\n[I] Available commands:\n" + END)
		helpPrint("MODULES", "List all modules", "modules")
		helpPrint("USE", "Use a module", "use module_name")
		helpPrint("OPTIONS", "Show a module's options", "options")
		helpPrint("SET", "Set an option", "set option_name option_value")
		helpPrint("RUN", "Run the selected module", "run")
		helpPrint("BG", "Toggle module background", "bg")
		helpPrint("BACK", "Go back to menu", "back")
		helpPrint("EXIT", "Shut down TBC", "exit")
		print()

	# NETCAT
  #  elif command == 'listen':
   #     nc.run()

	# BACKGROUND
	#elif command == 'bg':
	#    if nc.BG == True:
	#        nc.BG = False
	#    else:
	#        nc.BG = True
	#        nc.job()
	# USE
	elif command.startswith("use "):
		if not inModule:
			tempModule = command.replace("use ", "")
			inModule = False
			for module in allModules:
				if module[0] == tempModule:
					inModule = True
			if inModule:
				inModule = True
				currentModule = tempModule
				for text in textToModule:
					if text[0] == currentModule:
						currentModuleFile = text[1]
				getCoreOptions = getattr(currentModuleFile, "coreOptions", None)
				moduleOptions = getCoreOptions()
				try:
					getExtendCommands = getattr(currentModuleFile, "ExtendCommands", None)
					moduleExtendCommands = getExtendCommands()
				except:
					pass
				#print(moduleExtendCommands)
				
			else:
				print(RED + "[!] Module '" + YELLOW + tempModule + RED + "' not found." + END)
		else:
			print(RED + "[!] Module '" + YELLOW + currentModule + RED + "' already selected. Type '" + YELLOW + "back" + RED + "' to go back to the main menu." + END)
	elif command == "use":
		print(RED + "[!] Usage: 'use " + YELLOW + "module_name" + RED + "'" + END)

	# OPTIONS
	elif command == "options":
		if inModule:
			print(GREEN + "\n Options for module '" + YELLOW + currentModule + GREEN + "':" + END)
			for option in moduleOptions:
				if option[2] == "":
					print("\t" + YELLOW + option[0] + GREEN + " - " + BLUE + option[1] + GREEN + " ==> " + RED + "[NOT SET]" + END)
				else:
					print("\t" + YELLOW + option[0] + GREEN + " - " + BLUE + option[1] + GREEN + " ==> '" + YELLOW +
						  option[2] + GREEN + "'" + END)
			print()
			print(GREEN + "\n Commands for module '" + YELLOW + currentModule + GREEN + "':" + END)
			print("\t" + YELLOW + "run" + GREEN + " - " + BLUE + "Execute module" + GREEN + END)
			for optionExt in moduleExtendCommands:
				#print(optionExt)
				print("\t" + YELLOW + optionExt[0] + GREEN + " - " + BLUE + optionExt[1] + GREEN + END)
			print()
		else:
			print(RED + "[!] No module selected." + END)

	# SET
	elif command.startswith("set "):
		if inModule:
			command = command.replace("set ", "")
			command = command.split()
			error = False
			try:
				test = command[0]
				test = command[1]
			except:
				print(RED + "[!] Usage: 'set " + YELLOW + "option_name option_value" + RED + "'" + END)
				error = True
			if not error:
				inOptions = False
				for option in moduleOptions:
					if option[0] == command[0]:
						inOptions = True
						#option[2] = command[1]
						vquery = str(command).strip('[]')
						vquery = vquery.replace(command[0], "")
						vquery = vquery.replace("', '", "*")
						vquery = vquery.replace(" ", "")
						vquery = vquery.replace("*", " ")
						vquery = vquery.replace("'", "")
						vquery = del_char(vquery, [0])
						option[2] = vquery
						print(YELLOW + option[0] + GREEN + " ==> '" + YELLOW + str(vquery) + GREEN + "'" + END)
				if not inOptions:
					print(RED + "[!] Option '" + YELLOW + command[0] + RED + "' not found." + END)
		else:
			print(RED + "[!] No module selected." + END)
	elif command == "set":
		print(RED + "[!] Usage: 'set " + YELLOW + "option_name option_value" + RED + "'" + END)

	# RUN
	elif command == "run":
		if inModule:
			fail = False
			for option in moduleOptions:
				if option[2] == "":
					fail = True
			if not fail:
				print(GREEN + "[I] Starting module '" + YELLOW + currentModule + GREEN + "'..." + END)
				coreModule = getattr(currentModuleFile, "core")
				try:
					coreModule(moduleOptions)
				except KeyboardInterrupt:
					print(GREEN + "[I] Stopping module..." + END)
				except Exception as e:
					print(RED + "\n[!] Module crashed." + END)
					print(RED + "[!] Debug info:\n'")
					print(traceback.format_exc())
					print("\n" + END)
			else:
				print(RED + "[!] Not all options set." + END)
		else:
			print(RED + "[!] No module selected." + END)

	# BACKGROUND
	elif command == "bg":
		if inModule:
			fail = False
			for option in moduleOptions:
				if option[2] == "":
					fail = True
			if not fail:
				print(GREEN + "[I] Recovery job '" + YELLOW + currentModule + GREEN + "'..." + END)
				try:
					corebjModule = getattr(currentModuleFile, "job")

					try:

						corebjModule()
					except KeyboardInterrupt:
						print(GREEN + "[I] Stopping module..." + END)
					except Exception as e:
						print(RED + "\n[!] Module crashed." + END)
						print(RED + "[!] Debug info:\n'")
						print(traceback.format_exc())
						print("\n" + END)
				except Exception as e:
					print(RED + "\n[!] Module not have bj." + END)
			else:
				print(RED + "[!] Not all options set." + END)
		else:
			print(RED + "[!] No module selected." + END)
	# BACK
	elif command == "back":
		if inModule:
			inModule = False
			currentModule = ""
			moduleOptions = []
			moduleExtendCommands = []

	# EXIT
	elif command == "exit":
		print(GREEN + "[I] Shutting down..." + END)
		raise SystemExit

	# MODULES
	elif command == "modules":
		print(GREEN + "\nAvailable modules:" + END)
		for module in allModules:
			print(YELLOW + "\t" + module[0] + GREEN + " - " + BLUE + module[1] + END)
		print()

	# CLEAR
	elif command == "clear":
		os.system("clear||cls")

	# DEBUG
	elif command == "debug":
		print("inModule: " + str(inModule))
		print("currentModule: " + str(currentModule))
		print("moduleOptions: " + str(moduleOptions))
		print("currentModuleFile: " + str(currentModuleFile))

	elif command == "":
		pass

	else:
		if inModule:
			fail = False

			for option in moduleExtendCommands:

				if option[0] == command or command.startswith(option[0]):
					try: 
						updateModule = getattr(currentModuleFile, "save")
						updateModule(moduleOptions)
						ExecCmdExtend = getattr(currentModuleFile, option[0])
						command = command.replace(option[0] + " ", "")
						commands = command.split()
						ExecCmdExtend(commands)
					except Exception as e:
						print(RED + "\n[!] TBC crashed...\n[!] Debug info: \n")
						print(traceback.format_exc())
						print("\n" + END)
						pass
				   
		else:
			print(RED + "[!] Unknown command: '" + YELLOW + command + RED + "'. Type '" + YELLOW + "help" + RED + "' for all available commands." + END)

parser = argparse.ArgumentParser(description="TBC")
parser.add_argument("--run", action='store_true')
parser.add_argument("--test", action='store_true')
parser.add_argument('--module', action='store', type=str, required=False)
parser.add_argument('--options', action='store', type=str, required=False)
#args, leftovers = parser.parse_known_args()
args = parser.parse_args()

if args.test:
	print("Test build detected. Exiting...")
	exit()
if args.module:
	print(args.module)
	commandHandler('use '+args.module)
if args.options:

	for op in args.options.split(';'):
		commandHandler(op)

if args.run:
	commandHandler('run')


header = """

TBC command line interface 

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@%#(((%@@%#(((#@@&%#(##&@@&#(//#@@@&#//(#@@@&#(((%@@%%###%&@@@@@@@@@@
@@@@@@@@@@@@%#/(/&@@(#///#@@@/#,(*&@@@//*(/&@@&/(,(/@@@%/(*(*@@&((*(#@@@@@@@@@@@
@@@@@@@@@@@@&#((&@@@@#(/%@@@@%(*/%@@@@%(*(%@@@@#/*(#@@@@#//(%@@@#*(#&@@@@@@@@@@@
@@@@@@@@@@@@@%*#@@@@@@//@@@@@@%//@@@@@@#/#@@@@@@(*(@@@@@@(/&@@@@@,*&@@@@@@@@@@@@
@@@@@@@@@@@@@@(#@@@@@@(/@@@@@@&//@@@@@@#/%@@@@@@(*&@@@@@@//@@@@@@//@@@@@@@@@@@@@
@@@@@@@@@@@@@@##@@@@@@%*&@@@@@@#,&@@@@@#/#@@@@@%/#@@@@@@&(#@@@@@@##@@@@@@@@@@@@@
@@@@@@@@@@@@@@%*@@@@@@@#(@@@@@@@%*/@@@@#*(@@@@/*#@@@@@@@#(@@@@@@%*%@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%(&@@@@@@%/%@@@@@@@@&##(#,(((#&@@@@@@@@%/#@@@@@@%*(@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%(&@@@@@@@%((@@@@@@@@@@(*(@@@@@@@@@&#/#@@@@@@@&/#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&/#@@@@@@@@&%//#@@@@@&(*/@@@@@@#**#@@@@@@@@&#/@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%((@@@@@@@@@@@@&%#(#(,((((%&@@@@@@@@@@@&/(&@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@#/#@@@@@@@@@@@@@%#/(&@@@@@@@@@@@@&#*(@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%(*#%@@@@@@@@(***(@@@@@@@&%#*/%@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%/***(/*,**/***(%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/*/(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#/**(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/*/**%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/,***#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**/(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(**(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/*/*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#(,.,/(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(/,/(*/*///#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%((((,/***(//(#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#//(/,(,/,**/*//(%(##@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(/#//***/,/,** /,,*,/(#%@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&#%##(****////*,//,,*//((&&%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%(/(###(////////(.////////(#(##%@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@%%//((((*.,,,,,,,,.,.,,,(//((((&@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%#(((/,,,*,.*,*,,..*///(/((#@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&%%%#((/*(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

"""

print(GREEN + header + "                        v1.1\n" + END)


moduleList = ""
i = 0
for module in allModules:
	i += 1
	if i%7 == 0:
		moduleList += "\n"
	moduleList = moduleList + YELLOW + module[0] + GREEN + ", "
moduleList = moduleList[:-2]
print(GREEN + "Loaded modules: " + moduleList + "\n")

while True:
	if inModule:
		inputHeader = BLUE + "TBC" + RED + "/" + currentModule + BLUE + " $> " + END
	else:
		inputHeader = BLUE + "TBC $> " + END

	try:
		commandHandler(input(inputHeader))
	except KeyboardInterrupt:
		print(GREEN + "\n[I] Shutting down..." + END)
		raise SystemExit
	except Exception as e:
		print(RED + "\n[!] TBC crashed...\n[!] Debug info: \n")
		print(traceback.format_exc())
		print("\n" + END)
		exit()
