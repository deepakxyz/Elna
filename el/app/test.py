import os.path, time
file = r"Y:\pipeline\Shows\little_lines\asset_build\char\dav\model\head_model_v002.mb"
file_2 = r"Y:\pipeline\Shows\little_lines\asset_build\char\dav\model\head_model_v001.mb"
# print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))


f_modefied = os.path.getmtime(file_2)

modeified = os.path.getmtime(file)
c_time = (time.ctime(modeified))
# print(f_modefied < modeified)


import glob
import os

files = [file, file_2]
files.sort(key=os.path.getmtime)
print("\n".join(files))