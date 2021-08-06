import os

path = r"Y:\pipeline\Shows\mayday\asset_build\prop\sn8\tex\head_panel\v001"

def base_dir_to_win_dir(path):
    splitStr = path.split('/')
    del splitStr[:2]
    splitStr[0] = (splitStr[0] + ":")
    h = "/".join(splitStr)
    h.strip()
    return h

# List dir 
EXT = ['.exr', '.tiff', '.jpg']

def txconvert(name):

	cwd = os.getcwd()
	cwd = base_dir_to_win_dir(cwd)
	raw, ext = os.path.splitext(name)
	if ext in EXT:
		original_path = os.path.join(cwd, name)
		tx_path = os.path.join(cwd, raw + ".tx")

		command = f'maketx -v -u --oiio --checknan --filter lanczos3 {original_path} -o {tx_path}'
		print(f'Converting: {name}')
		os.system(f'cmd.exe /c {command}')



def converter(name=None, all=True):
	if all and name==None:
		cwd = os.getcwd()
		files = [name for name in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, name))]
		if len(files) > 0:
			for file in files:
				txconvert(name=file)
			print(f'Convertion Done')

	if name and all==False:
		txconvert(name)
		print(f'Convertion Done')


