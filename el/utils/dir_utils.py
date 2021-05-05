import os

# check if the directory exsists if not create
# decorator function
def create_dir(func):
    def wrapper(*args, **kwargs):
        arguments = kwargs
        if arguments['path'] and arguments['name']:
            path = os.path.join(arguments['path'],arguments['name'])
            # check if the base directory exists
            if os.path.isdir(arguments['path']):
                # check if the directory already exists.
                if not os.path.isdir(path):
                    os.mkdir(path)
                else:
                    try:
                        if arguments['type']:
                            dir_type = arguments['type']
                    except:
                        dir_type = 'directory'
                    print(f'WARNNING: The {dir_type} your trying to create already exists.')
                    print('')
            else:
                print('WARNNING: The base directory does not exists.')
                print(f'{path}')
            return func(**kwargs)
    return wrapper

