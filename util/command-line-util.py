import sys


command_value_map = {}


class CommandLineUtil:
    def __init__(self):
        self.config = ConfigUtil('config/config.yaml')
        self.run()

    def run(self):
        args = sys.argv[1:]
        config_map = {}

        for arg in args:
            if '=' in arg:
                key, value = arg.split('=')
                config_map[key] = value

        self.config._global_config_map.update(config_map)

        print("Config loaded successfully")
        print("Config map:")
        for key, value in self.config._global_config_map.items():
            print(f"{key} = {value}")