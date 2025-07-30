from decimal import Decimal
from flow.flow import Flow

def extract(flow:Flow):
    tot_fwd_pkts = len(flow.forward_packets)
    tot_bwd_pkts = len(flow.backward_packets)
    flow_duration =float(flow.flow_duration)

    if flow_duration > 0:
        flow_pkts_s =(tot_fwd_pkts + tot_bwd_pkts ) / flow_duration
        fwd_pkts_s = tot_fwd_pkts / flow_duration
        bwd_pkts_s = tot_bwd_pkts / flow_duration
    else:
        flow_pkts_s = fwd_pkts_s = bwd_pkts_s = 0.0
    return {
        "tot_fwd_pkts":Decimal(tot_fwd_pkts),
        "tot_bwd_pkts":Decimal(tot_bwd_pkts),
        "flow_pkts_s":Decimal(flow_pkts_s),
        "fwd_pkts_s":Decimal(fwd_pkts_s),
        "bwd_pkts_s":Decimal(bwd_pkts_s)
    }

