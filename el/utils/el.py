import os
import re
import logging
from el.config.GLOBALS import CONFIG_FILE_PATH
from el.utils.read_dump import read_json, read_yaml


class el:

    # echo fucn to print and log information
    @classmethod
    def echo(cls,msg,lvl="INFO",log=False):
        final_msg = (f"{lvl}: {msg}")
        print(final_msg)
        
    # change the current working directory
    @classmethod
    def cwd(cls,path):
        os.chdir(path)
        # os.system('/bin/zsh')
        os.system('/bin/bash')



    @classmethod
    def log(cls, msg, level):
        logging.basicConfig(level=logging.DEBUG, filename='test.log', format='%(asctime)s -%(levelname)s -- %(message)s')
        logging.debug(f'Add {num1} + {num2} = {add_result}')

    
    @staticmethod
    def path(path):
        dir_name , file_name = os.path.split(path)
        last_folder, file = os.path.split(dir_name)
        raw, ext = os.path.splitext(file_name)
        path_out = [last_folder, file, raw, ext]
        return path_out


def current_show(path):
    i = os.path.split(path)
    print(i)


class Path():
    config = read_yaml(CONFIG_FILE_PATH)
    show_base_path = config['base_show_path']

    @classmethod
    def show_name(cls,path):
        if cls.show_base_path in path:
            show_name = re.sub(cls.show_base_path, '', path)
            show_name = show_name.split('/')
            if len(show_name) <= 1:
                return None
            else:
                show_name.pop(0)
                output = os.path.join(cls.show_base_path, show_name[0])
                return output
        else:
            el.echo('''
            You are not the show level.
            Use the command  'el goshow' to move to the show level.

            ''',lvl="ERROR")

