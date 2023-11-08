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
        print("4")
        angle = np.degrees(np.arcsin((boxx-mousex)/length))
    elif (mousex>(boxx) and mousey>boxy): # 1
         print("1")
         angle = np.degrees(np.arcsin((mousex-boxx)/length))
    elif (mousex<(boxx) and mousey>boxy): # 3
        print("3")
        angle = np.degrees(np.arcsin((mousey-boxy)/length))
    elif (mousex>(boxx) and mousey<boxy): # 2
        print("2")
        angle = np.degrees(np.arcsin((boxy-mousey)/length))
    
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
    #window.fill("white")
    yspeed+=0.05
    reyt+=yspeed
    if reyt >= 400:
        yspeed = 0
        reyt = 400
        
    if pressed:
        #print(angle)
        rext = (x - length*(np.cos(angle)))
        reyt = (y + length*np.sin(angle))
        angle+=0.01
        py.draw.line(window,(0,0,0),(rext+30,reyt),(x,y))
        
        
    rect = [rext,reyt,30,40] #x,y,w,h
    py.draw.rect(window,(0,0,0),rect)
    py.display.flip()
    clock.tick(60)     
    
py.quit()

