import os
from el.utils.el import el
from el.utils.read_dump import dump_yaml, read_yaml

from el.config.GLOBALS import CONFIG_FILE_PATH



class Init():

    main_dir_name = "Shows"

    def __init__(self,base_path):
        self.base_path = base_path
        self.fullpath = os.path.join(self.base_path, Init.main_dir_name)

        # check and create the base directory
        self.initialize_dir()
        
        # if base directory is created then create all other utils.
        if self.output:

            self.create_data_base()
            self.add_config()

    def initialize_dir(self):

        # check if any other shows has been configured
        config_data = read_yaml(CONFIG_FILE_PATH)
        try:
            if config_data['base_show_path']:
                el.echo('You cannot Initialize a new "Shows" when a "Shows" directory already exists',lvl="ERROR")
                msg=f'''
                Current running "Shows" directory: {config_data['base_show_path']}
                Go the to current runnig "Show" by using the command 'el goshow'
                '''
                el.echo(msg=msg)
                self.output = False
        except:
            # check if the show directory already exists
            if not os.path.isdir(self.fullpath):
                os.mkdir(self.fullpath)
                self.output = True
            else:
                el.echo('Main Show directory already exists.')
                self.output = False

        return self.output        

    # creating database if self.initialize is True
    def create_data_base(self):

        el.echo('Creating database...')

        # database folder path
        cwd = os.path.join(self.fullpath, '_database') 
        # creating database folder
        os.mkdir(cwd)

        ## CREATE MAIN.CONFIG FILE
        # create config file in the show root directory
        main_config_path = os.path.join(self.fullpath,  'main.config') 
        os.system(f'touch {main_config_path}')

        # # dump the base data to config file
        data = {"base_show_path":self.fullpath} 
        dump_yaml(main_config_path, data)

        ## CREATE SHOWS.JSON FILE
        


        
    def add_config(self):
        # main config from el local base
        config_data = {"base_show_path":self.fullpath}
        dump_yaml(CONFIG_FILE_PATH, config_data)

        
