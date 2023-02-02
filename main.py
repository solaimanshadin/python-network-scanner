import scapy.all as scapy

def scan(ip):
     request = scapy.ARP(pdst=ip)
     bordcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
     bordcast_arp = bordcast/request
     answered=scapy.srp(bordcast_arp, timeout=1, verbose=False)[0]
     print("Mac \t\t\tIP \n------------------------------------------")
     for packet in answered:
          print(packet[1].hwsrc + "\t",packet[1].psrc )

scan("192.168.0.100/24")