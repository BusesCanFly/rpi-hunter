# rpi-hunter
Automate discovering all Raspberry Pi's on a LAN and drop a payload via ssh (using default creds)

This tool can be useful for when there are multiple Raspberry Pi's on your LAN with default or known credentials, in order to automate sending commands to them.

# GUIDE:

## Installation

1. Install dependencies: `sudo pip install -U argparse termcolor` and `sudo apt -y install arp-scan tshark`
2. Download autowrite: `git clone https://github.com/BusesCanFly/rpi-hunter`
3. Navigate to autowrite: `cd ./rpi-hunter`
4. Make autowrite.py executable: `chmod +x rpi-hunter.py`
* One line variant: sudo pip install -U argparse termcolor && sudo apt -y install arp-scan tshark && git clone https://github.com/BusesCanFly/rpi-hunter && cd ./rpi-hunter && chmod +x rpi-hunter.py

## Usage
```
usage: rpi-hunter.py [-h] [--no-scan] [-r IP_RANGE] [-f IP_LIST] [-c CREDS]
                     [-H HOST] [-P PORT] [--safe]

optional arguments:
  -h, --help            show this help message and exit
  --no-scan             Disable scanning
  -r IP_RANGE, --ip_range IP_RANGE
                        IP range to scan
  -f IP_LIST, --ip_list IP_LIST
                        IP list to use (Default ./scan/RPI_list)
  -c CREDS, --creds CREDS
                        Password to use when ssh'ing
  -H HOST, --host HOST  (If using reverse shell payload) Host for reverse
                        shell
  -P PORT, --port PORT  (If using reverse shell payload) Port for reverse
                        shell
  --safe                Print sshpass command, but don't execute it
```
* Example: `./rpi-hunter.py -r 192.168.0.0/16 -c password`
* Note: Currently payloads are just a commented list in `rpi-hunter.py`, just uncomment which one you want to run
    * I'm a noob with python, it'll be better soon :D

## Disclaimer
## The standard internet fun disclaimer applies. Don't commit crimes, be responsible.

## I am in no way responsible for anything and everything you do with rpi-hunter.
