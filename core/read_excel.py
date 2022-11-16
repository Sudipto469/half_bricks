import pandas as pd
# read by default 1st sheet of an excel file
path = '../data/'
fileName = 'Tables.xlsx'
path_modified = path+fileName
def generate_csv(path,Table_name):
    dataframe= pd.read_excel(path)
    dataframe.to_csv('../data/'+Table_name)
    print(dataframe)

generate_csv(path_modified,"Far_ratio.csv")


