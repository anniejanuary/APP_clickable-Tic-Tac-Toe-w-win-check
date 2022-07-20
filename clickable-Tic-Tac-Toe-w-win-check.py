import turtle
import random
import time

window = turtle.Screen()

side = 600
X = -300
Y = 300

window.setup(side, side)
window.title('Tic Tac Toe')
window.bgcolor('black')

xo = turtle.Turtle()
xo.color('white')
xo.speed(0)
xo.pensize(7)
xo.hideturtle()

board = [[None, None, None],
           [None, None, None],
           [None, None, None]]

turn = random.choice(['x', 'o'])

# linie

distance = int(side / 3)

for a in [1, 2]:
    xo.penup()
    xo.goto(X + a * distance, Y)
    xo.pendown()
    xo.goto(X + a * distance, -Y)

    xo.penup()
    xo.goto(X, Y - a * distance)
    xo.pendown()
    xo.goto(-X, Y - a * distance)


def check():
    # po skosie
    if board[0][0] == board[1][1] == board[2][2]: return board[2][2]
    if board[0][2] == board[1][1] == board[2][0]: return board[2][0]

    # w wierszu
    for w in range(3):
        if board[w][0] == board[w][1] == board[w][2]: return board[w][0]

    # w kolumnie
    for k in range(2):
        if board[0][k] == board[1][k] == board[2][k]: return board[0][k]

    return None


def click(x, y):
    global turn

    # które to pole
    column = 0
    row = 0

    if x < X + distance:
        column = 0
    elif x > X + 2 * distance:
        column = 2
    else:
        column = 1

    if y < Y - 2 * distance:
        row = 2
    elif y > Y - distance:
        row = 0
    else:
        row = 1

    # pole jest puste ?

    if board[row][column] != None: return

    # narysować

    column_center = (column * distance + distance / 2) - side / 2
    row_center = (-row * distance - distance / 2) + side / 2

    xo.penup()
    xo.goto(column_center - 25, row_center - 25)
    if turn == 'x':
        xo.write('X', font=('Arial', 50))
    else:
        xo.write('O', font=('Arial', 50))

    # dodać informację x / o

    board[row][column] = turn

    if turn == 'o':
        turn = 'x'
    else:
        turn = 'o'

    # sprawdź

    if check() != None:
        xo.penup()
        xo.goto(-150, 0)
        time.sleep(1)
        xo.clear()
        xo.write(f"{check()} has won!", font=("Arial", 50))


window.onclick(click)

window.listen()
window.mainloop()
