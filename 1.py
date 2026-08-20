import turtle
turtle.setup(width=800,height=600)
turtle.penup()
turtle.fd(-100)
turtle.pendown()
turtle.pensize(10)
turtle.pencolor("red")
turtle.seth(135)
turtle.circle(-100,50)
turtle.right(90)
turtle.circle(-100,50)#左耳朵
turtle.seth(30)
turtle.circle(-100,55)#head
turtle.seth(60)
turtle.circle(-100,50)
turtle.seth(-75)
turtle.circle(-100,50)#右耳
turtle.seth(-60)
turtle.circle(-90,40)
turtle.seth(-30)
turtle.circle(-50,100)#right face
turtle.seth(135)
turtle.circle(30,360)#right hand
turtle.penup()
turtle.circle(30,-90)
turtle.pendown()
turtle.seth(-70)
turtle.circle(-40,30)
turtle.seth(15)
turtle.circle(-45,360)#right leg
turtle.penup()
turtle.circle(-45,-90)
turtle.pendown()
turtle.seth(-135)
turtle.circle(-110,85)#pg
turtle.seth(85)
turtle.circle(45,360)#left leg
turtle.penup()
turtle.circle(45,90)
turtle.pendown()
turtle.seth(100)
turtle.circle(-40,30)
turtle.seth(135)
turtle.circle(-30,360)#left hand
turtle.penup()
turtle.circle(-30,90)
turtle.pendown()
turtle.seth(135)
turtle.circle(-50,100)
turtle.seth(110)
turtle.circle(-90,42)#left face
turtle.penup()
turtle.circle(-40,-90)
turtle.seth(0)
turtle.fd(20)
turtle.pendown()
turtle.seth(90)
turtle.color("black")
turtle.circle(-8,360)
turtle.done()

