from dataclasses import dataclass

@dataclass
class Stats:
    endpoints: list
    all: int
    failed: int
    history: list
    most_endpoint: dict
    most_endpoints: list
    most_type: dict
    most_types: list
