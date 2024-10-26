from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Packet: {ip_layer.src} -> {ip_layer.dst}, Protocol: {ip_layer.proto}")

    if TCP in packet:
        tcp_layer = packet[TCP]
        print(f"TCP Packet: {tcp_layer.sport} -> {tcp_layer.dport}")

    if UDP in packet:
        udp_layer = packet[UDP]
        print(f"UDP Packet: {udp_layer.sport} -> {udp_layer.dport}")

def main():
    print("Starting network activity scan...")
    # Adjust the filter as needed (e.g., "ip" for IP packets, "tcp" for TCP packets)
    sniff(prn=packet_callback, filter="ip", store=False)

import time

if __name__ == "__main__":
    main()
    timeout_seconds = 3 #Ends scan in three seconds
