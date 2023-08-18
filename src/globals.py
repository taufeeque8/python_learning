import configparser
import os
from typing import Union, TypeVar

T = TypeVar("T")

class ConfigAndResourcesManager:
    def __init__(self):
        self._config_parser = configparser.ConfigParser()
    def read_config_file_resource(self, resource_file_name: str) -> None:
        self.read_config_string(ConfigAndResourcesManager.get_contents_of_resource_file(resource_file_name))

    def read_config_string(self, config_string: str) -> None:
        self._config_parser.read_string(config_string)

    @staticmethod
    def get_config_value(self, config_grp: str, config_item: str, resource_file_name: str , fallback : T= None) -> Union[T, str]:
        overridden_value = os.environ.get(f"CONFIG_{config_grp}_{config_item}")
        if overridden_value is not None:
            return overridden_value
        return  self._config_parser.get(config_grp,config_item,fallback =fallback)

    get = get_config_value

