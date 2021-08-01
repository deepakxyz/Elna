import os
from time import gmtime, strftime

from el.core.levels import Level
from el.utils.read_dump import read_json, dump_json
from el.utils.el import el, Path


class CreateAsset():

    asset_types = ['char', 'env', 'matte', 'prop']
    asset_build_sub_dir = ['cfx', 'fx','groom', 'lookDev', 'model', 'reference', 'renders', 'rig', 'rnd', 'temp', 'zfile', 'tex','cache', 'anim','comp'] 
    # TODO: Have to find a way to publish zfiles and textures
    asset_sub_dir = ['cfx', 'fx','groom', 'lookDev', 'model', 'renders', 'rig', 'zfile', 'tex', 'anim','comp'] # cfx and fx will the setup publishes



    @classmethod
    def check(cls):
        Check = Level.check()
        return Check

    @classmethod
    def check_if_exists(cls,asset_name, type):

        asset_path = os.path.join(os.getcwd(), 'asset_build', type, asset_name)
        if not os.path.isdir(asset_path):
            return True
        else:
            return False

    # creating directories under asset build folder 
    @classmethod
    def create_directory(cls,asset_name,type,desc):

        # base show directory
        show_directory = os.getcwd()

        # check asset name for spaces
        asset_name = asset_name.replace(' ', '-')


        # create asset directory
        asset_directory_path = os.path.join(show_directory, 'asset_build', type, asset_name)
        os.mkdir(asset_directory_path)

        # create sub directory
        for dir in cls.asset_build_sub_dir:
            path = os.path.join(asset_directory_path, dir)
            os.mkdir(path)

        # add data to asset_build.lv file
        asset_build_lv_file = os.path.join(show_directory, 'asset_build', 'asset_build.lv')
        created_on = strftime("%d %b %Y", gmtime())

        asset_details = {"name": asset_name,
        "created-on":created_on,
        "publishes":[],
        "build_files":{
            "zfile":[],
            "model":[],
            "rig":[],
            "animation":[],
            "groom":[],
            "cfx":[],
            "fx":[],
            "lookDev":[],
            "comp":[]
        }
        }

        data = read_json(asset_build_lv_file)
        data['assets'][type].append(asset_details)

        # dump data
        dump_json(asset_build_lv_file, data)

        asset_lvl_file_path = os.path.join(asset_directory_path, 'asset.lvl')
        
        dump_json(asset_lvl_file_path, asset_details)


    # creating directories under asset folder 
    @classmethod
    def create_asset_directory(cls, asset_name,type,desc):
        # base show directory
        show_directory = os.getcwd()

        # check asset name for spaces
        asset_name = asset_name.replace(' ', '-')


        # create asset directory
        asset_directory_path = os.path.join(show_directory, 'assets', type, asset_name)
        os.mkdir(asset_directory_path)

        # create sub directory
        for dir in cls.asset_sub_dir:
            path = os.path.join(asset_directory_path, dir)
            os.mkdir(path)

        # add data to asset_build.lv file
        asset_lv_file = os.path.join(show_directory, 'assets', 'asset.lv')
        created_on = strftime("%d %b %Y", gmtime())

        asset_details = {"name": asset_name,
        "created-on":created_on,
        "publishes":{
            "zfile":[],
            "model":[],
            "rig":[],
            "animation":[],
            "groom":[],
            "cfx":[],
            "fx":[],
            "lookDev":[]
        }
        }

        '''
        model: alembic / usd / obj
        rig: Maya file / nxt-script
        animation: Maya file
        groom: houdini file
        cfx: houdini file / Ziva (maya file)
        fx: houidni file
        lookDev: houdini / katana / maya

        '''

        data = read_json(asset_lv_file)
        data['assets'][type].append(asset_details)

        # dump data
        dump_json(asset_lv_file, data)

        asset_lvl_file_path = os.path.join(asset_directory_path, 'asset.lvl')
        
        dump_json(asset_lvl_file_path, asset_details)


class Asset():

    @classmethod
    def check(cls):
        if Level.check():
            return True
        elif Level.check('asset_build'):
            return True
        else:
            return False
    
    # read the asset file

    @classmethod
    def asset_list(cls):

        # get current show name
        show_name = Path.show_name(os.getcwd())
        if show_name:
            path =os.path.join(show_name, 'asset_build', 'asset_build.lv')
            data = read_json(path)
            for asset in data['assets']:
                p_data_1 = f'''
                {asset} '''
                print(p_data_1)
                for i in data['assets'][asset]:
                    print_data = f'''
                    Name: {i['name']}
                    Created-on: {i['created-on']}
                    Publishes: {i['publishes']}
                    Command:
                    el asset -t {asset} -a {i['name']}
                    -----------------------------
                    '''
                    print(print_data)

    @classmethod
    def go_asset(cls,cat, asset_name):
        path = os.path.join(os.getcwd(),'asset_build', cat, asset_name)
        if os.path.isdir(path):
            el.cwd(path)
        else:
            el.echo("The asset doesn't exsits under this category.",lvl="ERROR")


