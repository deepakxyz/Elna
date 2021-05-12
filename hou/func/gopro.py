import os
from hou.globals import BASE_PATH
from hou.utils.utils import cwd

class GoPro():

    @staticmethod
    def toRoot():
        cwd(BASE_PATH)