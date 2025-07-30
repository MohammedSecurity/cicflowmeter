from decimal import Decimal
from scapy.layers.inet import TCP

def extract(flow):
    syn = ack = fin = rst = psh = urg = ece = cwr = 0
    fwd_psh = bwd_psh = fwd_urg = bwd_urg = 0

    # الحساب العام
    for pkt in flow.packets:
        if TCP in pkt:
            flags = int(pkt[TCP].flags)

            if flags & 0x01:
                fin += 1
            if flags & 0x02:
                syn += 1
            if flags & 0x04:
                rst += 1
            if flags & 0x08:
                psh += 1
            if flags & 0x10:
                ack += 1
            if flags & 0x20:
                urg += 1
            if flags & 0x40:
                ece += 1
            if flags & 0x80:
                cwr += 1

    # PSH و URG لكل اتجاه
    for pkt in flow.forward_packets:
        if TCP in pkt:
            flags = int(pkt[TCP].flags)
            if flags & 0x08:
                fwd_psh += 1
            if flags & 0x20:
                fwd_urg += 1

    for pkt in flow.backward_packets:
        if TCP in pkt:
            flags = int(pkt[TCP].flags)
            if flags & 0x08:
                bwd_psh += 1
            if flags & 0x20:
                bwd_urg += 1

    return {
        "fin_flag_cnt": Decimal(fin),
        "syn_flag_cnt": Decimal(syn),
        "rst_flag_cnt": Decimal(rst),
        "psh_flag_cnt": Decimal(psh),
        "ack_flag_cnt": Decimal(ack),
        "urg_flag_cnt": Decimal(urg),
        "ece_flag_cnt": Decimal(ece),
        "cwr_flag_cnt": Decimal(cwr),
        "fwd_psh_flags": Decimal(fwd_psh),
        "bwd_psh_flags": Decimal(bwd_psh),
        "fwd_urg_flags": Decimal(fwd_urg),
        "bwd_urg_flags": Decimal(bwd_urg),
    }
