import json
import logging
logging.basicConfig(level=logging.INFO)
path = '../data/parameters.json'
'''
This method is responsible for converting the json file into 
a dictonary 
'''
def get_json_data(path):
    '''
    :param path: We pass the relative path from the file we call the function
    :return:
    '''
    logging.info(100*'*')
    logging.info("File:Read_json.py method:get_json_data")
    file = open(path)
    data = json.load(file)
    logging.info("file opened successfully")
    logging.info("Exiting File:Read_json.py method:get_json_data")
    logging.info(100*'*')
    return data
