import logging
from reader.pcap_reader import extract_packets,extract_flows
from flow.flow_builder import build_flows
from features import extract_all_feactures
from output.writer import write_csv
from config import PCAP_PATH,OUTPUT_PATH

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info(" Start processing PCAP file ...")

    packets = extract_packets(PCAP_PATH)
    raw_flows_dict = extract_flows(packets=packets)
    logging.info(f"read raw flows: {len(raw_flows_dict)} keys")



    flow_objects = build_flows(raw_flows_dict=raw_flows_dict)
    logging.info(f"Built {len(flow_objects)} flow objects")


    all_features = []
    for flow in flow_objects:
        features = extract_all_feactures(flow=flow)
        
        all_features.append(features)
    logging.info(f"Extracted features from {len(all_features)} flows")

    
    write_csv(all_features)
    logging.info(f"Features writtin to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()