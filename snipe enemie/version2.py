import win32gui,win32api,win32con
from win32api import GetSystemMetrics
from PIL import ImageGrab
import time

a,b = GetSystemMetrics(0),GetSystemMetrics(1)

def ClickL(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def KeyDown(code):
    win32api.keybd_event(code,0,0,0)



def Shoot(x,y):
    # the maginfying class ratio
    ratio = 4
    beforeP = win32gui.GetCursorPos()

    # the vec between cursor and enemy position
    difVec = (x-beforeP[0],y-beforeP[1])

    shootP = (int(beforeP[0]+difVec[0]/ratio),int(beforeP[1]+difVec[1]/ratio+4))
    win32api.SetCursorPos(shootP)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,shootP[0],shootP[1],0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,shootP[0],shootP[1],0,0)

    # close the maginfying class
    KeyDown(32)


def GetAnePosition(px,im,cursor):
    yGap = 3
    xGap = 3

    width = 320
    height = 320


    #for speeding up the caculating  limit the domain in magnifying class 
    yBottom = int(cursor[1]-height/2)
    yTop = int(cursor[1]+height/2)
    if(yBottom<0):
        yBottom = 0
    if(yTop>im.size[1]):
        yTop = im.size[1]

    xBottom = int(cursor[0]-width/2)
    xTop = int(cursor[0]+width/2)   
    if(xBottom<0):
        xBottom = 0

    if(xTop>im.size[0]):
        xTop = im.size[0]

    for i in range(yBottom,yTop,yGap):
        for j in range(xBottom,xTop,xGap):
            pixelN = px[j,i]
            if(checkAne(pixelN)):
                return (j,i)    

    return False
        
# check if there is an enemy at corresponding pixel
def checkAne(pixel):
    center = (174,145,113)
    # mL = (166,130,96)
    # mR = (212,167,125)
    # lL = (222,184,144)
    # lR = (190,158,123)
    checkPs = []
    checkPs.append(center)
    # checkPs.append(mL)
    # checkPs.append(mR)
    # checkPs.append(lL)
    # checkPs.append(lR)
    # checkPs.append((132,107,67))
    # checkPs.append((185,148,112))
    # checkPs.append((158,131,103))
    tol = 30
    output =False
    for p in checkPs:
        if(abs(p[0]-pixel[0])<=tol and abs(p[1]-pixel[1])<=tol and abs(p[2]-pixel[2])<=tol):
            output = True
            break
    return output

    
    


if __name__ == "__main__":
    input("start?")

    # record game screen anchors
    leftTop = (314,180)
    rightBottom = (1300,1000)

    # wake up 4399 window
    ClickL(leftTop[0]+10,leftTop[1])

    while True:
        #capture the game screen
        im = ImageGrab.grab((leftTop[0],leftTop[1],rightBottom[0],rightBottom[1]))
        px = im.load()

        # check if the magifying glass is open
        checkMagP = px[4,4] 
        if(checkMagP[0]<10 and checkMagP[1]<10 and checkMagP[2]<10):
            #if true get current cursor in game
            cursor= win32gui.GetCursorPos()
            cursor = (cursor[0]-leftTop[0],cursor[1]-leftTop[1])

            #get anemy position
            aniPosition = GetAnePosition(px,im,cursor)
            if(aniPosition!=False):
                # if any,shoot
                Shoot(aniPosition[0]+leftTop[0],aniPosition[1]+leftTop[1])
                time.sleep(0.5)



        






    