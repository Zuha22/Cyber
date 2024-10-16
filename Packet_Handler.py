from scapy.all import sniff
from scapy.layers.inet import IP

def packet_handler(packet):
    if packet.haslayer(IP):
        # Extract relevant information
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto
        payload = packet[IP].payload

        # Print the captured information
        print("Source IP:", source_ip)
        print("Destination IP:", destination_ip)
        print("Protocol:", protocol)
        print("Payload:", payload)
        print("\n")

# Start sniffing packets
sniff(prn=packet_handler)