from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_tim = []
        self.create_snake()
        self.head = self.all_tim[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_tim = Turtle("square")
        new_tim.color("white")
        new_tim.penup()
        new_tim.goto(position)
        self.all_tim.append(new_tim)

    def extend(self):
        self.add_segment(self.all_tim[-1].position())

    def move(self):
        for t_num in range(len(self.all_tim) - 1, 0, -1):
            new_x = self.all_tim[t_num - 1].xcor()
            new_y = self.all_tim[t_num - 1].ycor()
            self.all_tim[t_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)