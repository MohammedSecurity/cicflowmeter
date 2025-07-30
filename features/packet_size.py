import numpy as np

def extract(flow):
    pkt_lengths = [len(pkt) for pkt in flow.packets]

    if not pkt_lengths:
        return {
            "pkt_size_avg":0,
            "pkt_len_var":0
        }
    return {
        "pkt_size_avg":round(np.mean(pkt_lengths),2),
        "pkt_len_var":round(np.var(pkt_lengths),2)
    }