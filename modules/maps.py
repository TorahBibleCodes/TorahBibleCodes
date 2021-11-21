from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from contextlib import closing
import csv
import io
from colorama import init
from colorama import Fore, Back, Style, Cursor
from datetime import datetime
import os
import threading
import time
import sys
from itertools import cycle
import netaddr
import resource as res
import subprocess

MAX_THREADS = 1
scanfilter  = ''
ports = '80'
from time import perf_counter
#IPv4Network('0.0.0.0/255.255.255.0').prefixlen
lista = []
plist = {}


def coreOptions():
	options = [["latitude", "set map latitude", ""], ["longitude", "set map longitude", ""], ["threads", "Set max threads", "1"]]
	return options

class Colored:
	@staticmethod
	def magenta(s):
		return Style.BRIGHT+Fore.MAGENTA+s+Fore.RESET+Style.RESET_ALL
	@staticmethod
	def green(s):
		return Style.BRIGHT+Fore.GREEN+s+Fore.RESET+Style.RESET_ALL
	@staticmethod
	def white(s):
		return Fore.WHITE+s+Fore.RESET+Style.RESET_ALL
	@staticmethod
	def cyan(s):
		return Style.BRIGHT+Fore.CYAN+s+Fore.RESET+Style.RESET_ALL
	@staticmethod
	def cyan_fine(s):
		return Fore.CYAN+s+Fore.RESET+Style.RESET_ALL
	@staticmethod
	def yellow(s):
		return Style.BRIGHT+Fore.YELLOW+s+Fore.RESET+Style.RESET_ALL
	@staticmethod
	def red(s):
		return Style.BRIGHT+Fore.RED+s+Fore.RESET+Style.RESET_ALL
	@staticmethod
	def yel_info():
		return Style.BRIGHT+Fore.CYAN+"[INFO]"+Fore.RESET+Style.RESET_ALL
	@staticmethod
	def red_warn():
		return Style.BRIGHT+Fore.RED+"[WARN]"+Fore.RESET+Style.RESET_ALL
	@staticmethod
	def rce():
		return Style.BRIGHT+Fore.RED+"[RCE]"+Fore.RESET+Style.RESET_ALL
	@staticmethod
	def de_rce():
		return "[deserialization rce]"
	@staticmethod
	def upload():
		return "[upload]"
	@staticmethod
	def de_upload():
		return "[deserialization upload]"
	@staticmethod
	def de():
		return "[deserialization]"
	@staticmethod
	def contains():
		return "[file contains]"
	@staticmethod
	def xxe():
		return "[xxe]"
	@staticmethod
	def sql():
		return "[sql]"
	@staticmethod
	def ssrf():
		return "[ssrf]"


color = Colored()

class Timed:
	@staticmethod
	def timed(de):
		get_time = datetime.now()
		time.sleep(de)
		timed = color.cyan_fine("["+str(get_time)[11:19]+"] ")
		return timed
	@staticmethod
	def timed_line(de):
		get_time = datetime.now()
		time.sleep(de)
		timed = color.cyan("["+str(get_time)[11:19]+"] ")
		return timed
	@staticmethod
	def no_color_timed(de):
		get_time = datetime.now()
		time.sleep(de)
		no_color_timed = "["+str(get_time)[11:19]+"] "
		return no_color_timed


now = Timed()

def identify_prt(name):
	print("\r{0}{1} {2}".format(now.timed(de=0), color.yel_info(), color.red(name)), end="                ")

def identify_prt2(name):
	print("\r{0}{1} {2}".format(now.timed(de=0), color.yel_info(), color.red(name)))


def get_country():

	url = "https://www.nirsoft.net/countryip/"
	page = urlopen(url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")

	job_elems = soup.find_all('table')[6]

	job_elems2 = job_elems.find_all('a')

	#print(job_elems2)

	for link in job_elems2:
			address = link["href"]
			text = link.text
			print(f"{text}: {address}")





#res.setrlimit(res.RLIMIT_NOFILE,(10000,10000))

def run(country):
        subprocess.call(['mapscii'], shell=True)

def core(moduleOptions):
	global MAX_THREADS, ports
	country = moduleOptions[0][2]
	ports = moduleOptions[1][2]
	scanfilter = moduleOptions[2][2]
	MAX_THREADS = int(moduleOptions[2][2])
	#target = moduleOptions[2][2]
	#uselist = moduleOptions[3][2]
	subprocess.call('mapscii')


#returned_value = os.system('nohup '+cmd+' > /dev/null &') 
