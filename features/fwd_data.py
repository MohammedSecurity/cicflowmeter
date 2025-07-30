from decimal import Decimal
from scapy.layers.inet import TCP

def extract(flow):
    fwd_data_pkts = 0
    for pkt in flow.forward_packets:
        if TCP in pkt:
            payload_len = len(pkt[TCP].payload)
            if payload_len > 0:
                fwd_data_pkts += 1
    return {
        "fwd_act_data_pkts":Decimal(fwd_data_pkts)
    }