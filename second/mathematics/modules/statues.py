class PointCircleStatues:
    inCircle = -1
    onCircle = 0
    outCircle = 1

class LineCircleStatues:
    cutCircle = 1
    crossCircle = 2
    drawCircle = 3
    isRadius = 4
    isDiameter = 5
    isChord = 6
    inCircle = 7
    overCircle = 8
    statueError = 9

pointStatuesDic = {-1:'inCircle', 0:'onCircle', 1:'outCircle'}
lineStatuesDic = {1:'cutCircle', 2:'crossCircle', 3:'drawCircle', 4:'isRadius', 5:'isDiameter', 6:'isChord', 7:'inCircle', 8:'overCircle', 9:'statueError'}