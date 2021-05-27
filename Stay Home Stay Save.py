import turtle
var=turtle.Turtle()
s=turtle.getscreen()
turtle.screensize(1800,3200)
s.bgcolor("black")
var.hideturtle()
var.pencolor("red")
var.penup()
var.setposition(140,-270)
var.pendown()
var.write("Stay Home, Stay Safe!",'false','right', font=('Showcard Gothic',20))
var.penup()
var.setposition(100, -325)
var.pendown()
var.pencolor('orange')
var.write("Wear Face Mask.\n Wash hands often.\n Use Sanitizer.\n Cook food thoroughly.")
var1=0
var2=0

var.penup()
var.setposition(620,-325)
var.pencolor("pink")
var.pendown()
var.write("By Priyanka Ghosh",'false','right', font=('Showcard Gothic',10))


var.speed(0)

var.pencolor("dark green")
var.pensize(1)
var.penup()
var.goto(0,230)
var.pendown()
while True:
    var.fd(var1)
    var.rt(var2)
    var1+=3
    var2+=1
    if var2==207:
        break
    var.hideturtle()


turtle.done()
