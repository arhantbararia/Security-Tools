from scapy.all import *
import sys
import time



def ARPscanner(iface, iprange):
	print("[+] Scanning iprange");
	start_time = time.time()
	print("[+] Scan started at ", time.ctime(start_time))
	conf.verb = 0 		#setting verbose off "we dont need much information
	
	#configuring ether layer
	ether= Ether(dst = "ff:ff:ff:ff:ff:ff") #setting to broadcast
	
	#configuring ARP packets
	arp= ARP(pdst = iprange)
	
	packet = ether/arp

	ans , unans = srp(packet, iface= iface , timeout = 5, inter = 0.1)
	for send , recieve in ans:
		ip = recieve[ARP].psrc
		mac = recieve[Ether].src
		print("\t", ip)
		print("\t" , mac)
		print("\n")
	duration = time.time() - start_time
	print("[+] Scan Completed, Duration ", duration)




#scanner.py eth0 192.168.0.1/24
if __name__ == "__main__":
	iface = sys.argv[1]
	ip_range = sys.argv[2]
	ARPscanner(iface, ip_range)



	

