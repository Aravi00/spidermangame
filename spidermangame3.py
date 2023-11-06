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
    global rext, reyt
    length = np.sqrt((mousex-(boxx+30))**2 + (boxy-mousey)**2)
    if mousex>(boxx+30):
        x = mousex-(boxx+30)
    elif mousex<(boxx+30):
        x = (boxx+30)-mousex
    if mousey>boxy:
        y = boxy-mousey
    elif mousey<boxy:
        y = mousey-boxy
    if (mousex<(boxx+30) and mousey<boxy) or (mousex>(boxx+30) and mousey>boxy):
        angle = np.degrees(np.arctan(x/y))
        print("topl")
    if (mousex<(boxx+30) and mousey>boxy) or (mousex>(boxx+30) and mousey<boxy):
        angle = np.degrees(np.arctan(y/x))
        print("topr")
    return angle, length
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    if ev.type == py.MOUSEBUTTONDOWN:
        pressed = not pressed
        x,y = py.mouse.get_pos()
        print(x,y)
        angle,length = getdata(rext,reyt,x,y)
    window.fill("white")
    yspeed+=0.05
    reyt+=yspeed
    if reyt >= 400:
        yspeed = 0
        reyt = 400

    if rext > windowwidth:
        rext = 0
    elif rext < 0:
        rext = windowwidth
        #draw here
    if pressed:
        print(angle,length)
        rext = x - length*(np.cos(angle))
        reyt = y + length*np.sin(angle)
        angle+=0.01
        py.draw.line(window,(0,0,0),(rext+30,reyt),(x,y))
        
    rect = [rext,reyt,30,40] #x,y,w,h
    py.draw.rect(window,(0,0,0),rect)
    py.display.flip()
    clock.tick(60)     
    
py.quit()

