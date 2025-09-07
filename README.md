# Network-Port-Scanner-using-Scapy
Developed a Python-based network scanning tool using the Scapy library to craft and send TCP packets, identify open/closed ports, and analyze responses.

# Features:
Scan multiple ports on a target IP.

Detect open and closed ports.

Save output to a file.

# How It Works:
Crafts TCP SYN packets for each port.

Sends packets to the target host.

# Analyzes responses:
SYN-ACK means the port is open.

RST-ACK means the port is closed.

# Requirements:
Python

Scapy (pip install scapy)


# Why Scapy means:
1.Direct Access to Network Interfaces

2.Crafting and Sending Raw Packets

3.Performing Network Scans and Sniffing
