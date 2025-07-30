from flow.flow import Flow
import logging

logger = logging.getLogger(__name__)


def build_flows(raw_flows_dict):
    """convert dictionary of packet to enitite flow"""
    flow_objects = []
    for key,pkt_list in raw_flows_dict.items():
        packets = []
        timestamps = []
        for pkt, ts in pkt_list :
            packets.append(pkt)
            timestamps.append(ts)
        
        flow_obj = Flow(packets=packets, timestamps=timestamps, key=key)
        
        flow_objects.append(flow_obj)
    logger.info(f"{len(flow_objects)}streaming objects were built .")
    return flow_objects