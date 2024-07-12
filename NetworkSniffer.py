import socket
import struct

# Function to parse Ethernet frames
def parse_ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return format_mac_addr(dest_mac), format_mac_addr(src_mac), socket.htons(proto), data[14:]

# Function to format MAC address
def format_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

# Function to sniff and analyze network packets
def sniff_packets(iface):
    # Create a raw socket and bind it to the network interface
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
    sock.bind((iface, 0))

    try:
        while True:
            raw_data, addr = sock.recvfrom(65535)  # Maximum size of the packet
            dest_mac, src_mac, eth_proto, data = parse_ethernet_frame(raw_data)
            
            print(f'\nEthernet Frame:')
            print(f'Destination MAC: {dest_mac}, Source MAC: {src_mac}, Protocol: {eth_proto}')
            
            # Add more protocols and parsing logic here (e.g., IP, TCP, UDP)
            # Example: For IPv4
            if eth_proto == 0x0800:  # IPv4
                # Parse IP header (20 bytes for IPv4)
                version_header_length = data[0]
                version = version_header_length >> 4
                header_length = (version_header_length & 15) * 4
                ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
                print(f'IPv4 Packet:')
                print(f'Source IP: {socket.inet_ntoa(src)}, Destination IP: {socket.inet_ntoa(target)}')

    except KeyboardInterrupt:
        print("\nShutting down.")
        sock.close()

if __name__ == "__main__":
    sniff_packets('eth0')  # Replace 'eth0' with your network interface
