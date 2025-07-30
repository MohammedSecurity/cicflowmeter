
import numpy as np
from decimal import Decimal

def extract(flow):
    # All packets
    pkt_lengths = [len(pkt) for pkt in flow.packets]

    # Forward packets
    fwd_lengths = [len(pkt) for pkt in flow.forward_packets]
    # Backward packets
    bwd_lengths = [len(pkt) for pkt in flow.backward_packets]

    result = {}

    # General stats (all packets)
    result["pkt_len_min"] = int(np.min(pkt_lengths)) if pkt_lengths else 0
    result["pkt_len_max"] = int(np.max(pkt_lengths)) if pkt_lengths else 0
    result["pkt_len_mean"] = round(np.mean(pkt_lengths), 2) if pkt_lengths else 0
    result["pkt_len_std"] = round(np.std(pkt_lengths), 2) if pkt_lengths else 0
    result["pkt_len_var"] = round(np.var(pkt_lengths), 2) if pkt_lengths else 0
    result["pkt_size_avg"] = round(np.mean(pkt_lengths), 2) if pkt_lengths else 0

    # Forward stats
    result["totlen_fwd_pkts"] = int(np.sum(fwd_lengths)) if fwd_lengths else 0
    result["fwd_pkt_len_max"] = int(np.max(fwd_lengths)) if fwd_lengths else 0
    result["fwd_pkt_len_min"] = int(np.min(fwd_lengths)) if fwd_lengths else 0
    result["fwd_pkt_len_mean"] = round(np.mean(fwd_lengths), 2) if fwd_lengths else 0
    result["fwd_pkt_len_std"] = round(np.std(fwd_lengths), 2) if fwd_lengths else 0

    # Backward stats
    result["totlen_bwd_pkts"] = int(np.sum(bwd_lengths)) if bwd_lengths else 0
    result["bwd_pkt_len_max"] = int(np.max(bwd_lengths)) if bwd_lengths else 0
    result["bwd_pkt_len_min"] = int(np.min(bwd_lengths)) if bwd_lengths else 0
    result["bwd_pkt_len_mean"] = round(np.mean(bwd_lengths), 2) if bwd_lengths else 0
    result["bwd_pkt_len_std"] = round(np.std(bwd_lengths), 2) if bwd_lengths else 0

    return {k: Decimal(v) for k, v in result.items()}
