import os
import shutil
from hou.utils.read_dump import read_json, dump_json
from hou.utils.utils import echo

# read the houdini json file
# read hou file of the projects
class Otls:

    @staticmethod
    def check(base_path):
        # read houdini json file
        houdini_json_file_path = os.path.join(base_path,'houdini.json')
        houdini_json_data = read_json(houdini_json_file_path)

        for project in houdini_json_data['projects']:
            # hou file path of each project
            hou_file_path = os.path.join(base_path, project['name'],'hou')
            # if hou file exists
            if os.path.isfile(hou_file_path):
                # read hou file 
                hou_data = read_json(hou_file_path)
                
                for hou_otls in hou_data['otls']:
                    if not hou_otls in project['otls']:
                        project['otls'].append(hou_otls)
                        
                        otls_name = hou_otls['path'].split('/')
                        echo(f"Project: {project['name']}")
                        echo(f'New otls published > {otls_name[-1]}')
                        echo(f'Description: {hou_otls["description"]}')
                        print('')

                        # copy and paste file
                        target_file = os.path.join(base_path,'_otls',otls_name[-1])
                        original_file = hou_otls['path']

                        shutil.copyfile(original_file, target_file)


                dump_json(houdini_json_file_path, houdini_json_data)

            
            
            else:
                pro_name = project['name']
                echo(f'`hou` file does not exists in the project {pro_name}')

            # add data to houdini.json otls
            for otls in project['otls']:
                if not otls in houdini_json_data['otls']:
                    houdini_json_data['otls'].append(otls)


                dump_json(houdini_json_file_path, houdini_json_data)
        #update data  
        

    
    # print all the otls available
    @staticmethod
    def otls_list(base_path):
        # read houdini json file
        houdini_json_file_path = os.path.join(base_path,'houdini.json')
        houdini_json_data = read_json(houdini_json_file_path)

        for otls in houdini_json_data['otls']:
            otls_name = otls['path'].split('/')
            echo(f'New otls published > {otls_name[-1]}')
            echo(f'Description: {otls["description"]}')
            print('')

    # force update the project otls
    @staticmethod
    def otls_force_update(base_path,cwd):
        # read houdini json file
        houdini_json_file_path = os.path.join(base_path,'houdini.json')
        houdini_json_data = read_json(houdini_json_file_path)


        for project in houdini_json_data['projects']:
            # hou file path of each project
            echo('Force updating all the Otls in the current project.')
            for hou_otls in (project['otls']):
                otls_name = hou_otls['path'].split('/')
                echo(f"Project: {project['name']}")
                echo(f'New otls published > {otls_name[-1]}')
                echo(f'Description: {hou_otls["description"]}')
                print('')

                # copy and paste file
                target_file = os.path.join(base_path,'_otls',otls_name[-1])
                original_file = hou_otls['path']

                shutil.copyfile(original_file, target_file)