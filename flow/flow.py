import logging
from scapy.layers.inet import IP, TCP, UDP
logger = logging.getLogger(__name__)


class Flow:
    def __init__(self, packets, timestamps, key):
        self.packets = packets
        self.timestamps =timestamps
        self.key = key

        self.src_ip = key[0]
        self.dst_ip = key[1]
        self.src_port = key[2]
        self.dst_port = key[3]
        self.protocol = key[4]

        self.forward_packets = []
        self.backward_packets = []
        self.forward_timestamps = []
        self.backward_timestamps = []
        self._split_directions()
        self.flow_duration = self.calculate_durations()
    def calculate_durations(self):
        if not self.timestamps:
            return 0.0
        return float(self.timestamps[-1] - self.timestamps[0])
    def _split_directions(self):

        for pkt, ts in zip(self.packets, self.timestamps ):
            if pkt.haslayer(IP):
                if pkt[IP].src == self.src_ip and pkt[IP].dst == self.dst_ip:
                    self.forward_packets.append(pkt)
                    self.forward_timestamps.append(ts)
                elif pkt[IP].src == self.dst_ip and pkt[IP].dst == self.src_ip:
                    self.backward_packets.append(pkt)
                    self.backward_timestamps.append(ts)
                

    """Object representing a network stream contanting the packages and related inforation """
    def get_feacture_dict(self, feature_extractors):
        features = {
            "src_ip":self.src_ip,
            "dst_ip": self.dst_ip,
            "src_port":self.src_port,
            "dst_port":self.dst_port,
            "protocol":self.protocol,
        }
        for extractor in feature_extractors:
            try:
                
                extracted = extractor.extract(self)
                features.update(extracted)
            except Exception as e:
                logger.warning(f"failed to extract features from {e} : {extractor.__name__} ")
        return features