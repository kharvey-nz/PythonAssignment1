'''
Author: Kyle Harvey 18473155
Pledge of Honour: I pledge by honour that this program is solely my own work.
Description: This program uses functions to build up an image using turtle of
             a podium for first place, second place, and third place people
             to stand on. Upon each podium spot will be drawn a person with
             their bodies matching the podium place they stand on.
'''
# A lot of style guides recommend not using the import * and instead
# I should explicitly import each class/module
# but now I have 3 lines of import from turtle alone
from turtle import up, goto, down, speed, pensize, pencolor, hideturtle
from turtle import exitonclick, circle, begin_fill, end_fill, fillcolor
from turtle import setheading, forward, left, right


def move_to(x, y):
    '''
    move_to(x, y):
    This function will move the position of the turtle without drawing anything
    , up and down are related to penup and pendown.
    '''
    up()
    goto(x, y)
    down()


def draw_head(x, y, radius):
    '''
    draw_head(x, y, radius):
    This function will draw a circle with the specified radius at the specified
    location x, y. (location of circle relative to x and y is that x, y specify
    the bottom of the circle)
    '''
    move_to(x, y)
    # remember in move_to the down() function gets called so we can draw
    circle(radius)


def draw_line(x1, y1, x2, y2):
    '''
    draw_line(x1, y1, x2, y2):
    This will draw a line with one end starting at x1, y1 and the other end
    at x2, y2. No other lines should be drawn thanks to the move_to function.
    '''
    move_to(x1, y1)
    # remember in move_to the down() function gets called so we can draw
    goto(x2, y2)


def draw_block(x, y, width, height, colour):
    '''
    draw_block(x, y, width, height, colour):
    Draws a block with the bottom left corner at x and y. The block's width
    and height are specified as width and height and the block will be filled
    with the colour specified with colour.
    '''
    move_to(x, y)
    fillcolor(colour)  # set the fill colour before filling in our graphics
    begin_fill()
    # the following could be replaced by a loop of 4 iterations
    # of forwards and lefts
    goto(x + width, y)  # goto bottom right point
    goto(x + width, y + height)  # goto top right point
    goto(x, y + height)  # goto top left point
    goto(x, y)  # goto bottom left point which is our starting point
    end_fill()


def draw_podium(winner_colour, second_colour, third_colour):
    '''
    draw_podium(winner_colour, second_colour, third_colour):
    This function will draw 3 blocks in the style of a podium.
    Each block of the podium will be given a specific colour and have
    a specific set of dimensions for each block.
    '''
    draw_block(0, 0, 60, 60, second_colour)  # first block of podium
    draw_block(60, 0, 60, 90, winner_colour)  # middle block of podium
    draw_block(120, 0, 60, 40, third_colour)  # last block of podium


def draw_winner(winner_colour):
    '''
    draw_winner(winner_colour):
    This function will draw a person on the winning block of the podium.
    The person will be drawn with the specific colour winner_colour.
    '''
    draw_head(90, 160, 10)  # head of winner
    draw_line(90, 140, 60, 180)  # left arm
    draw_line(90, 140, 120, 180)  # right arm
    draw_line(80, 90, 80, 120)  # left leg
    draw_line(100, 90, 100, 120)  # right leg
    draw_block(70, 120, 40, 40, winner_colour)  # winner body


def draw_second(second_colour):
    '''
    draw_second(second_colour):
    This function will draw a person on the part of the podium for runner ups.
    The person will be drawn with the colour second_colour.
    '''
    draw_head(30, 125, 10)  # head of second person
    draw_line(30, 110, 0, 130)  # left arm
    draw_line(30, 110, 60, 130)  # right arm
    draw_line(20, 90, 20, 60)  # left leg
    draw_line(40, 90, 40, 60)  # right leg
    # start building the triangle body
    move_to(10, 90)
    setheading(0)  # draw forward by moving in the positive x direction
    fillcolor(second_colour)
    begin_fill()
    for i in range(3):  # for the 3 sides of the triangle
        forward(40)  # draw a line
        left(120)  # then turn 1/3 of a circle anti-clockwise
    end_fill()


def draw_third(third_colour):
    '''
    draw_third(third_colour):
    This function will draw a person on the third place part of the podium.
    The person will get the colour third_colour as the fill colour.
    '''
    draw_head(150, 90, 10)  # head of third person
    draw_line(150, 70, 120, 120)  # left arm
    draw_line(150, 70, 180, 120)  # right arm
    draw_line(140, 40, 140, 70)  # left leg
    draw_line(160, 40, 160, 70)  # right leg
    # start building the triangle body
    move_to(130, 90)
    setheading(0)  # draw forward by moving in the positive x direction
    fillcolor(third_colour)
    begin_fill()
    for i in range(3):  # for the 3 sides of the triangle
        forward(40)  # draw a line
        right(120)  # the turn 1/3 of a circle clockwise
    end_fill()


def main():
    '''
    main():
    This is the main function with a few set up statements before
    the function in this program get called
    '''
    speed(0)  # faster drawing
    pensize(3)
    pencolor("black")
    # the colours for the person and podium place
    winner_colour = "red"
    second_colour = "orange"
    third_colour = "purple"

    # draw podium first
    draw_podium(winner_colour, second_colour, third_colour)  # draw podium
    # draw from left to right
    draw_second(second_colour)  # the runner up
    draw_winner(winner_colour)  # the winner
    draw_third(third_colour)  # last place

    hideturtle()  # hide the turtle after drawing to make things look clean
    exitonclick()  # pause the program so we can see the drawing


main()
