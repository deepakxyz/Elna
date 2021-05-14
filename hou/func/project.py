import os
from hou.utils.utils import echo
from hou.utils.read_dump import read_json
from hou.globals import PRO_SUB_DIR

# lauch a blank file if there is not any .hip file
# if there is any, lauch the latest version of the .hip file

class Launch():

    @classmethod
    def scene_file(cls,hou_file_path):
        # list directory
        hou_file_data = read_json(hou_file_path)
        if len(hou_file_data['hip_files']) > 0:
            latest_file = hou_file_data['hip_files'][-1]
            # check if the last file exists
            cwd = os.getcwd()
            lastest_file_path = os.path.join(cwd, latest_file)
            if os.path.isfile(lastest_file_path):
                print(f'''
                Launching a the latest working file {latest_file}.
                Happy Hacking!
                ''')
                os.system(f"cmd.exe /c start houdini {latest_file}")
            
            else:
                echo(f"The file {latest_file} in the log data doesn't not exists in the directory.",lvl="WARNNING")
                echo("Please check the directory and update the log file.")

        else:
            echo('Launching a Blank Houdini file.')
            print('''
            Happy Hacking!
            ''')
            os.system("cmd.exe /c start houdini")

