import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Simple Human Shape with Chest and Genitalia Labels")

t = turtle.Turtle()
t.speed(3)
t.pensize(2)

# Helper to write labels
def label(text, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text, font=("Arial", 12, "bold"))

# Draw head (circle filled)
def draw_head():
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.fillcolor("peachpuff")
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    label("Head", -60, 130)

# Draw eyes (two small black circles)
def draw_eyes():
    eye_y = 130
    eye_x_offset = 12
    eye_radius = 4

    # Left eye
    t.penup()
    t.goto(-eye_x_offset, eye_y)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(eye_radius)
    t.end_fill()

    # Right eye
    t.penup()
    t.goto(eye_x_offset, eye_y)
    t.pendown()
    t.begin_fill()
    t.circle(eye_radius)
    t.end_fill()

    label("Eyes", 40, 135)

# Draw nose (simple triangle)
def draw_nose():
    t.penup()
    t.goto(0, 125)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.goto(-5, 95)
    t.goto(5, 95)
    t.goto(0, 105)
    t.end_fill()
    label("Nose", 15, 95)

# Draw ears (two half-circles on sides)
def draw_ears():
    ear_y = 120
    ear_x_offset = 30
    ear_radius = 10

    # Left ear
    t.penup()
    t.goto(-ear_x_offset, ear_y)
    t.setheading(90)
    t.pendown()
    t.fillcolor("peachpuff")
    t.begin_fill()
    t.circle(ear_radius, 180)  # half circle
    t.end_fill()

    # Right ear
    t.penup()
    t.goto(ear_x_offset, ear_y)
    t.setheading(270)
    t.pendown()
    t.begin_fill()
    t.circle(ear_radius, 180)  # half circle
    t.end_fill()

    label("Ears", 30, 120)

# Draw torso (rectangle filled)
def draw_torso():
    t.penup()
    t.goto(-30, 100)
    t.setheading(0)
    t.pendown()
    t.fillcolor("lightblue")
    t.begin_fill()
    for _ in range(2):
        t.forward(60)
        t.right(90)
        t.forward(80)
        t.right(90)
    t.end_fill()
    label("Torso", 40, 60)

# Draw chest (two overlapping circles on upper torso)
def draw_chest():
    t.penup()
    t.goto(-15, 70)
    t.pendown()
    t.fillcolor("pink")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.goto(15, 70)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    label("Chest", 40, 85)

# Draw genitalia (small oval under torso)
def draw_genitalia():
    t.penup()
    t.goto(-10, 10)
    t.pendown()
    t.fillcolor("lightpink")
    t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.circle(10, 90)
        t.circle(5, 90)
    t.end_fill()
    label("Genitalia", 20, 5)

# Draw left arm (rectangle filled)
def draw_left_arm():
    t.penup()
    t.goto(-70, 90)
    t.setheading(0)
    t.pendown()
    t.fillcolor("lightblue")
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.right(90)
        t.forward(15)
        t.right(90)
    t.end_fill()
    label("Left Arm", -120, 70)

# Draw right arm (rectangle filled)
def draw_right_arm():
    t.penup()
    t.goto(30, 90)
    t.setheading(0)
    t.pendown()
    t.fillcolor("lightblue")
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.right(90)
        t.forward(15)
        t.right(90)
    t.end_fill()
    label("Right Arm", 80, 70)

# Draw left leg (rectangle filled)
def draw_left_leg():
    t.penup()
    t.goto(-25, 20)
    t.setheading(0)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.right(90)
        t.forward(60)
        t.right(90)
    t.end_fill()
    label("Left Leg", -70, -30)

# Draw right leg (rectangle filled)
def draw_right_leg():
    t.penup()
    t.goto(5, 20)
    t.setheading(0)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.right(90)
        t.forward(60)
        t.right(90)
    t.end_fill()
    label("Right Leg", 40, -30)

# Draw all parts
draw_head()
draw_ears()
draw_eyes()
draw_nose()
draw_torso()
draw_chest()
draw_genitalia()
draw_left_arm()
draw_right_arm()
draw_left_leg()
draw_right_leg()

t.hideturtle()
turtle.done()
