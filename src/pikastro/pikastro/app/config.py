import dataclasses
import yaml


@dataclasses.dataclass
class Config:
    x_google_backend: str
    environment: str = "development"


def get_config_from_file(env):
    path_to_file = f"./configs/{env}.yaml"
    cfg_values = _load_config(path_to_file)
    return Config(**cfg_values)


def _load_config(file_path):
    with open(file_path, "r") as stream:
        try:
            config = yaml.safe_load(stream)
            return config
        except yaml.YAMLError as e:
            print(f"Error loading YAML file: {e}")
            return None
