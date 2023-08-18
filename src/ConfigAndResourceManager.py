import configparser
import importlib.resources as pkg_resources
import json
import os
from functools import lru_cache
from typing import Union, TypeVar, Optional, Any
from src import resources



T = TypeVar("T")

class ConfigAndResourcesManager:
    def __init__(self):
        self._config_parser = configparser.ConfigParser()

    def read_config_file_resource(self, resource_file_name: str) -> None:
        self.read_config_string(ConfigAndResourcesManager.get_contents_of_resource_file(resource_file_name))

    def read_config_string(self, config_string: str) -> None:
        self._config_parser.read_string(config_string)

    @staticmethod
    def get_contents_of_resource_file(resource_file_name: str) -> str:
        # return (pkg_resources.files (resources) / resource_file_name).read_text(encoding='utf-8')
        return pkg_resources.files(resources).joinpath(resource_file_name).read_text(encoding='utf-8')


#     def get_config_value(self, config_grp: str, config_item: str, fallback: T = None) -> Union[str,T]:
#         overridden_value = os.environ.get(f"CONFIG {config_grp}_{config_item}")
#         if overridden_value is not None:
#             return overridden_value
#         return self._config_parser.get(config_grp, config_item, fallback = fallback)
#
#     get = get_config_value
#
#     @lru_cache(maxsize=64)
#     def get_contents_of_config_file_item(self, config_grp: str, config_item: str)-> Optional[str]:
#         resource_abs_path = self.get(config_grp, config_item + '_ABSPath')
#         if resource_abs_path is not None:
#             with open(resource_abs_path, 'rt', encoding='utf-8') as f:
#                 return f.read()
#         else:
#             resource_file_name = self.get(config_grp, config_item)
#             if resource_file_name is None:
#                 return None
#
#             return self.get_contents_of_resource_file(resource_file_name)
#
#     @lru_cache(maxsize=256)
#     def get_value_from_config_map_file_item(self, config_grp: str, config_item: str, key: str) -> Optional[Any]:
#         file_contents = self.get_contents_of_config_file_item(config_grp, config_item)
#         return ConfigAndResourcesManager._get_value_from_nap_str(file_contents, key)
#
#     @lru_cache(maxsize=256)
#     def get_value_from_map_resource(self, resource_file_name: str, key: str) -> Optional[Any]:
#         file_content = self.get_contents_of_resource_file(resource_file_name)
#         return ConfigAndResourcesManager._get_value_from_map_str(file_content, key)
#
#     @staticmethod
#     def get_value_from_map_str(map_str: str, key: str) -> Optional[Any]:
#         if map_str is None:
#             return None
#         return json.Loads(map_str).get(key)
#
# def _setup_config_and_resources_manager() -> ConfigAndResourcesManager:
#     manager = ConfigAndResourcesManager()
#     manager.read_config_file_resource('application.ini')
#     env="dev"
#     if os.environ.get("ENVIRONMENT") is not None:
#         env = os.environ["ENVIRONMENT"]
#     manager.read_config_file_resource(f'application-(env).ini')
#     overridden_configs = manager.get_contents_of_config_file_iten('ConfigFiles', 'application-overrides.ini')
#     if overridden_configs is not None:
#         manager.read_config_string(overridden_configs)
#     return manager
#
# config_and_resources_manager: ConfigAndResourcesManager = _setup_config_and_resources_manager()