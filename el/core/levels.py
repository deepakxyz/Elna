import os


class Level():
    # def __init__(self,cwd):
    #     self.cwd = cwd

    @classmethod
    def check(cls,level="Show"):
        cwd = os.getcwd()
        level_file = level + ".lv"
        file = os.path.join(cwd, level_file)

        if os.path.isfile(file):
            return True
        else:
            return False
