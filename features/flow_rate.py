from decimal import Decimal

def extract(flow):
    total_bytes = sum(len(pkt) for pkt in flow.packets)
    duration = float(flow.flow_duration)
    if duration > 0:
        bytes_per_sec = total_bytes / duration
    else:
        bytes_per_sec = 0.0

    return {
        "flow_bytes_s":Decimal(bytes_per_sec)
    }