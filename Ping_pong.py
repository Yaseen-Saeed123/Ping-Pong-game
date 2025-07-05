# import turtle module
import turtle
import time

# Create game screen
window = turtle.Screen() # Create screen
window.title("Ping Pong Game")
window.bgcolor("black")  # Change bgcolor
window.setup(width = 800, height=600) # Set width and height
window.tracer(0)  # Prevent automatic update of window

# Game objects
## Bat 1
bat1 = turtle.Turtle()  # Create turtle object
bat1.speed(0)  # Speed of drawing
bat1.shape("square")  # Determine shape
bat1.penup() # Prevent making lines
bat1.color("blue") # Determining colors
bat1.shapesize(stretch_len=1, stretch_wid=5) # Change size to 100px x 20px
bat1.goto(-350, 0) # Determine location

## bat 2
bat2 = turtle.Turtle()
bat2.speed(0)
bat2.shape("square")
bat2.penup()
bat2.color("red")
bat2.shapesize(stretch_len=1, stretch_wid=5)
bat2.goto(350, 0)

## ball
ball = turtle.Turtle()
ball.shape("square")
ball.penup()
ball.color("white")
ball.goto(0, 0)
time.sleep(2)
ball.dx = 0.3
ball.dy = 0.3

## Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.speed(0)
score.write(f"Player 1 {score1} : {score2} Player 2", font=("Arial", 24, "normal"), align="center")

# Moving Bats
## Bat 1
def bat1_up():
    y = bat1.ycor()
    if y < 250:
        y += 20
        bat1.sety(y)

def bat1_down():
    y = bat1.ycor()
    if y > -250:
        y -= 20
        bat1.sety(y)
## Bat 2
def bat2_up():
    y = bat2.ycor()
    if y < 250:
        y += 20
        bat2.sety(y)

def bat2_down():
    y = bat2.ycor()
    if y > -250:
        y -= 20
        bat2.sety(y)

## Keyboard bindings
window.listen()
window.onkeypress(bat1_up, "Up")
window.onkeypress(bat1_down, "Down")
window.onkeypress(bat2_up, "w")
window.onkeypress(bat2_down, "s")

# Main game Loop
while True:
    window.update() # Update the game every time the loop runs
    # ball movement
    ## x-axis
    ball.setx(ball.xcor() + ball.dx)
    ## y-axis
    ball.sety(ball.ycor() + ball.dy)

    # Check borders
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1 {score1} : {score2} Player 2", font=("Arial", 24, "normal"), align="center")

    elif ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1 {score1} : {score2} Player 2", font=("Arial", 24, "normal"), align="center")

    elif ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball touching bats
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bat2.ycor() + 40 and ball.ycor() > bat2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bat1.ycor() + 40 and ball.ycor() > bat1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    # Score check
    if score1 == 10 or score2 == 10:
        score.clear()
        score1 = 0
        score2 = 0
        score.write(f"Player 1 {score1} : {score2} Player 2", font=("Arial", 24, "normal"), align="center")