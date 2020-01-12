import turtle
import winsound

wn=turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score1=0
score2=0

#board1
board1=turtle.Turtle()
board1.speed(0)
board1.shape("square")
board1.color("White")
board1.penup()
board1.goto(-350,0)
board1.shapesize(stretch_wid=5, stretch_len=1)

#board2
board2=turtle.Turtle()
board2.speed(0)
board2.shape("square")
board2.color("White")
board2.penup()
board2.goto(350,0)
board2.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("White")
ball.penup()
ball.goto(0,0)
ball.dx=0.19
ball.dy=0.19

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player1 :0   Player2 :0", align="center", font=("Courier",24,"normal"))

#functions...
def board1_up():
    y=board1.ycor()
    y+=20
    board1.sety(y)

def board1_down():
    y=board1.ycor()
    y-=20
    board1.sety(y)

def board2_up():
    y=board2.ycor()
    y+=20
    board2.sety(y)

def board2_down():
    y=board2.ycor()
    y-=20
    board2.sety(y)
    
#keyboard binding
wn.listen()
wn.onkeypress(board1_up,"w")
wn.onkeypress(board1_down,"s")
wn.onkeypress(board2_up,"Up")
wn.onkeypress(board2_down,"Down")

#main loop

while True:
    wn.update()

    #moving the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 +=1
        pen.clear()
        pen.write(f"Player1 :{score1}  Player2 :{score2}", align="center", font=("Courier",24,"normal"))

    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 +=1
        pen.clear()
        pen.write(f"Player1 :{score1}  Player2 :{score2}", align="center", font=("Courier",24,"normal"))

    #paddle & ball collision
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<board2.ycor() + 40 and ball.ycor()> board2.ycor()- 40):
        ball.setx(340)
        ball.dx*= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<board1.ycor() + 40 and ball.ycor()> board1.ycor()- 40):
        ball.setx(-340)
        ball.dx*= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
