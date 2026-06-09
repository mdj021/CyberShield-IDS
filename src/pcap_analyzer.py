from scapy.all import rdpcap

def analyze_pcap(file_path):

    packets = rdpcap(file_path)

    total_packets = len(packets)

    tcp_count = 0
    udp_count = 0
    icmp_count = 0

    for packet in packets:

        if packet.haslayer("TCP"):
            tcp_count += 1

        elif packet.haslayer("UDP"):
            udp_count += 1

        elif packet.haslayer("ICMP"):
            icmp_count += 1

    # Risk Analysis

    if udp_count > tcp_count * 3:
        risk = "HIGH"
        message = "Possible UDP Flood Attack"

    elif tcp_count > 1000:
        risk = "MEDIUM"
        message = "Heavy TCP Traffic Detected"

    else:
        risk = "LOW"
        message = "Traffic Appears Normal"

    return {
        "total": total_packets,
        "tcp": tcp_count,
        "udp": udp_count,
        "icmp": icmp_count,
        "risk": risk,
        "message": message
    }