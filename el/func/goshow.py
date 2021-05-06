import os
from el.utils.read_dump import read_yaml
from el.config.GLOBALS import CONFIG_FILE_PATH
from el.utils.el import el


class GoShow():
    
    @staticmethod
    def toRoot():
        # change directory
        read_config = read_yaml(CONFIG_FILE_PATH)
        el.cwd(read_config['base_show_path'])

# el.cwd('/mnt/x/')