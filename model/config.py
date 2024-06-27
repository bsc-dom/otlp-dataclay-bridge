from typing import Any, Callable, Optional, TypeVar
from dataclay import DataClayObject, activemethod


MatchRule = tuple[str, Callable[[Any], bool], Any]


class ResourceConfiguration(DataClayObject):
    """Hold the configuration for a resource, including the rules to match it.
    
    The rules will be given in the form of a list of tuples, where each tuple
    contains the key to match, a function to match the value, and the value to
    match.

    Example:

    >>> rc = ResourceConfiguration("test", [("key", operator.eq, 1)])
    
    Which will match any resource with the key "key" and value 1. All operator.*
    functions are supported.

    Every ResourceConfiguration will result in a DataFrame (managed in the main
    bridge application). This object also holds the set of metric names that are
    being collected for this resource.
    """
    name: str
    rules: list[MatchRule]
    metric_names: set[str]

    def __init__(self, name: str, rules: Optional[list[MatchRule]] = None, metric_names: Optional[set[str]] = None):
        self.name = name
        self.rules = rules or []
        self.metric_names = metric_names or set()

    @activemethod
    def add_metric(self, metric_name: str):
        self.metric_names.add(metric_name)
    
    @activemethod
    def remove_metric(self, metric_name: str):
        self.metric_names.remove(metric_name)

    @activemethod
    def match(self, resource_kvs: dict[str, str]) -> bool:
        for rule in self.rules:
            key, matcher, value = rule
            for k, v in resource_kvs.items():
                if k == key and not matcher(v, value):
                    return False
        return True


class BridgeConfiguration(DataClayObject):
    """Aggregate the configuration for the bridge.
    
    This class holds the configuration for the bridge, including the resource
    configuration objects. It also holds the time-to-live for the dataframes.
    """
    resource_configurations: dict[str, ResourceConfiguration]
    dataframe_ttl: int

    def __init__(self):
        self.resource_configurations = {}
        self.dataframe_ttl = 60

    @activemethod
    def set_res_config(self, rc: ResourceConfiguration):
        self.resource_configurations[rc.name] = rc

    @activemethod
    def remove_res_config(self, name: str):
        del self.resource_configurations[name]

    @activemethod
    def get_matching_res_configs(self, resource_kvs: dict[str, str]) -> list[ResourceConfiguration]:
        return [rc for rc in self.resource_configurations.values() if rc.match(resource_kvs)]
