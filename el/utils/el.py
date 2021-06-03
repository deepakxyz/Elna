import os
import logging


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



path = '/mnt/y/pipeline/Shows/Mayday/asset_build'
current_show(path)