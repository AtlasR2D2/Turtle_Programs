import turtle as t
import shapes as sh
import random
import colorgram
from math import sqrt

def timmy_draw_a_square_w_cross():
    timmy_the_turtle = t.Turtle()
    timmy_the_turtle.shape("turtle")
    timmy_the_turtle.color("blue")

    SINGLE_MOVE = 100
    LEFT_EDGE_ORD_x = 0 - SINGLE_MOVE/2
    LEFT_EDGE_ORD_y = 0
    RIGHT_EDGE_ORD_x = 0 + SINGLE_MOVE/2
    RIGHT_EDGE_ORD_y = 0
    BOTTOM_EDGE_ORD_x = 0
    BOTTOM_EDGE_ORD_y = 0 - SINGLE_MOVE/2
    TOP_EDGE_ORD_x = 0
    TOP_EDGE_ORD_y = 0 + SINGLE_MOVE/2

    DASHES_COUNT = 10

    DASH_LENGTH = SINGLE_MOVE / DASHES_COUNT * (2/3)
    SPACE_LENGTH = SINGLE_MOVE / DASHES_COUNT * (1/3)

    # Draw me a square Timmy!
    timmy_the_turtle.penup()
    timmy_the_turtle.goto(x=-50, y=-50)
    timmy_the_turtle.pendown()
    for move in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(90)

    # Return Timmy home!
    timmy_the_turtle.penup()
    timmy_the_turtle.goto(x=0, y=0)
    timmy_the_turtle.pendown()

    # Draw me a dashed line through the middle as a cross Timmy!
    timmy_the_turtle.penup()
    timmy_the_turtle.goto(x=LEFT_EDGE_ORD_x, y=LEFT_EDGE_ORD_y)
    blnDash = True
    blnExit = False
    while timmy_the_turtle.xcor() < RIGHT_EDGE_ORD_x and not blnExit:
        if blnDash:
            blnExit = (timmy_the_turtle.xcor() + DASH_LENGTH > RIGHT_EDGE_ORD_x)
            if blnExit:
                continue
            timmy_the_turtle.pendown()
            timmy_the_turtle.forward(DASH_LENGTH)
            blnDash = False
        else:
            blnExit = (timmy_the_turtle.xcor() + SPACE_LENGTH > RIGHT_EDGE_ORD_x)
            if blnExit:
                continue
            timmy_the_turtle.penup()
            timmy_the_turtle.forward(SPACE_LENGTH)
            blnDash = True

    timmy_the_turtle.penup()
    timmy_the_turtle.goto(x=BOTTOM_EDGE_ORD_x, y=BOTTOM_EDGE_ORD_y)
    # Turn Timmy North
    timmy_the_turtle.left(90)
    blnDash = True
    blnExit = False
    while timmy_the_turtle.ycor() < TOP_EDGE_ORD_y and not blnExit:
        if blnDash:
            blnExit = (timmy_the_turtle.ycor() + DASH_LENGTH > TOP_EDGE_ORD_y)
            if blnExit:
                continue
            timmy_the_turtle.pendown()
            timmy_the_turtle.forward(DASH_LENGTH)
            blnDash = False
        else:
            blnExit = (timmy_the_turtle.ycor() + SPACE_LENGTH > TOP_EDGE_ORD_y)
            if blnExit:
                continue
            timmy_the_turtle.penup()
            timmy_the_turtle.forward(SPACE_LENGTH)
            blnDash = True

    # Rotate Timmy to the East
    timmy_the_turtle.right(90)
    # Return Timmy home!
    timmy_the_turtle.penup()
    timmy_the_turtle.goto(x=0, y=0)
    timmy_the_turtle.pendown()

    screen = t.Screen()
    screen.exitonclick()


def draw_shapes(max_shape_sides, shape_side_length):
    # Initialise Shapes List
    shapes = sh.initialise_shapes(max_sides=max_shape_sides, side_length_x=shape_side_length)
    # print(f"Shapes Length: {len(shapes)}")
    tam = t.Turtle()
    for shape in shapes:
        tam.penup()
        # Reset tam's position
        tam.goto(x=0, y=0)
        tam.setheading(to_angle=0)
        tam.pendown()
        # Draw the shape
        for side_x in range(1, shape.sides+1):
            # If not first side then rotate right for corner angle
            if side_x != 1:
                tam.right(shape.corner_angle)
            tam.forward(shape.side_length)
    tam.penup()
    # Hide Tam
    tam.hideturtle()

    screen = t.Screen()
    screen.exitonclick()

def random_walk(num_steps, step_size, rand_color_flag):
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
              "SeaGreen"
    ]

    max_degrees = 360
    right_angle = 90
    headings = [x for x in range(0, max_degrees+1, right_angle)]
    print(headings)
    george = t.Turtle()
    george.pensize(10)
    george.speed(speed=0)
    george.hideturtle()
    # Initialise Random Number Generator
    random.seed()
    for step_x in range(0, num_steps):
        heading_x = random.choice(headings)
        if rand_color_flag:
            t.colormode(255)
            color_x = random_color()
        else:
            color_x = random.choice(colors)
        george.pencolor(color_x)
        george.setheading(to_angle=heading_x)
        george.forward(step_size)
        random.seed()

    screen = t.Screen()
    screen.exitonclick()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_circle(turtle_x,radius_x):
    turtle_x.circle(radius_x)


def draw_spirograph(num_circles, step_size, radius_size, rand_color_flag):
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
              "SeaGreen"
    ]

    max_degrees = 360
    angle_x = max_degrees / num_circles
    george = t.Turtle()
    # george.pensize(10)
    george.speed(speed=0)
    george.hideturtle()
    # Initialise Random Number Generator
    random.seed()
    for step_x in range(0, num_circles):
        if rand_color_flag:
            t.colormode(255)
            color_x = random_color()
        else:
            color_x = random.choice(colors)
        george.pencolor(color_x)
        george.left(angle=angle_x)
        draw_circle(turtle_x=george, radius_x=radius_size)
        random.seed()

    screen = t.Screen()
    screen.exitonclick()

def extract_colors(num_cols_x):
    colors = colorgram.extract('HirstPainting.jpg', num_cols_x)
    colors_rgb = [(color.rgb.r,color.rgb.g,color.rgb.b) for color in colors]
    return colors_rgb

def draw_hirst_painting(num_cols, pen_size_x, dot_space_x):

    DOT_SPACE = dot_space_x
    EDGE_BUFFER = 20
    EDGE_LENGTH = 500
    SCREEN_HEIGHT = EDGE_LENGTH
    SCREEN_WIDTH = EDGE_LENGTH
    # Calculate Edge Buffer
    EDGE_BUFFER = max(EDGE_BUFFER, (SCREEN_WIDTH - int(sqrt(num_cols)) * pen_size_x - (int(sqrt(num_cols)) - 1) * dot_space_x) / 2)

    LEFT_EDGE = - SCREEN_WIDTH/2 + EDGE_BUFFER
    RIGHT_EDGE = SCREEN_WIDTH / 2 - EDGE_BUFFER
    BOTTOM_EDGE = -SCREEN_WIDTH / 2 + EDGE_BUFFER
    TOP_EDGE = SCREEN_WIDTH / 2 - EDGE_BUFFER
    print(f"LEFT EDGE: {LEFT_EDGE}, RIGHT EDGE: {RIGHT_EDGE}, BOTTOM_EDGE: {BOTTOM_EDGE}, TOP_EDGE: {TOP_EDGE}")

    # ivan.speed(speed=0)
    # ivan.shape("circle")
    colors = extract_colors(num_cols)
    turtles = [t.Turtle() for color in range(num_cols)]

    t.colormode(255)
    x_ord = 0
    y_ord = 0
    for i in range(num_cols):
        turtle_x = turtles[i]
        turtle_x.speed("fastest")
        turtle_x.fillcolor(random.choice(colors))
        turtle_x.shape("circle")
        turtle_x.pensize(pen_size_x)
        turtle_x.penup()
        x_coordinate = LEFT_EDGE + (pen_size_x + dot_space_x) * x_ord
        y_coordinate = BOTTOM_EDGE + (pen_size_x + dot_space_x) * y_ord
        turtle_x.goto(x=x_coordinate, y=y_coordinate)
        if x_coordinate + (pen_size_x + dot_space_x) >= RIGHT_EDGE:
            x_ord = 0
            y_ord += 1
        else:
            x_ord += 1

    screen = t.Screen()
    screen.screensize(canvwidth=SCREEN_WIDTH, canvheight=SCREEN_HEIGHT)
    screen.exitonclick()