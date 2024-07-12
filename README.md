# Network Sniffer
## Overview
This project is a network sniffer tool implemented in Python. It captures and analyzes network traffic, providing detailed information about each packet.

## Features
 Listening and Analyzing Network Packets:
    Once the socket is set up, the program enters a loop (while True) to listen for incoming network packets.

  -  Parsing Ethernet Frames:
    Upon receiving a packet, the program uses the parse_ethernet_frame function to parse the Ethernet frame header to extract information such as MAC addresses (source and destination) and the frame's protocol (e.g., IPv4).

   - Parsing IPv4 Packets:
    If the frame's protocol is IPv4 (0x0800), the program uses the parse_ipv4_packet function to parse the packet header to extract information such as source IP address, destination IP address, and the protocol (TCP or UDP).

-  Parsing TCP and UDP Packets:
    If the protocol inside the IPv4 packet is TCP (6) or UDP (17), the program uses the parse_tcp_segment or parse_udp_segment functions to extract information such as source and destination ports, and any additional data.

 -   Displaying Information:
    After parsing each packet, the program prints the extracted information to the screen, such as MAC addresses, IP addresses, and TCP or UDP ports.

- ### The script will start capturing network packets and display detailed information about each packet in real-time.
