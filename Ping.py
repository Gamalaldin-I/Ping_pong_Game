import turtle

score1=0
score2=0
goal=10
winner=""
x=0

#screen
wind=turtle.Screen()
wind.title("ping pong game by gamal hataba")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(1)
#madrab 1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.penup()
madrab1.shapesize(stretch_wid=5,stretch_len=1)
madrab1.goto(-350,0)
#madrab 2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("green")
madrab2.penup()
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.goto(350,0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx=2.5
ball.dy=2.5

#score 
score=turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.goto(0,250)
score.hideturtle()
score.write("Gamal : 0 || Kareem : 0 ",align="center",font=("Ariel",24,"normal"))
#moves of madrab1
def madrab1Up():
    y=madrab1.ycor()
    y= y+ 20
    madrab1.sety(y)
def madrab1down():
    y=madrab1.ycor()
    y= y- 20
    madrab1.sety(y)
#moves of madrab2
def madrab2Up():
    y=madrab2.ycor()
    y= y+ 20
    madrab2.sety(y)
def madrab2down():
    y=madrab2.ycor()
    y= y- 20
    madrab2.sety(y)
#key bord control
wind.listen()
wind.onkeypress(madrab1Up,"w")
wind.onkeypress(madrab1down,"s")
wind.onkeypress(madrab2Up,"Up")
wind.onkeypress(madrab2down,"Down")








while x==0 :
    wind.update()
    ball.setx (ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

#border check
    if ball.ycor()==290:
        ball.dy*=-1
    if ball.ycor()==-290:
        ball.dy*=-1

#return
    if (ball.xcor()==-400) :
        ball.goto(0,0)
        ball.dx*=-1
        score2+=1
        score.clear()
        score.write("Gamal : {} || Kareem : {} ".format(score1,score2),align="center",font=("Ariel",24,"normal"))
    if (ball.xcor()==400) :
        ball.goto(0,0)
        ball.dx*=-1
        score1+=1
        score.clear()
        score.write("Gamal : {} || Kareem : {} ".format(score1,score2),align="center",font=("Ariel",24,"normal"))

    if (ball.xcor() >340 and ball.xcor()< 350) and (ball.ycor() < madrab2.ycor()+40 and ball.ycor()>madrab2.ycor()-40) :
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor() <-340 and ball.xcor()> -350) and (ball.ycor() < madrab1.ycor()+40 and ball.ycor()>madrab1.ycor()-40) :
        ball.setx(-340)
        ball.dx*=-1
    
    #if(score1==goal):
        #score.clear()
        #  score.color("red")
        # score.goto(0,0)
        #score.write("Gamal won",align="center",font=("Ariel",70,"normal"))
        #winner="Gamal"
        #x=-1
        #if(score2==goal):
        #  score.clear()
        # score.color("blue")
        #score.goto(0,0)
        #score.write("Kareem won",align="center",font=("Ariel",70,"normal"))
        #winner="Kareem"
    
 
#score

    