import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
root=Tk()
root.geometry("820x620")
root.config(bg="grey")

# noun = pd.read_csv('substantiv.csv')
# adjective = pd.read_csv('adjektiv.csv')
# verb = pd.read_csv('verben.csv')
# adverb = pd.read_csv('adverb.csv')
# pronoun = pd.read_csv('fürwort.csv')
# preposition = pd.read_csv('präposition.csv')
# conjunction = pd.read_csv('konjunktion.csv')

# - - - - - - - - - - function - - - - - - - - - - -



# - - - - - - - - - - - view - - - - - - - - - - - - 

canvas = Canvas(root,bg = "white")
canvas.place(x = 10, y = 10, width = 800, height =600)
root.mainloop()