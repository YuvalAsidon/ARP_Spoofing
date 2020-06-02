# arp_spoofing
[scapy](https://scapy.readthedocs.io/en/latest/index.html)
* ARP spoofing in python3 using scapy
* Fools the victim's computer that we are the router and the router thinks that we are the victim

## install scapy
* cd /tmp
* git clone https://github.com/phaethon/scapy
* sudo python3 setup.py install

## install sslstrip
if you are running the new kali:
 * add to the source.list --> deb http://old.kali.org/kali sana main non-free contrib
 * only then -->  sudo apt-get install sslstrip

## how to use:
* enable packets to flow though the kali just like a router
  * sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
* change in the code to the IP address you want for the router and the victim 
* sudo python3 arp_spoofing.py
