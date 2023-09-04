import turtle
from turtle import *
import random
import time
import threading
from playsound import playsound
import winsound

wn = turtle.Screen()
wn.bgcolor('#7cb834')
wn.setup(1400, 750)
wn.title("Yedidya Hazan")
turtle.speed('fastest')
t = turtle.Turtle()
tracer(0)

#סאונד

# def play_sound(file_path):
#     # play sound file
#     playsound(file_path)
#
# # start a new thread for playing the sound
# t = threading.Thread(target=play_sound, args=('traffic.wav',))
# t.start()
#
# # continue running the code while the sound is playing
# for i in range(5):
#     print(i)


# כביש ימין תחתון
t.penup()
t.speed(0)
t.goto(1530/2, -70)
t.setheading(180)
t.pendown()
t.pensize(50)
t.pencolor("#727272")
t.forward(440)
t.left(90)
t.forward(440)


#כביש ימין עליון
t.penup()
t.goto(1555/2, 150)
t.setheading(180)
t.pendown()
t.pencolor('#727272') # צבע הקו
t.pensize(70) # עובי הקו
t.forward(440)
t.right(90)
t.forward(440)


#כביש שמאל תחתון
t.penup()
t.goto(-1510/2, -70)
t.setheading(0)
t.pendown()
t.pencolor('#727272') # צבע הקו
t.pensize(60) # עובי הקו
t.forward(440)
t.right(90)
t.forward(440)

#כביש שמאל עליון
t.penup()
t.goto(-1510/2, 150)
t.setheading(0)
t.pendown()
t.pencolor('#727272') # צבע הקו
t.pensize(60) # עובי הקו
t.forward(440)
t.left(90)
t.forward(440)


#אי עגול עליון
t = turtle.Turtle()
t.speed(0)
t.pensize(1)
t.penup()
t.goto(-75, 400)
t.setheading(-90)
t.pendown()
t.fillcolor("gray")
t.begin_fill()
t.forward(200)
t.circle(70, 180)
t.forward(200)
t.end_fill()
t.hideturtle()

# אי עגול תחתון
t = turtle.Turtle()
t.speed(0)
t.pensize(1)
t.penup()
t.goto(-75, -400)
t.setheading(90)
t.pendown()
t.fillcolor("gray")
t.begin_fill()
t.forward(250)
t.circle(-70, 180)
t.forward(250)
t.end_fill()
t.hideturtle()

#צבע כביש אמצע
def draw_rectangle(length):
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(170)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

turtle.speed(0)
turtle.penup()
turtle.color('#2f2f2f')
turtle.goto(-770, -50)
draw_rectangle(1550)
t.hideturtle()

#עיגול מכסה עליון
t.speed(0)
t.pensize(60)
t.penup()
t.color('#2f2f2f')
t.goto(-110, 210)
t.pendown()
t.circle(100, 180)

#עיגול מכסה תחתון
t.speed(0)
t.pensize(70)
t.penup()
t.color('#2f2f2f')
t.goto(95, -145)
t.setheading(90)
t.pendown()
t.circle(100, 180)
t.hideturtle()

#צבע כביש רוחב
def draw_rectangle(length, width):
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


turtle.speed(0)
turtle.penup()
turtle.color('#2f2f2f')
turtle.goto(62, -420)
draw_rectangle(1300, 255)


turtle.speed(0)
turtle.penup()
turtle.color('#2f2f2f')
turtle.goto(-310, -420)
draw_rectangle(1300, 240)



#אי עגול עליון
t.speed(0)
t.pensize(1)
t.penup()
t.goto(-75, 400)
t.setheading(-90)
t.pendown()
t.fillcolor("gray")
t.begin_fill()
t.forward(200)
t.circle(70, 180)
t.forward(200)
t.end_fill()
t.hideturtle()

#מעבר חציה
def draw_sidewalk(x, y, gap, num_blocks):
    t.speed(0)
    t.pensize(0)

    block_color = "white"
    block_width = 90
    block_height = 30

    # calculate the total width of the sidewalk row
    row_width = num_blocks * block_width + (num_blocks - 1) * gap

    # draw the sidewalk row
    for i in range(num_blocks):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(block_color)
        t.begin_fill()
        t.forward(block_width)
        t.left(90)
        t.forward(block_height)
        t.left(90)
        t.forward(block_width)
        t.left(90)
        t.forward(block_height)
        t.left(90)
        t.end_fill()
        x += block_width + gap

    # add extra gap at the end of the row
    x += gap


draw_sidewalk(100, 170, -40, 5)#ימין עליון
draw_sidewalk(100, -180, -40, 5)#ימין תחתון
draw_sidewalk(-280, -190, -40, 5)#שמאל תחתון
draw_sidewalk(-275, 170, -40, 5)#שמאל עליון

t.hideturtle()

#פסי כביש
def draw_rectangle(length, width):
    turtle.hideturtle()
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

turtle.speed(0)
turtle.penup()
turtle.color('white')
for i in range(7):
    x = 730 - (50 * i)
    turtle.goto(x, 30)
    draw_rectangle(25, 5)

t.hideturtle()

turtle.goto(-770, 30)
for i in range(8):
    draw_rectangle(25, 5)
    turtle.forward(50)
t.hideturtle()

turtle.goto(190, -400)
for i in range(4):
    turtle.goto(190, -400 + (i * 50))
    draw_rectangle(5, 25)
t.hideturtle()

turtle.goto(190, 370)
for i in range(3):
    turtle.goto(190, 270 + (i * 50))
    draw_rectangle(5, 25)
t.hideturtle()

turtle.goto(-190, 370)
for i in range(3):
    turtle.goto(-190, 370 - (i * 50))
    draw_rectangle(5, 25)

t.hideturtle()
turtle.goto(-190, -400)
for i in range(4):
    turtle.goto(-190, -400 + (i * 50))
    draw_rectangle(5, 25)

t.end_fill()

#תמונה בית
turtle.register_shape("home.gif")
t = turtle.Turtle()
# שינוי גודל התמונה לגודל רצוי
t.shapesize(2, 2)
# הזזת התמונה למיקום אחר במסך
t.penup()
t.goto(580, 280)
t.pendown()
t.shape("home.gif")

#תמונה מגרש
turtle.register_shape("Playground.gif")
t = turtle.Turtle()
# שינוי גודל התמונה לגודל רצוי
t.shapesize(7, 9)
# הזזת התמונה למיקום אחר במסך
t.penup()
t.goto(560, -230)
t.pendown()
t.shape("Playground.gif")
#רמזור
# def create_traffic_light(rect_x, rect_y, rect_width=10, rect_height=40, circle_size=0.9):
#
#     player = turtle.Turtle()
#     player.speed(0)
#     player.ht()
#     player.hideturtle()
#
#     # הוספת צבע
#     player.fillcolor("black")
#     player.begin_fill()
#     player.penup()
#
#     # יצירת רמזור
#     player.goto(300,-100)
#     player.pendown()
#     player.forward(rect_width)
#     player.left(90)
#     player.forward(rect_height)
#     player.left(90)
#     player.forward(rect_width)
#     player.left(90)
#     player.forward(rect_height)
#     player.left(90)
#     player.end_fill()
#
#     # עמוד רמזור
#     player.pensize(5)
#     player.penup()
#     player.forward(8)
#     player.right(90)
#     player.pendown()
#     player.goto(300,-100)
#     player.pendown()
#     player.goto(310,-150)
#
#     # צבעי רמזור
#     player = turtle.Turtle()
#     player.penup()
#     player.shape("circle")
#     player.shapesize(circle_size)
#     player.color("red")
#     player.goto(300,-45)
#     player.pendown()
#
#     player = turtle.Turtle()
#     player.penup()
#     player.shape("circle")
#     player.shapesize(circle_size)
#     player.color("yellow")
#     player.goto(300,-70)
#     player.pendown()
#
#     player = turtle.Turtle()
#     player.penup()
#     player.shape("circle")
#     player.shapesize(circle_size)
#     player.color("green")
#     player.goto(300,-90)
#     player.pendown()
#
#
# # קריאה לרמזור
#     create_traffic_light(0, 0, rect_width=20, rect_height=80, circle_size=0.8)


#לכלוכים ברצפה
positions = [(-20, -79), (-60, 150), (-360, 179), (-250, -120), (250, 120)]

def change_position(turtle_object):
    x, y = random.randint(-200, 200), random.randint(-200, 200)
    turtle_object.goto(x, y)


wn = turtle.Screen()
wn.addshape('poop.gif')

# Create a list to store the turtle objects
dirties = []

for _ in range(5):
    dirty = turtle.Turtle()
    dirty.shape('poop.gif')
    dirty.penup()
    dirties.append(dirty)

# Function to reset the positions of all images
def reset_positions():
    for dirty, position in zip(dirties, positions):
        dirty.goto(position[0], position[1])


reset_positions()

# מכוניות
wn.addshape('car1.gif')
wn.addshape('car2.gif')
wn.addshape('car3.gif')
wn.addshape('car4.gif')
wn.addshape('car7.gif')
wn.addshape('car8.gif')
wn.addshape('car9.gif')

redCar = turtle.Turtle()
greenTender = turtle.Turtle()
yellowCar = turtle.Turtle()
blueCar = turtle.Turtle()
greyCarMid = turtle.Turtle()
redTender = turtle.Turtle()
perpul = turtle.Turtle()

#הזזת מכוניות
def move_cars():
    car_speed = 2
    blueCar.forward(car_speed - 1)
    greyCarMid.forward(car_speed + 2.2)
    redCar.forward(car_speed)
    redTender.forward(car_speed + 4)
    yellowCar.forward(car_speed)
    greenTender.forward(car_speed + 3)
    perpul.forward(car_speed + 3)

    #מזיז את הרככב אחורה כשהוא מגיע לקצה המסך
    if redCar.xcor() > 850:
        redCar.hideturtle()
        redCar.speed(100000)
        redCar.goto(-853, 0)
        redCar.speed(4)
        redCar.showturtle()

    if greenTender.xcor() > 850:
        greenTender.hideturtle()
        greenTender.speed(100000)
        greenTender.goto(-800, 0)
        greenTender.speed(4)
        greenTender.showturtle()

    if blueCar.xcor() < -850:
        blueCar.hideturtle()
        blueCar.speed(100000)
        blueCar.goto(730, 100)
        blueCar.speed(5)
        blueCar.showturtle()

    if greyCarMid.xcor() < -850:
        greyCarMid.hideturtle()
        greyCarMid.speed(100000)
        greyCarMid.goto(730, 100)
        greyCarMid.speed(7)
        greyCarMid.showturtle()

    if redTender.xcor() < -850:
        redTender.hideturtle()
        redTender.speed(100000)
        redTender.goto(850, 100)
        redTender.speed(7)
        redTender.showturtle()

    if yellowCar.xcor() > 850:
        yellowCar.hideturtle()
        yellowCar.speed(100000)
        yellowCar.goto(-730, -0)
        yellowCar.speed(4)
        yellowCar.showturtle()

    if perpul.xcor() > 850:
            perpul.hideturtle()
            perpul.speed(100000)
            perpul.goto(-990, -0)
            perpul.speed(4)
            perpul.showturtle()

    # Call the move_cars function recursively
    turtle.ontimer(move_cars, 10)

# Set up initial positions and properties of the cars
def setup_cars():
    redCar.speed(1)
    redCar.hideturtle()
    redCar.shape("car1.gif")
    redCar.penup()
    redCar.goto(130, 0)
    redCar.showturtle()
    redCar.direction = "left"

    greenTender.speed(1)
    greenTender.hideturtle()
    greenTender.shape("car2.gif")
    greenTender.penup()
    greenTender.goto(-800, 0)
    greenTender.showturtle()
    greenTender.direction = "right"

    yellowCar.speed(1)
    yellowCar.hideturtle()
    yellowCar.shape("car3.gif")
    yellowCar.penup()
    yellowCar.goto(0,0)
    yellowCar.showturtle()
    yellowCar.direction = "right"

    blueCar.speed(1)
    blueCar.hideturtle()
    blueCar.shape("car4.gif")
    blueCar.penup()
    blueCar.goto(250, 100)
    blueCar.showturtle()
    blueCar.right(180)

    greyCarMid.speed(1)
    greyCarMid.hideturtle()
    greyCarMid.shape("car7.gif")
    greyCarMid.penup()
    greyCarMid.goto(-200, 100)
    greyCarMid.showturtle()
    greyCarMid.right(180)

    redTender.speed(1)
    redTender.hideturtle()
    redTender.shape("car8.gif")
    redTender.penup()
    redTender.goto(-500, 100)
    redTender.showturtle()
    redTender.right(180)

    perpul.speed(1)
    perpul.hideturtle()
    perpul.shape("car9.gif")
    perpul.penup()
    perpul.goto(-900, 100)
    perpul.showturtle()
    perpul.right(180)


setup_cars()

move_cars()


#איש אוסף מטבעות
wn.addshape('adventurer_idle.gif')
wn.addshape('adventurer_walk2.gif')
wn.addshape('adventurer_walk1.gif')
wn.addshape('adventurer_cheer2.gif')
wn.addshape('adventurer_swim2.gif')
wn.addshape('adventurer_stand.gif')
wn.addshape('adventurer_swim1.gif')
wn.addshape('adventurer_back (3).gif')
wn.addshape('adventurer_back (2).gif')

player = turtle.Turtle()
player.penup()
player.shape('adventurer_idle.gif')
player.goto(0, -160)
player.setheading(90)

score = 0
score_pen = turtle.Turtle()
score_pen.speed('fastest')
score_pen.color("red")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

coins = []
num_coins = 1

def move_up():
    player.sety(player.ycor() + 20)
    player.shape('adventurer_back (3).gif')

def move_down():
    player.sety(player.ycor() - 20)
    player.shape('adventurer_idle.gif')

def move_left():
    player.setx(player.xcor() - 20)
    player.shape('adventurer_swim2.gif')
    player.setheading(180)

def move_right():
    player.setx(player.xcor() + 20)
    player.shape('adventurer_walk2.gif')
    player.setheading(0)

# קובעים שיעורים לכפתורים
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

for _ in range(num_coins):
    coin = turtle.Turtle()
    wn.addshape("coin.gif")
    coin.shape("coin.gif")
    coin.penup()
    coin.goto(random.randint(-280, 280), random.randint(-280, 200))
    coins.append(coin)

def update():
    global score

    for dirty in dirties:
        if player.distance(dirty) < 45:
            score -= 5
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
            change_position(dirty)

    for coin in coins:
        if player.distance(coin) < 45:
            coin.goto(random.randint(-280, 280), random.randint(-280, 200))
            score += 5
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
            player.shape('adventurer_cheer2.gif')
            time.sleep(0.1)
            player.shape('adventurer_walk2.gif')

    for car in [redCar, greyCarMid, blueCar, redTender, greenTender, yellowCar, perpul]:
        if player.distance(car) < 55:
            game_over()
            return

    wn.update()
    turtle.ontimer(update, 1000 // 60)

def play_game():
    update()

def game_over():
    global score
    player.hideturtle()
    for coin in coins:
        coin.hideturtle()
    for dirty in dirties:
        dirty.hideturtle()

    game_over_pen = turtle.Turtle()
    game_over_pen.speed(0)
    game_over_pen.color("red")
    game_over_pen.penup()
    game_over_pen.setposition(0, 0)
    game_over_pen.write("Game Over!", align="center", font=("Courier", 54, "bold"))
    game_over_pen.setposition(0, -30)
    game_over_pen.write("Your score is: {}".format(score), align="center", font=("Courier", 24, "bold"))

    time.sleep(4)
    game_over_pen.clear()
    game_over_pen.hideturtle()
    player.penup()
    player.goto(0, -160)
    player.showturtle()

    for coin in coins:
        coin.showturtle()

    for dirty in dirties:
        dirty.showturtle()
    play_game()


# Set up initial positions and properties of the cars
def setup_cars():

    setup_cars()
move_cars()

def start_again(x, y):
    wn.onclick(start_again, btn=1, add=True)
play_game()
turtle.done()