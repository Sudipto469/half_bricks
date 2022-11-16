from vpython import *
import sys
from core.read_json import get_json_data
import logging
logging.basicConfig(level=logging.INFO)

'''
'''
def diagram(side, thk, front):
    '''

    :param side: Side of the plot
    :param thk: Thickness is obtained from json file
    :param front: Front of the plot
    :return:
    '''
    logging.info(100*"*")
    logging.info("File:Only Plot Method:Diagram")
    c1 = canvas(background=color.white)
    wallB = box(canvas = c1 ,pos=vector(0, 0, 0), size=vector(front,side,thk * 3), color=color.green,opacity=0.5)
    logging.info("Plot Created successfully")
    labl = label(canvas=c1, pos=wallB.pos, align="left",
                 text="Length:{} \nBreadth:{} "
                 .format(int(front), int(side), linewidth=0.001, yoffset=10000*thk, xoffset=4 * front
    ))
    logging.info("Plot label Created successfully")
    logging.info("Exiting File:Only Plot Method:Diagram")
    logging.info(100*"*")


if __name__ == '__main__':
    X = sys.argv
    relative_path ='\data\parameters.json'
    path = sys.path[0]+relative_path
    data = get_json_data(path)
    thk = data["Plot_thickness"]
    print(thk)
    front = float(X[1])
    side = float(X[2])
    diagram(side, thk, front)



