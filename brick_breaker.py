import tkinter as tk
import random
import math
import copy

# Main class: inherit from tk.Canvas class
class Game(tk.Canvas):
    textDisplayed = False
    linesNb = 20
    seconds = 0

    # Bar Properties
    barHeight = 20
    barSpeed = 10

    # Ball property
    ballSpeed = 7

    # Bricks Properties
    bricks = []
    bricksWidth = 50
    bricksHeight = 20
    bricksNbByLine = 16
    bricksColors = {
        "r": "#e74c3c",
        "g": "#2ecc71",
        "b": "#3498db",
        "t": "#1abc9c",
        "p": "#9b59b6",
        "y": "#f1c40f",
        "o": "#e67e22",
    }

    # Screen properties
    screenHeight = 500
    screenWidth = bricksWidth*bricksNbByLine

    # This method initializes some attributes: the ball, the bar...
    def __init__(self,root):
        tk.Canvas.__init__(self,root,bg="#ffffff", bd=0,highlightthickness=0, relief="ridge", width=self.screenWidth, height=self.screenHeight)
        self.pack()
        