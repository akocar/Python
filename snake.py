import turtle
import time
import random

delay = 0.1

point = 0
high_point = 0

# Screen
wn = turtle.Screen()
print(wn)
wn.title("Snake game by Haznedar")
wn.bgcolor("orange")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0, 100)

segments = []

# Scoreboard
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("green")
score.penup()
score.hideturtle()
score.goto(0, 262)
score.write("Score: 0  High Score: 0", align="center",
            font=("Courier", 24, "normal"))

# Funcs


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Game loop
while True:
    wn.update()

    # Check for a collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(0.7)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        point = 0

        delay = 0.1

        score.clear()
        score.write("Score: {}  High Score: {}".format(
            point, high_point), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        # Increasing the score
        point += 10

        if point > high_point:
            high_point = point

        score.clear()
        score.write("Score: {}  High Score: {}".format(
            point, high_point), align="center", font=("Courier", 24, "normal"))

# Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

# Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Head collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.7)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(2000, 2000)

            segments.clear()

            point = 0

            delay = 0.1

            score.clear()
            score.write("Score: {}  High Score: {}".format(
                point, high_point), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
