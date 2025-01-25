import pgzrun
import random

WIDTH=300
HEIGHT=300

def draw():
    screen.fill("black")
    w=WIDTH-200
    h=HEIGHT-200
    r=0
    g=random.randint(120,255)
    b=255
    x1=0
    y1=0
    for x in range(20):
        #creating a rectangle requires 2 steps
        #step1- setting the properties of the rectangle
        rectangle=Rect((100,100),(w,h))
        rectangle.center=(x1,y1)
        #step2- drawing on the screen
        screen.draw.filled_rect(rectangle,(r,g,b))
        w=w-10
        h=h+10
        r=r+10
        b=b-10
        x1=x1+5
        y1=y1+5
pgzrun.go()