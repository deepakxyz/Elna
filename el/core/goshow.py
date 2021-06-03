import os
from el.utils.read_dump import read_yaml, read_json
from el.config.GLOBALS import CONFIG_FILE_PATH
from el.utils.el import el


class GoShow():

    config = read_yaml(CONFIG_FILE_PATH)
    show_base_path = config['base_show_path']
    
    # move to root directory
    @classmethod
    def toRoot(cls):
        # change directory
        cls.read_config = read_yaml(CONFIG_FILE_PATH)
        el.cwd(cls.read_config['base_show_path'])

    @classmethod
    # get shows list
    def goshow_data(cls):
        # show file path
        cls.read_config = read_yaml(CONFIG_FILE_PATH)
        cls.shows_json_file_path = os.path.join(cls.read_config['base_show_path'], 'Shows.json')
        cls.show_json_data = read_json(cls.shows_json_file_path)
        return cls.show_json_data
        
    @classmethod
    def goshow_list(cls):
        data = cls.goshow_data()
        for show in data['shows']:
            info = f'''
                Show Name: {show['name']}
                Show Short Name: {show['short-name']}
                Description: {show['description']}
                Created on: {show['created-on']}
                Command:
                el goshow {show['name']}
            '''
            print(info)

    @classmethod
    def goshow(cls, showname):
        data = cls.goshow_data()

        # check if the show exists
        shows = []
        for j_showname in data['shows']:
            shows.append(j_showname['name'])

        if showname in shows:
            el.echo(f"Moving to show '{showname}'")
            el.echo('Currently under show level')

            show_path = os.path.join(cls.show_base_path, showname)
            el.cwd(show_path)

        else:
            el.echo(f"Show by the name '{showname}' does not exists.")