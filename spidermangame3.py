import pygame as py
import numpy as np
#setup
py.init()
windowwidth = 500
windowheight = 500
window = py.display.set_mode((windowwidth,windowheight))
clock = py.time.Clock()
#loop
rext = 50
reyt = 50
yspeed = 2
pressed = False
def getdata (boxx,boxy,mousex,mousey):
    boxx = boxx+30
    length = np.sqrt((mousex-(boxx))**2 + (boxy-mousey)**2)
    #use sin or cosine instead and then use length as hypotonues using picture as reference
    if (mousex<(boxx) and mousey<boxy): # 4
        angle = np.degrees(np.arcsin((boxx-mousex)/length))
        print("4",angle)
    elif (mousex>(boxx) and mousey>boxy): # 1
        angle = np.degrees(np.arcsin((mousex-boxx)/length))
        print("1",angle)
    elif (mousex<(boxx) and mousey>boxy): # 3

        angle = np.degrees(np.arcsin((mousey-boxy)/length))
        print("3",angle)
    elif (mousex>(boxx) and mousey<boxy): # 2
        angle = np.degrees(np.arcsin((boxy-mousey)/length))
        print("2",angle)
    
    return angle, length
window.fill("white")
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    if ev.type == py.MOUSEBUTTONDOWN:
        pressed = not pressed
        
        x,y = py.mouse.get_pos()
        if pressed:
            print(x,y)
            angle,length = getdata(rext,reyt,x,y)
        else:
            yspeed = -0.6*yspeed
    window.fill("white")

    yspeed+=0.05
    reyt+=yspeed
    if reyt >= 400:
        yspeed = -0.8*yspeed # die here
        reyt = 400
    if pressed:
        print(angle)
        if angle > 160:
            pressed = False
            yspeed = -0.6*yspeed
        else:
            rext = (x - length*(np.cos(np.radians(angle))))
            reyt = (y + length*np.sin(np.radians(angle)))
            angle+=1
            py.draw.line(window,(0,0,0),(rext+30,reyt),(x,y))
    rect = [rext,reyt,30,40] #x,y,w,h
    py.draw.rect(window,(0,0,0),rect)
    py.display.flip()
    clock.tick(60)     
    
py.quit()

