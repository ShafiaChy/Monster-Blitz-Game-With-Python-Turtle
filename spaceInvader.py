import turtle
import math
import os
import random
import platform
import time

# If on Windows, you import winsound ,else Linux
from typing import Any, Union

if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("Winsound module is not available.")

# set up the screen
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Sea Invaders")
wn.bgpic("sea_bg.gif")
wn.tracer(0)

# Show the name of the game on screenG
w_pen = turtle.Turtle()
w_pen.speed(0)
w_pen.color("black")
w_pen.penup()
wstring = "Monster Blitz"
w_pen.write(wstring, False, "center", ("Comic Sans MS",25, "bold"))
w_pen.hideturtle()
time.sleep(5)
w_pen.clear()

#start the game
a_pen = turtle.Turtle()
a_pen.speed(0)
a_pen.color("white")
a_pen.penup()
astring = "Start"
a_pen.write(astring, False, "center", ("Arial", 20, "italic"))
a_pen.hideturtle()
time.sleep(2)
a_pen.clear()

# Register the shape
turtle.register_shape("e.gif")
turtle.register_shape("playplay.gif")
turtle.register_shape("searoc.gif")
turtle.register_shape("stafi.gif")

# Draw border
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

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 276)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, "left", ("Arial", 14, "normal"))
score_pen.hideturtle()

# End the game
def game_over():
    g_pen = turtle.Turtle()
    g_pen.speed(0)
    g_pen.color("white")
    g_pen.penup()

    gstring = "Game Over"
    g_pen.write(gstring, False, "center", ("Arial", 20, "italic"))
    g_pen.hideturtle()


# Choose a number of enemies
number_of_enemies = 11
# Create an empty list
enemies = []
k = 0
j = 0
for i in range(number_of_enemies):
    # create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:

    enemy.color("dark red")
    enemy.shape("e.gif")
    enemy.penup()
    enemy.speed(0)

    x = random.randint(-250+k, -220+j)
    y = random.randint(150, 270)
    enemy.setposition(x, y)

    k = k + 50
    j = j + 50

enemyspeed = 0.2

# Create player
player = turtle.Turtle()
player.color("dark green")
player.shape("playplay.gif")
player.penup()
player.speed(0)
player.setposition(0, -170)
player.setheading(90)

playerspeed = 0
# Choose a number of rocks
number_of_rocks = 2
# Create an empty list
rocks = []
x = -525
y = -235

for i in range(number_of_rocks):
    # create the rock
    rocks.insert(i, turtle.Turtle())
# Create obstacles
for rock in rocks:
    rock.color("grey")
    rock.shape("searoc.gif")
    rock.penup()
    rock.speed(0)
    rock.shapesize(6, 6)
    rock.setheading(90)
    rock.setposition(x, y)
    x += 300
    rock.setposition(x, y)

# Choose a number of starfishes
number_of_starfishes = 2
# Create an empty list
stars = []
x = -320
y = -240

for i in range(number_of_starfishes):
    # create the rock
    stars.insert(i, turtle.Turtle())
# Create starfishes
for star in stars:
    star.color("grey")
    star.shape("stafi.gif")
    star.penup()
    star.speed(0)
    star.shapesize(3, 3)
    star.setheading(90)
    star.setposition(x, y)
    x+= 60
    star.setposition(x, y)



playerspeed = 25

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -255:
        x = -255

    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 255:
        x = 255

    player.setx(x)

def move_up():
    y = player.ycor()
    y += playerspeed
    if y > -140:
        y = -140

    player.sety(y)

def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -220:
        y = -220

    player.sety(y)



def fire_bullet():
    # Declare bulletstate as a global if it needs changes
    global bulletstate
    if bulletstate == "ready":
        play_sound("laser.wav")
        bulletstate = "fire"
    # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision1(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False


def isCollision2(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 80:
        return True
    else:
        return False

def isCollision3(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 80:
        return True
    else:
        return False

def play_sound(sound_file, time=0):
    # Windows
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    # Linux
    elif platform.system() == "Linux":
        os.system("aplay -q {}&".format(sound_file))

    #Mac
    else:
        os.system("aplay {}&".format(sound_file))

    # Repeat Sound
    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t = int(time * 1000))



# Create player's bullet
bullet = turtle.Turtle()
bullet.color("black")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setposition(0, -250)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 5

# Define bullet speed
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

# Create keyboard bindings
turtle.listen()

turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")


# Play background music
play_sound("bg.wav", 119)
# Main Game Loop
c = 0
while True:
    wn.update()

    for enemy in enemies:
        #  Move the enemy

        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #  Move the enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)

            enemyspeed *= -1

        #  Check for a collision between the bullet and the enemy
        if isCollision1(bullet, enemy):
            play_sound("explosion.wav")
            #  Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)

            #  Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(0, 10000)

            # Update the score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, "left", ("Arial", 14, "normal"))
            c = c + 1


        for rock in rocks:

            if isCollision3(enemy, rock):
                play_sound("explosion.wav")

                x = random.randint(-250, 250)
                y = random.randint(150, 250)
                enemy.setposition(x, y)



        if enemy.ycor() < -248:
            x = random.randint(-250, 250)
            y = random.randint(150, 250)
            enemy.setposition(x, y)

        if isCollision1(player, enemy):
            play_sound("explosion.wav")
            player.hideturtle()
            enemy.hideturtle()
            bulletstate = "not ready"
            game_over()
            break


    for rock in rocks:

        if isCollision2(player, rock):
            play_sound("explosion.wav")
            player.hideturtle()
            bulletstate = "not ready"
            game_over()
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Make sure the bullet reaches the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    # Declare the winner
    if c == number_of_enemies:
        d_pen = turtle.Turtle()
        d_pen.speed(0)
        d_pen.color("white")
        d_pen.penup()

        dstring = "Player Wins"
        d_pen.write(dstring, False, "center", ("Arial", 20, "italic"))
        d_pen.hideturtle()



