def extract(flow):
    """
    extract the time for flow
    """
    if not flow.timestamps:
        return {"flow_duration":0}
    start = min(flow.timestamps)
    end = max(flow.timestamps)
    duration = end - start
    return {"flow_duration": round(duration,6)}
