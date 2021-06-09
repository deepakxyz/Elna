import os
from time import gmtime, strftime
from el.utils.read_dump import read_json, dump_json
from el.core.levels import Level

# move to base directory

class CreateShow():
    def __init__(self,base_dir,show_name):

        self.base_dir = base_dir
        self.show_name = show_name

        # check has already been done by check() at the cli state
        self.create_directories()


    # check if the show name already exists
    @staticmethod
    def check(base_dir, show_name):
        if os.path.isdir(os.path.join(base_dir, show_name)):

            print(f'The project already exists by the name {show_name}')
            print('Please try it with an other name.')
            return False
        
        else:
            return True


    
    def create_directories(self):

        # create show folder
        show_dir = os.path.join(self.base_dir, self.show_name)
        os.mkdir(show_dir)

        # create asset-build and sub-directory
        self.asset_build_dir = os.path.join(show_dir, "asset_build")
        os.mkdir(self.asset_build_dir)

        self.asset_dir = os.path.join(show_dir, 'assets')
        os.mkdir(self.asset_dir)

        # create asset_build sub-directories
        asset_cat_list = ['char','env','matte','prop']
        for asset_cat_dir in asset_cat_list:
            
            # asset build directory
            asset_build_cat_dir_path = os.path.join(self.asset_build_dir, asset_cat_dir)
            os.mkdir(asset_build_cat_dir_path)

            # asset directory
            asset_cat_dir_path = os.path.join(self.asset_dir, asset_cat_dir)
            os.mkdir(asset_cat_dir_path)

        # create  directory [ asset, sequences, references, globals, scripts]
        other_dir_list = ["shots","houdini","maya", "references", "globals", "scripts", "docs", "shaders", "editorial"]
        for cat in other_dir_list:
            other_dir = os.path.join(show_dir, cat)
            os.mkdir(other_dir)


        # create

    def create_level_files(self):

        # asset build level file
        asset_build = {"assets":{
            "char":[],
            "env":[],
            "matte":[],
            "prop":[]
        }}

        # create asset_build level file
        asset_build_level_file = os.path.join(self.asset_build_dir, "asset_build.lv")
        dump_json(asset_build_level_file, asset_build)

        # create asset level file
        asset_level_file = os.path.join(self.asset_dir, "asset.lv")
        dump_json(asset_level_file, asset_build)



    def add_to_json(self, short_name, desc):

        time = strftime("%d %b %Y", gmtime())
        data = {"name":self.show_name, "short-name":short_name, "description":desc, "created-on":time}

        # adding to main json file
        path = os.path.join(self.base_dir, 'Shows.json')
        read_data = read_json(path)
        read_data['shows'].append(data)
        dump_json(path, read_data)

        # add show level file
        show_level_file = os.path.join(self.base_dir, self.show_name, "show.lv")
        dump_json(show_level_file, data)




    def msg(self):
        msg = f'''
        Project "{self.show_name}" successfully created.
        '''
        print(msg)



