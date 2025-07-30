import numpy as np
from decimal import Decimal

def extract(flow):
    """
    Extract inter-arrival time statistics for the flow in both directions
    """
    # Helper function to calculate IAT statistics
    def calculate_iat_stats(timestamps):
        if len(timestamps) < 2:
            return {
                'tot': Decimal(0),
                'mean': Decimal(0),
                'std': Decimal(0),
                'max': Decimal(0),
                'min': Decimal(0)
            }
        
        # Convert timestamps to float first to avoid numpy types
        timestamps = [float(ts) for ts in timestamps]
        iats = np.diff(timestamps)
        iats = iats[iats >= 0]  # Remove negative values if any
        
        if len(iats) == 0:
            return {
                'tot': Decimal(0),
                'mean': Decimal(0),
                'std': Decimal(0),
                'max': Decimal(0),
                'min': Decimal(0)
            }
        
        # Convert numpy values to Python native types first
        return {
            'tot': Decimal(float(np.sum(iats))),
            'mean': Decimal(float(np.mean(iats))),
            'std': Decimal(float(np.std(iats))),
            'max': Decimal(float(np.max(iats))),
            'min': Decimal(float(np.min(iats)))
        }
    
    # Calculate overall IAT statistics
    flow_stats = calculate_iat_stats(flow.timestamps)
    
    # Calculate forward IAT statistics
    fwd_stats = calculate_iat_stats(flow.forward_timestamps)
    
    # Calculate backward IAT statistics
    bwd_stats = calculate_iat_stats(flow.backward_timestamps)
    
    return {
        # Flow IAT features
        "flow_iat_tot": flow_stats['tot'],
        "flow_iat_mean": flow_stats['mean'],
        "flow_iat_std": flow_stats['std'],
        "flow_iat_max": flow_stats['max'],
        "flow_iat_min": flow_stats['min'],
        
        # Forward IAT features
        "fwd_iat_tot": fwd_stats['tot'],
        "fwd_iat_mean": fwd_stats['mean'],
        "fwd_iat_std": fwd_stats['std'],
        "fwd_iat_max": fwd_stats['max'],
        "fwd_iat_min": fwd_stats['min'],
        
        # Backward IAT features
        "bwd_iat_tot": bwd_stats['tot'],
        "bwd_iat_mean": bwd_stats['mean'],
        "bwd_iat_std": bwd_stats['std'],
        "bwd_iat_max": bwd_stats['max'],
        "bwd_iat_min": bwd_stats['min']
    }