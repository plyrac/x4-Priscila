from tkinter import *
from functools import partial


global ROWS
global COLUMNS
global canvas
global mainWindow
global currentCol
global haveNew


SQUARE_SIZE = 60
COIN_RADIUS = 0.8 * SQUARE_SIZE / 2
BOARD_PADDING = 10
BUTTON_MARGING = 10

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

COLORS = ["#000000", "#FFD700", "#008000", "#4682B4", "#DC143C", "#8B0000"]

haveNew = False
currentCol = 0

# Pegar coluna escolhida pelo jogador


def getCol():
    global haveNew
    global currentCol
    global mainWindow

    while not haveNew:
        mainWindow.update()

    haveNew = False

    return (currentCol + 1)

def mouseClick(value):
    global haveNew
    global currentCol

    haveNew = True
    currentCol = int(value)

def initGUI(linhas, colunas):
    global ROWS
    global COLUMNS
    global canvas
    global mainWindow

    ROWS = linhas
    COLUMNS = colunas

    mainWindow = Tk()
    canvas = Canvas(mainWindow, width = COLUMNS * SQUARE_SIZE +
                                        2 * BOARD_PADDING, height = ROWS * SQUARE_SIZE + 2 * BOARD_PADDING)

    label = Label(mainWindow, text="x4 - Priscila Lyra Cabral")
    label.pack()

    mainWindow.resizable(0,0)
    button = []
    for col_ in range(0, COLUMNS):
        buttonOriginX = BOARD_PADDING + BUTTON_MARGING + (col_ * SQUARE_SIZE)
        button.append(Button(mainWindow, text=col_, command=partial(mouseClick, col_)))
        button[col_].place(height=SQUARE_SIZE - 2 * BUTTON_MARGING, width=SQUARE_SIZE- 2 * BUTTON_MARGING,
                           x=buttonOriginX, y=ROWS * SQUARE_SIZE + SQUARE_SIZE/2 + BUTTON_MARGING)

        for row_ in range(0, ROWS):
            squareOriginX = BOARD_PADDING + col_ * SQUARE_SIZE
            squareOriginY = BOARD_PADDING + row_ * SQUARE_SIZE

            circleOriginX = BOARD_PADDING + col_ * SQUARE_SIZE + SQUARE_SIZE/2
            circleOriginY = BOARD_PADDING + row_ * SQUARE_SIZE + SQUARE_SIZE / 2

            canvas.create_rectangle(squareOriginX, squareOriginY, squareOriginX + SQUARE_SIZE, squareOriginY + SQUARE_SIZE, fill="#e1b12c")
            canvas.create_oval(circleOriginX-COIN_RADIUS, circleOriginY - COIN_RADIUS, circleOriginX + COIN_RADIUS, circleOriginY + COIN_RADIUS, fill="#000000")

            canvas.pack(fill=BOTH, expand=1)

            mainWindow.geometry(str((COLUMNS) * SQUARE_SIZE + 2 * BOARD_PADDING) +
                                    "x" + str((ROWS+1)*SQUARE_SIZE + 4 * BOARD_PADDING))

            mainWindow.update()


def plotPieces(matriz):
    global canvas
    global mainWindow

    for x in range(0,len(matriz[0])):
        for y in range(0, len(matriz)):
            if matriz[y][x][2]:
                circleOriginX = BOARD_PADDING + x * SQUARE_SIZE + SQUARE_SIZE / 2
                circleOriginY = BOARD_PADDING + y * SQUARE_SIZE + SQUARE_SIZE / 2
                canvas.create_oval(circleOriginX - COIN_RADIUS, circleOriginY - COIN_RADIUS,
                                   circleOriginX + COIN_RADIUS, circleOriginY + COIN_RADIUS,
                                   fill=COLORS[matriz[y][x][2]])
    mainWindow.update()


def vencedor(winner):
    popup = Tk()
    popup.wm_title("VENCEDOR")
    label = Label(popup, text=str(winner) + " venceu!", font=LARGE_FONT)
    label.pack(side="top", fill="x", pady=10)

    popup.update()


def fim(placar):
    popup = Tk()
    popup.wm_title("Fim de jogo")
    label = Label(popup, text=str(placar[0]) + " fez " + str(len(placar)) + " ponto(s)!" + "\n" +
                              "obs. para fechar o jogo, apertar botão vermelho (X)", font=LARGE_FONT)
    label.pack(side="top", fill="x", pady=10)

    popup.update()


def fechar():
    mainWindow.protocol("WM_DELETE_WINDOW", on_closing)
    mainWindow.mainloop()


def on_closing():
    mainWindow.destroy()