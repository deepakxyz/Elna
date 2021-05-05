import os

# check if the directory exsists if not create
def create_dir(func):
    def wrapper(*args, **kwargs):
        arguments = kwargs
        if arguments['path'] and arguments['name']:
            path = os.path.join(arguments['path'],arguments['name'])
            if os.path.isdir(arguments['path']):
                print('The directory your trying to create already exists.')
                print(f'{path}')
            else:
                try:
                    os.mkdir(path)
                except:
                    print("DEBUG: Not enough argument to create the directory.")
                    print("DEBUG: The path is invalid.")
                    pass
    return wrapper

