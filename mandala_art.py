import turtle
import colorsys

t= turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor('black')
t.speed(10.5)
n,h=36,0
for i in range(360):
    c = colorsys.hsv_to_rgb(h,1,1)
    h +=1/n
    t.color(c)
    t.circle(180)
    t.left(10)
