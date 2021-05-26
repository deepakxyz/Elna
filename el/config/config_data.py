import os
from el.utils.read_dump import read_yaml, dump_yaml
from el.config.GLOBALS import CONFIG_FILE_PATH 


class Config():

    @classmethod
    def base(cls):
        file_path = os.path.join(CONFIG_FILE_PATH)
        data = read_yaml(file_path)
        base_show_path = data['base_show_path']
        return base_show_path


