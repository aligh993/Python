# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import os
import pathlib

class FileManager:

    def create_dir(self, name, address):
        dir_path = address+'/'+name
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def create_file(self, name, address):
        file_path = address+'/'+name
        if not os.path.exists(file_path):
            with open(file_path, 'w'): pass

    def delete(self, name, address):
        file_path = address + '/' + name
        if os.path.exists(file_path):
            os.remove(file_path)

    def find(self, name, address):
        find_lst = list()
        for path, subdirs, files in os.walk(address):
            for n in files:
                if n == name:
                    find_lst.append(pathlib.PurePath(path, n).as_posix())
        return find_lst

    def restore(self, name):
        pass
