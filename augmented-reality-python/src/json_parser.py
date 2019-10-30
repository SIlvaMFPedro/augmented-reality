# ------------------------
#   IMPORTS
# ------------------------
# Import the necessary packages
import json
from singleton import Singleton
from pprint import pprint


# ------------------------
#   JSON READER
# ------------------------
class JsonReader(Singleton):
    """
        Json Reader
    """
    def __init__(self):
        self.__json_data = None

    def read_from_file(self, path):
        """
        Read the JSON data from the file and convert it into a JSON string
        :param path: path to the JSON file
        :return: JSON string
        """
        with open(path, encoding='utf-8') as f:
            self.__json_data = json.load(f)

    def print_json(self):
        """
        Pretty print the data
        :return: None
        """
        pprint(self.__json_data)

    def get_value(self, key):
        """
        Return the value for given key in the JSON file
        :param key: Key as string in the JSON
        :return: value for the given key
        """
        return self.__json_data[key]
