import json
from typing import Union


def load_request_data(data: Union[str, dict]) -> dict:
    if isinstance(data, dict):
        data_loaded = data
    else:
        data_loaded = json.loads(data)
        
    return data_loaded