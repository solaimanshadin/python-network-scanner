import scapy.all as scapy

def scan(ip):
     request = scapy.ARP(pdst=ip)
     bordcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
     bordcast_arp = bordcast/request
     answered, unanswared=scapy.srp(bordcast_arp, timeout=1)
     print(answered.summary())

scan("192.168.0.100/24")