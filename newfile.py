import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

folder_path = filedialog.askopenfile()
print(folder_path.name)
