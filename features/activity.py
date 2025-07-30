import numpy as np
from decimal import Decimal

def extract(flow, idle_threshold=1.0):
    if len(flow.timestamps) < 2:
        return {
            "active_mean": Decimal(0),
            "active_std": Decimal(0),
            "active_max": Decimal(0),
            "active_min": Decimal(0),
            "idle_mean": Decimal(0),
            "idle_std": Decimal(0),
            "idle_max": Decimal(0),
            "idle_min": Decimal(0)
        }
    timestamps = [float(ts) for ts in flow.timestamps]
    timestamps.sort()
    iats = np.diff(timestamps)

    active_periods = []
    idle_periods = []
    current_active = []
    
    for iat in iats:
        if iat < idle_threshold:
            current_active.append(iat)
        else:
            if current_active:
                active_periods.append(sum(current_active))
                current_active = []
                
            idle_periods.append(iat)
            
    if current_active:
        active_periods.append(sum(current_active))
        

    def compute_stats(periods):
        
        if not periods :
            
            return (Decimal(0),Decimal(0),Decimal(0),Decimal(0))
       
        return {
            Decimal(np.mean(periods)),
            Decimal(np.std(periods,ddof=0)),
            Decimal(np.max(periods)),
            Decimal(np.min(periods))
        }
    
    active_mean , active_std ,active_max , active_min = compute_stats(active_periods)
    print("_______________________________________")
    idle_mean , idle_std , idle_max , idle_min = compute_stats(idle_periods)
    
    return {
        "active_mean": active_mean,
        "active_std":active_std,
        "active_max":active_max,
        "active_min":active_min,
        "idle_mean":idle_mean,
        "idle_std":idle_std,
        "idle_max":idle_max,
        "idle_min":idle_min
    }