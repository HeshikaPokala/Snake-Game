from turtle import Turtle

DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.square(number=3)  # You are creating/calling the func 'square' as soon as you are using the Snake Class
        self.head = self.all_turtles[0]
        self.speed_level = 1

    def square(self, number):
        for pos in range(0, number):
            self.new_square()

    def new_square(self):
        new_square = Turtle()
        new_square.shape("square")
        new_square.color("white")
        new_square.penup()
        new_x = -(len(self.all_turtles) * 20)
        new_y = 1
        new_square.goto(x=new_x, y=new_y)
        self.all_turtles.append(new_square)

    def snake_movement(self):
        for sq in range(len(self.all_turtles) - 1, 0, -1):  # len =3-1=2 (0,1,2)
            new_x_cor = self.all_turtles[sq - 1].xcor()  # we need to assign 1st position to 2nd so sq-1
            new_y_cor = self.all_turtles[sq - 1].ycor()
            self.all_turtles[sq].goto(new_x_cor, new_y_cor)

        self.all_turtles[0].forward(DISTANCE)

    def up(self):
        if self.all_turtles[0].heading() != DOWN:
            self.all_turtles[0].setheading(UP)

    def down(self):
        if self.all_turtles[0].heading() != UP:
            self.all_turtles[0].setheading(DOWN)

    def right(self):
        if self.all_turtles[0].heading() != LEFT:
            self.all_turtles[0].setheading(RIGHT)

    def left(self):
        if self.all_turtles[0].heading() != RIGHT:
            self.all_turtles[0].setheading(LEFT)

