import sys
path = sys.path[0]+'\data\parameters.json'
# from core.read_json import get_json_data
print("path34",path)
from core.read_json import get_json_data
get_json_data(path)
