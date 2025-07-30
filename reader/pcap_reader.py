import logging
from collections import defaultdict
from scapy.all import rdpcap, IP, TCP, UDP, packet 
from datetime import datetime

# setting of operating log
logger = logging.getLogger(__name__)
logging.basicConfig(filename='logfile.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def extract_packets(pcap_file):
    try:
        packets = rdpcap(pcap_file)
        logger.info(f"Uploaded{len(packets)} packet from file : {pcap_file} ")
        return packets
    except Exception as e:
        logger.error(f"Failed to read the file :{pcap_file}")
        return []
    
def extract_flows(packets:packet, flow_timeout=10):
    """ Extract streams from packets using 5-tuple with idle time """
    flows = defaultdict(list)
    
    for pkt in packets:
        
        if IP in pkt:
            proto = pkt['IP'].proto
            src_ip =pkt['IP'].src
            dst_ip =pkt['IP'].dst
            if proto == 6 and TCP in pkt:
                src_port = pkt['TCP'].sport
                dst_port = pkt['TCP'].dport
            elif proto == 17 and UDP in pkt:
                src_port = pkt['UDP'].sport
                dst_port = pkt['UDP'].dport
        
            # Use 5-tuple as a streaming switch
            Key = (src_ip,dst_ip,src_port,dst_port,proto)
            timestamps = pkt.time
            flows[Key].append((pkt,timestamps))
        else:
                logger.info("only TCP , UDP protocols are supported")
    logger.info(f"it has been extracted{len(flows)} Unique stream.")
    return flows    
    
            
        
# resu = extract_packets("C:\\Users\\M-ALANEED\Desktop\\cybersecurity\\nashwan\copy\\nb6-http.pcap")
# print(f"numbers of packet :{len(resu)}")

# flows = extract_flows(resu)
# print(f"flows : {len(flows)}")

# for key in list(flows.keys())[:1]:
#     print(f" elament one of list : {key}")

