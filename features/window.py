from decimal import Decimal 
from scapy.layers.inet import TCP

def extract(flow):
    init_fwd_win_bytes = 0
    init_bwd_win_bytes = 0

    for pkt in flow.forward_packets :
        if TCP in pkt:
            init_fwd_win_bytes = pkt[TCP].window
            break
    for pkt in flow.backward_packets:
        if TCP in pkt:
            init_bwd_win_bytes = pkt[TCP].window
            break
    return {
        "init_fwd_win_bytes":Decimal(init_fwd_win_bytes),
        "init_bwd_win_bytes":Decimal(init_bwd_win_bytes)
    }