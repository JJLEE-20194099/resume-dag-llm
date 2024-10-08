import math
def nan_2_none(obj):
    if isinstance(obj, dict):
        return {k:nan_2_none(v) for k,v in obj.items()}
    elif isinstance(obj, list):
        return [nan_2_none(v) for v in obj]
    elif isinstance(obj, float) and math.isnan(obj):
        return None
    return obj