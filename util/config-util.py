import yaml


config_map = {}


class ConfigUtil:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=')
                    key = key.strip()
                    value = value.strip()
                    config_map[key] = value
            return yaml.safe_load(f)

    @staticmethod
    def get(key):
        return config_map.get(key)
