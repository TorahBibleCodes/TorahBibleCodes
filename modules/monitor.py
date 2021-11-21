
import subprocess



def coreOptions():
	options = [["filter","set filter for the monitor ssh(setvice) or cn(country) or nothing","ssh"]]
	return options


def run(country):
        subprocess.call(['node ../blessed-contrib/examples/monitor.js'], shell=True)

def core(moduleOptions):
	s_filter = moduleOptions[0][2]
	subprocess.call(['node ../blessed-contrib/examples/monitor.js'], shell=True)
	#subprocess.call(['node /home/cryptocalypse/deus/blessed-contrib/examples/monitor.js'], shell=True)


#returned_value = os.system('nohup '+cmd+' > /dev/null &') 
