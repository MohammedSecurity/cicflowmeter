def extract(flow):
    fwd_bytes = sum(len(pkt) for pkt in flow.forward_packets)
    bwd_bytes = sum(len(pkt) for pkt in flow.backward_packets)

    ratio = 0
    if fwd_bytes != 0:
        ratio = round(bwd_bytes / fwd_bytes, 2)
    return {
        "down_up_ratio":ratio
    }