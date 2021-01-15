#!/usr/bin/env python3
import os
import requests
from scapy.all import *

# Obteniendo la direccion MAC por medio de la API web 
# que nos regala macvendors.com

def mac2device(macaddress):
	api = "https://api.macvendors.com/" + macaddress
	req = requests.get(api, headers={'User-Agent':'curl/7.47.0'})
	if req.ok:
		return req.text
	else:
		return "Error : " + req.status_code

def main(range_ip):
	print ("\n[+] Escaneando...\n")
	# Obteniendo las IPs usando el protocolo ARP
	ans, unans = arping(range_ip, verbose=0)
	for s, r in ans:
		print ("[+] HOST: {} MAC: {} DEVICE: {}".format(s[ARP].pdst, r[Ether].src, mac2device(r[Ether].src)))
		
if __name__ == "__main__":
	if os.geteuid() != 0:
		print ("\n[i] Tu no eres Root\n")
	else:	
		if len(sys.argv) < 2:
			print ("\nUSO: {} <rango de IPs>\n".format(sys.argv[0]))
		else:
			main(sys.argv[1])
