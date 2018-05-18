#Space Invaders - McNaldo the Mystic

import turtle
import os

#Set up screen
mainscreen = turtle.Screen()
mainscreen.bgcolor("black")
mainscreen.title("Space Invaders")

#Draw a border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()


#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Enemy Invader
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemyspeed = 2

#Create enemy projectile
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#"Move Left" function
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)

#"Move Right" function
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	global bulletstate

	#Move the bullet to just above the player
	x = player.xcor()
	y = player.ycor() +10
	bullet.setposition(x, y)
	bullet.showturtle()


#Keyboard Bindings
turtle.listen()
turtle.onkey(move_right, "Right")
turtle.onkey(move_left, "Left")
turtle.onkey(fire_bullet, "space")
#Main Game Loop
while True:
	
	#Move the enemy
	x = enemy.xcor()
	x += enemyspeed
	enemy.setx(x)

	#Move the enemy back and down
	if enemy.xcor() > 280:
		y = enemy.ycor()
		y -= 40
		enemyspeed *= -1
		enemy.sety(y)

	if enemy.xcor() < -280:
		y = enemy.ycor()
		y -= 40
		enemyspeed *= -1
		enemy.sety(y)

	#Move bullet
	y = bullet.ycor()
	y += bulletspeed
	bullet.sety(y)



delay = input("Press enter to finish.")