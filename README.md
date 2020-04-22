# arp_spoofing
[scapy](https://scapy.readthedocs.io/en/latest/index.html)
ARP spoofing in python3 using scapy
* fools the victim's computer that we are the router and the router thinks that we are the victim

## install scapy
* cd /tmp
* git clone https://github.com/phaethon/scapy
* sudo python3 setup.py install

## how to use:
* enable packets to flow though the kali just like a router
** sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
