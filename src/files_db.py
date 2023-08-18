import os
from typing import Tuple


def get_doctype_and_paths(folder_mapping: Tuple[str, str, str, str, str],
    input_folder: str, temp_folder: str, processed_folder: str, error_folder: str, secondary_location: str) -> Tuple[
    str, str, str, str, str, str]:
    doc_type = folder_mapping[0]
    input_folder = os.path.join(input_folder, folder_mapping[1])
    transient_folder = os.path.join(temp_folder, folder_mapping[2])
    success_folder = os.path.join(processed_folder, folder_mapping[3])
    error_folder = os.path.join(error_folder, folder_mapping[4])
    if secondary_location is not None:
        secondary_location = os.path.join(secondary_location, folder_mapping[1])
    return doc_type, input_folder, transient_folder, success_folder, error_folder, secondary_location























