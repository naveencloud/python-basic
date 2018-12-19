# OOPS Programming for Listing Directories

from os import listdir
from os.path import join, isdir, isfile #Join to find AbsolutePath
from pprint import pprint as pp
from json import dump # Dumping Output into JSON File


class ListOfDirectories:
    def __init__(self, *args): # *args --> Variable Length arguments
        self.list_of_directories = args
        self.container = dict()   # Empty dictionay, Populated content will be stored in Empty directory
        # print(self.list_of_directories)
        self.read_list_of_directories()  # It calls 'def read_list_of_directories(self)' function

    def get_abs_path_for_directory(self, dir_name):
        temp = []   # Empty List to append dir_name, file_item

        for file_item in listdir(dir_name):
            temp.append(join(dir_name, file_item))

        return temp

    def read_list_of_directories(self):
        for dir_name in self.list_of_directories: # it will look for directory in "args" in first section of code

            dir_content = self.get_abs_path_for_directory(dir_name) # it calls def "get_abs_path_for_directory(self, dir_name)"

            file_names = list(filter(isfile, dir_content))
            dir_names = list(filter(isdir, dir_content))
            self.container[dir_name] = dict(files=file_names, dirs=dir_names) # Key is files, dirs and it has corresponding value

    def to_json(self, json_file):   # it will populate Output into JSON
        dump(self.container, open(json_file, 'w'), indent=4) # Indent will add the indentation to json code

dictionary_library = ListOfDirectories('../../../dec182017')
dictionary_library.to_json('tmp.json')
pp(dictionary_library.container)