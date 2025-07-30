from decimal import Decimal

def extract(flow):
    fwd_pkt_lengths = [len(pkt) for pkt in flow.forward_packets]
    bwd_pkt_lengths = [len(pkt) for pkt in flow.backward_packets]

    fwd_total_bytes = sum(fwd_pkt_lengths)
    bwd_total_bytes = sum(bwd_pkt_lengths)

    fwd_total_pkts = len(flow.forward_packets)
    bwd_total_pkts = len(flow.backward_packets)

    down_up_ratio = (bwd_total_bytes / fwd_total_bytes) if fwd_total_bytes > 0 else 0

    return {
        "down_up_ratio":Decimal(down_up_ratio),
        "fwd_bytes_b_avg":Decimal(fwd_total_bytes / fwd_total_pkts if fwd_total_pkts > 0 else Decimal(0)),
        "fwd_pkts_b_avg":Decimal(fwd_total_pkts / fwd_total_bytes if fwd_total_bytes > 0 else Decimal(0)),
        "bwd_bytes_b_avg":Decimal(bwd_total_bytes / bwd_total_pkts if bwd_total_pkts > 0 else Decimal(0)),
        "bwd_pkts_b_avg":Decimal(bwd_total_pkts / bwd_total_bytes if bwd_total_bytes > 0 else Decimal(0))
    }