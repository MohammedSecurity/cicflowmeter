import logging
from importlib import import_module

logger = logging.Logger(__name__)

FEATURE_MODULES = [
    "general",
    "duration",
    "packet_count",
    "packet_length",
    "flow_rate",
    "iat",
    "flags",
    "header",
    "fwd_bwd_rate",
    "packet_size",
    "direction_ratio",
    "segment_size",
    "bulk_rate",
    "subflow",
    "window",
    "fwd_data",
    "activity"
]
EXTRACTORS = []
for module_name in FEATURE_MODULES:
    try:
        module = import_module(f"features.{module_name}")
        if hasattr(module,"extract"):
            EXTRACTORS.append(module.extract)
        else:
            logger.warning(f"Module {module_name} does not have 'extract' function.")
    except Exception as e:
        logger.warning(f"Failed to import module {module_name} : {e}")

def extract_all_feactures(flow):
    all_features = {}
    for extractor in EXTRACTORS:
        try:
            features = extractor(flow)
            
            all_features.update(features)

        except Exception as e:
            logger.warning(f" Failed to extract features from  {extractor.__module__} : {e}")
    return all_features