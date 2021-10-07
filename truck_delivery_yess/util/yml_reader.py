import yaml


class YmlReader:

    def __init__(self, file_path):
        yml_file = open(file_path)
        self.yml_load = yaml.load(yml_file, Loader=yaml.FullLoader)

    def get_var(self, key):
        return self.yml_load.get(key)
