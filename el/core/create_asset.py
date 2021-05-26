import os
from time import gmtime, strftime
from el.core.levels import Level
from el.utils.read_dump import read_json, dump_json



class CreateAsset():

    asset_types = ['char', 'env', 'matte', 'prop']
    asset_sub_dir = ['cfx', 'fx','groom', 'lookDev', 'model', 'reference', 'renders', 'rig', 'rnd', 'temp', 'zfile', 'tex'] 

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

    @classmethod
    def create_directory(cls,asset_name,type,desc):

        # base show directory
        show_director = os.getcwd()

        # create asset directory
        asset_directory_path = os.path.join(show_director, 'asset_build', type, asset_name)
        os.mkdir(asset_directory_path)

        # create sub directory
        for dir in cls.asset_sub_dir:
            path = os.path.join(asset_directory_path, dir)
            os.mkdir(path)

        # add data to asset_build.lv file
        asset_build_lv_file = os.path.join(show_director, 'asset_build', 'asset_build.lv')
        created_on = strftime("%d %b %Y", gmtime())

        asset_details = {"name": asset_name,
        "created-on":created_on,
        "pulishes":[]
        }

        data = read_json(asset_build_lv_file)
        data['assets'][type].append(asset_details)

        # dump data
        dump_json(asset_build_lv_file, data)
        

        






