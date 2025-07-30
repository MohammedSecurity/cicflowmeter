from decimal import Decimal
import numpy as np

def compute_bulk_stats(packets,timestamps):
    if not packets or len(packets) < 2:
        return {
            "bytes_b_avg":Decimal(0),
            "pkts_b_avg":Decimal(0),
            "blk_rate_avg":Decimal(0)
        }
    BULK_THRESHOLD = 1.0
    block_sizes = []
    block_pkts = []
    block_times = []

    current_bytes = 0
    current_pkts = 0
    start_time = float(timestamps[0])

    for i in range(1,len(packets)):
        time_diff = float(timestamps[i]) - float(timestamps[i - 1])
        current_bytes += len(packets[i])
        current_pkts += 1

        if time_diff > BULK_THRESHOLD :
            block_sizes.append(current_bytes)
            block_pkts.append(current_pkts)
            block_times.append(float(timestamps[i])- start_time)

            current_bytes = 0
            current_pkts = 0
            start_time = float(timestamps[i])
    if current_pkts > 0:
        block_sizes.append(current_bytes)
        block_pkts.append(current_pkts)
        block_times.append(float(timestamps[-1]) - start_time )
    bytes_b_avg = float(np.mean(block_sizes)) if block_sizes else 0 
    pkts_b_avg = float(np.mean(block_pkts)) if block_pkts else 0
    blk_rate_avg = float(np.mean([b/t if t > 0 else 0 for b,t in zip(block_sizes,block_times)])) if block_sizes else 0

    return{
        "bytes_b_avg":Decimal(bytes_b_avg),
        "pkts_b_avg":Decimal(pkts_b_avg),
        "blk_rate_avg":Decimal(blk_rate_avg)
    }

def extract(flow):
    fwd_stats = compute_bulk_stats(flow.forward_packets,flow.forward_timestamps)
    bwd_stats = compute_bulk_stats(flow.backward_packets,flow.backward_timestamps)

    return {
        "fwd_bytes_b_avg":fwd_stats["bytes_b_avg"],
        "fwd_pkts_b_avg":fwd_stats["pkts_b_avg"],
        "fwd_blk_rate_avg":fwd_stats["blk_rate_avg"],
        "bwd_bytes_b_avg":bwd_stats["bytes_b_avg"],
        "bwd_pkts_b_avg":bwd_stats["pkts_b_avg"],
        "bwd_blk_rate_avg":bwd_stats["blk_rate_avg"]
    }
