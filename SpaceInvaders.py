#Space Invaders - McNaldo the Mystic

import turtle
import os
import math
import random
import winsound

#Set up screen
mainscreen = turtle.Screen()
mainscreen.bgcolor("white")
mainscreen.title("Space Invaders")
mainscreen.bgpic("Background.gif")

#Register the shapes
turtle.register_shape("Invader.gif")
turtle.register_shape("Player.gif")

#Draw a border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("purple")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#Set score to 0
score = 0

#Draw Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("Player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15


#Choose # of enemies
num_of_enemies = 5
#Create empty list
enemies = []
#Add enemies to list
for i in range(num_of_enemies):
	#Create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:
	#Enemy Invader Properties
	enemy.color("red")
	enemy.shape("Invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)

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

bulletstate = "ready"

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
	if bulletstate == "ready":
		winsound.PlaySound('laser.wav', winsound.SND_FILENAME)
		bulletstate = "fire"
	#Move the bullet to just above the player
		x = player.xcor()
		y = player.ycor() +10
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False


#Keyboard Bindings
turtle.listen()
turtle.onkey(move_right, "Right")
turtle.onkey(move_left, "Left")
turtle.onkey(fire_bullet, "space")


#Main Game Loop
while True:
	
	for enemy in enemies:

		#Move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#Move the enemy back and down
		if enemy.xcor() > 280:
			#Moves all of the enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1

		if enemy.xcor() < -280:
			for e in enemies:
				#Move all enemies down
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1

		#Check for collision between bullet and enemy
		if isCollision(bullet, enemy):
			winsound.PlaySound('explosion.wav', winsound.SND_FILENAME)
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#Reset the enemy
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			#Update the score
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

		#Check for collision between player and enemy
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print("Game Over")
			break

	#Move bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#Check if bullet hits border
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"

delay = input("Press enter to finish.")