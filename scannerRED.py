#!/usr/bin/env python3

import os
from scapy.all import *
from mac_vendor_lookup import MacLookup
	
def main(range_ip):
	print ("\n[+] Escaneando...\n")
	# Obteniendo las IPs usando el protocolo ARP
	ans, unans = arping(range_ip, verbose=0)
	
	for s, r in ans:
		print ("[+] HOST: {} MAC: {} DEVICE: {}".format(s[ARP].pdst, r[Ether].src, MacLookup().lookup(r[Ether].src)))
		
if __name__ == "__main__":
	if os.geteuid() != 0:
		print ("\n[i] Tu no eres Root\n")
	else:	
		if len(sys.argv) < 2:
			print ("\nUSO: {} <rango de IPs>\n".format(sys.argv[0]))
		else:
			main(sys.argv[1])
