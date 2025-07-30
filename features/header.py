from scapy.layers.inet import TCP, IP,UDP

def extract(flow):
    fwd_header_len = 0 
    bwd_header_len = 0


    for pkt in flow.forward_packets:
        if IP in pkt:
            ip_layer = pkt[IP]
            ip_header_len = ip_layer.ihl * 4
            l4_header_len = 0
            if TCP in pkt:
                l4_header_len = pkt[TCP].dataofs * 4
            elif UDP in pkt:
                l4_header_len = 8

            total_header = ip_header_len + l4_header_len

            if pkt.src == flow.src_ip:
                fwd_header_len += total_header
            else:
                bwd_header_len += total_header
    return {
        "fwd_header_len":fwd_header_len,
        "bwd_header_len":bwd_header_len
    }