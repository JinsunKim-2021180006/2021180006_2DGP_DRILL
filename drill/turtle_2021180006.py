import turtle


turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()


count = 0
while (count < 4):
    turtle.forward(500)
    turtle.left(90)
    count+=1

count = 0

while(count<2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.left(90)
    count+=1

count = 0
turtle.forward(100)

while(count <2):
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    count+=1

