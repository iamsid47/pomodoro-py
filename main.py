import time
import tkinter as tk
from tkinter import ttk, PhotoImage
import threading

class Pomodoro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodoro Timer")
        
        self.root.mainloop()
        
Pomodoro()