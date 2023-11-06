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
reyt =50
yspeed = 2
pressed = False
while True:
    ev = py.event.poll()
    if ev.type == py.QUIT:
        break
    key = py.key.get_pressed()
    if ev.type == py.MOUSEBUTTONDOWN:
        pressed = True
        x,y = py.mouse.get_pos()
        print(x,y)
        
    window.fill("white")    
    yspeed+=1
    reyt+=yspeed
    if reyt >= 400:
        yspeed = 0
        reyt = 400

    if rext > windowwidth:
        rext = 0
    elif rext < 0:
        rext = windowwidth
    
    rect = [rext,reyt,30,40] #x,y,w,h
    #draw here
    if pressed:
        angle = int(np.degrees(np.arctan((reyt-y)/(x-(rext+30)))))
        length = np.sqrt((x-(rext+30))**2 + (reyt-y)**2)
        print(angle,length)
        
        
        
        
        
        py.draw.line(window,(0,0,0),(rext+30,reyt),(x,y))
    py.draw.rect(window,(0,0,0),rect)
    py.display.flip() 
    clock.tick(60)                                   
py.quit()

