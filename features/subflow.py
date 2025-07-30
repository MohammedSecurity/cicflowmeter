from decimal import Decimal

def extract(flow):
    subflow_fwd_pkts = len(flow.forward_packets)
    subflow_bwd_pkts = len(flow.backward_packets)

    subflow_fwd_bytes = sum(len(pkt) for pkt in flow.forward_packets)
    subflow_bwd_bytes = sum(len(pkt ) for pkt in flow.backward_packets)

    return {
        "subflow_fwd_pkts":Decimal(subflow_fwd_pkts),
        "subflow_fwd_bytes":Decimal(subflow_fwd_bytes),
        "subflow_bwd_pkts":Decimal(subflow_bwd_pkts),
        "subflow_bwd_bytes":Decimal(subflow_bwd_bytes)
    }