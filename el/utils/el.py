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
        os.system('/bin/bash')


    @classmethod
    def log(cls, msg, level):
        logging.basicConfig(level=logging.DEBUG, filename='test.log', format='%(asctime)s -%(levelname)s -- %(message)s')
        logging.debug(f'Add {num1} + {num2} = {add_result}')