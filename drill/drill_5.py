import turtle

turtle.shape("turtle")
turtle.color("green")

def wKey():
    turtle.seth(90)
    go()
def aKey():
    turtle.seth(180)
    go()
def sKey():
    turtle.seth(270)
    go()
def dKey():
    turtle.seth(0)
    go()

def go():
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.onkey(wKey,'w')
turtle.onkey(aKey,'a')
turtle.onkey(sKey,'s')
turtle.onkey(dKey,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
