import os
import logging


# echo fucn to print and log information
def echo(msg,lvl="INFO",log=False):
    final_msg = (f"{lvl}: {msg}")
    print(final_msg)
        
# change the current working directory
def cwd(path):
    os.chdir(path)
    os.system('/bin/bash')


def log(msg, level):
    logging.basicConfig(level=logging.DEBUG, filename='test.log', format='%(asctime)s -%(levelname)s -- %(message)s')
    logging.debug(f'Add {num1} + {num2} = {add_result}')