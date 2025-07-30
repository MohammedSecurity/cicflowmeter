from decimal import Decimal
from scapy.layers.inet import TCP

def extract(flow):
    fwd_seg_size = []
    bwd_seg_size = []

    for pkt in flow.forward_packets :
        if TCP in pkt :
            size = len(pkt[TCP].payload)

        else:
            size = len(pkt)
        fwd_seg_size.append(size)

    for pkt in flow.backward_packets :
        if TCP in pkt :
            size = len(pkt[TCP].payload)
        else:
            size = len(pkt)
        bwd_seg_size.append(size)
    fwd_avg = sum(fwd_seg_size) / len(fwd_seg_size) if fwd_seg_size else 0
    bwd_avg = sum(bwd_seg_size) / len(bwd_seg_size) if bwd_seg_size else 0
    fwd_min = min(fwd_seg_size) if fwd_seg_size else 0

    return {
        "fwd_seg_size_avg":Decimal(fwd_avg),
        "bwd_seg_size_avg":Decimal(bwd_avg),
        "fwd_seg_size_min":Decimal(fwd_min)
    }