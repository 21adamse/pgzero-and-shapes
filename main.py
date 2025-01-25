import pgzrun
import random

WIDTH=300
HEIGHT=300

def draw():
    screen.fill("black")
    w=WIDTH
    h=HEIGHT-200
    r=0
    g=random.randint(120,255)
    b=255
    for x in range(20):
        #creating a rectangle requires 2 steps
        #step1- setting the properties of the rectangle
        rectangle=Rect((100,100),(w,h))
        rectangle.center=(150,150)
        #step2- drawing on the screen
        screen.draw.rect(rectangle,(r,g,b))
        w=w-10
        h=h+10
        r=r+10
        b=b-10
pgzrun.go()

