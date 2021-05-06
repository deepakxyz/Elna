import os

class el:

    # echo fucn to print and log information
    @classmethod
    def echo(cls,msg,lvl="INFO",log=False):
        final_msg = (f"{lvl}: {msg}")
        print(final_msg)
        

    @classmethod
    def cwd(cls,path):
        os.chdir(path)
        os.system('/bin/bash')