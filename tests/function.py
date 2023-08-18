# Python 3.7
import json
from typing import List


def celestial_bodies_temperatures(filename: str) -> List[List[str, int]]:
    return_list = []
    with open(filename) as f:
        data = json.load(f)
        for each_planet in data:
            return_list.append(
                [each_planet["name"],
                 int(each_planet["surfaceTemperature"])]
            )
    return return_list