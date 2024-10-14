#This mode consist of function which returns the path of generated file
import os
def get_path(name):
    '''This function returns the path of generated report'''
    desktop = os.path.expanduser("~\Desktop")
    path=(f'{desktop}\{name}.txt')
    return path
