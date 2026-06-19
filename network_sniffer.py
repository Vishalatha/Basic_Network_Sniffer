from scapy.all import sniff
from scapy.layers.inet import IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("=" * 50)
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")
        print(f"Protocol       : {packet[IP].proto}")
        print(f"Summary        : {packet.summary()}")

sniff(prn=packet_callback, count=10)