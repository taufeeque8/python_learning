class ClusterInfo:
    def __init__(self, status: str, cluster_num: int, cluster_properties_file: str ):
        self.status =status
        self.cluster_num= cluster_num
        self.cluster_properties_file= cluster_properties_file

    @property
    def is_active(self) -> bool:
        return self.status == "ACTIVE"

    @property
    def is_inactive(self) -> bool:
        return not self.is_active
