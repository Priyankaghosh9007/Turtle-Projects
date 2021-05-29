import turtle
s=turtle.getscreen()
t=turtle.Turtle()
turtle.ht()
turtle.bgcolor("black")
t.ht()
t.up()
t.goto(0,50)
t.down()
for i in range(104):
    t.pensize(2)
    t.speed(50)
    color=['indigo','purple','darkviolet','magenta','hotpink','tomato','white','red','maroon']

    if i%9==0:
         t.pencolor(color[0])
    if i%9==1:
         t.pencolor(color[1])
    if i%9==2:
         t.pencolor(color[2])
    if i%9==3:
         t.pencolor(color[3])

    if i%9==4:
         t.pencolor(color[4])
    if i%9==5:
         t.pencolor(color[5])
    if i%9==6:
         t.pencolor(color[6])
    if i%9==7:
         t.pencolor(color[7])
    if i%9==8:
         t.pencolor(color[8])
         
    
    
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(150)
    
    
    t.lt(5)




    
