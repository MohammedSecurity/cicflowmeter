from decimal import Decimal

def extract(flow):
    src_ip , dst_ip , src_port , dst_port , protocol = flow.key
    return {
        "dst_port": Decimal(dst_port),
        "protocol": Decimal(protocol),
        "timestamp": Decimal(float(flow.timestamps[0])) if flow.timestamps else Decimal(0)
    }