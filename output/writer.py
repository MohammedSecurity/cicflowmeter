import csv
import logging 
import os 

logger = logging.Logger(__name__)

def write_csv(data,outputfile='flows.csv'):

    
    if not data:
        logger.warning("no data on pcap file.")
        return 
    fieldnames = list(data[0].keys())

    
    try:
        with open(outputfile,mode='w',newline='',encoding='utf-8') as csvfile:
            print(type(csvfile))
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
            
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        logger.info(f"ok to writed csv file")
    except Exception as e:
        logger.error(f"feiled to writing on file csv {e}")