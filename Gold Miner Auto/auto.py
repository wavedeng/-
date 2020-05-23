import win32gui,win32api,win32con
from win32api import GetSystemMetrics
from PIL import ImageGrab
import time
import math
from pynput.mouse import Listener
import threading





def ClickL(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def KeyDown(code):
    win32api.keybd_event(code,0,0,0)


# def checkSameDirection(vec1,vec2):

#     length1 = getLengthOfV(vec1)
#     length2 = getLengthOfV(vec2)

#     # print(str(vec1[0]))

#     vec1 = (vec1[0]/length1,vec1[1]/length1)
#     vec2 = (vec2[0]/length2,vec2[1]/length2)

#     vecDis = (vec1[0]-vec2[0],vec1[1]-vec2[1])

#     dis = getLengthOfV(vecDis)


#     if(dis<0.09):
#         return True
#     else:
#         return False

    


def getLengthOfV(vec):
    return math.sqrt(math.pow(vec[0],2)+math.pow(vec[1],2))



targetP = None


centerP = (961,189)
catching = False
R = 14
# density = 20
# pie = math.pi/density

def on_click(x, y, button, pressed):
    global targetP
    # print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

    print(str(x)+","+str(y))
    if(x<10 and y <10):
        return False



    tick = 0



    if pressed:
        targetP = (x,y)

        while True:

            tick += 1
            if(tick >200):
                break
            #capture the game screen
            im = ImageGrab.grab((centerP[0]-(R),centerP[1],centerP[0]+(R),centerP[1]+(R)))
            px = im.load()
    
            # for i in range(density):
            #     # print(str(math.cos(pie*i)))
            #     # print(str(math.sin(pie*i)))
            #     checkOffsetX =  math.cos(pie * i) * (R-2)
            #     checkOffsetY = math.sin(pie * i) * (R-2)
            #     checkP = (int(R+checkOffsetX),int(checkOffsetY))
            #     endP = px[checkP[0],checkP[1]]
            #     if(endP[0] == 51 and endP[1] == 51 and endP[2] == 51):
            #         currentEndP = [checkOffsetX,checkOffsetY]
            #         break


            

            checkP = (targetP[0]-centerP[0],targetP[1]-centerP[1])

            tempLen = getLengthOfV(checkP)

            checkP = (int(checkP[0]*(R-1)/tempLen),int(checkP[1]*(R-1)/tempLen))

            checkPixel = px[checkP[0]+R,checkP[1]]

            if(checkPixel[0] == 51 and checkPixel[1] == 51 and checkPixel[2] == 51):
                KeyDown(40)
                targetP = None
                break

            # if(currentEndP!=None and targetP != None):
            #     if(checkSameDirection(currentEndP,(targetP[0]-centerP[0],targetP[1]-centerP[1]))):
            #         print("")
            #         KeyDown(40)
            #         targetP = None
            #         break

                

    return True
            









if __name__ == "__main__":
    with Listener( on_click=on_click) as listener:
        listener.join()






        
