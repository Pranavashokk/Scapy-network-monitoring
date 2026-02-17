from scapy.all import sniff  


packets = sniff(count=10)

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"), timeout=2)
packets.summary()
ans.summary