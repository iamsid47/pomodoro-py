import time
import tkinter as tk
from tkinter import ttk
import threading

class Pomodoro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodoro Timer")
        
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Inter", 14))
        self.s.configure("TButton", font=("Inter", 14))
        
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)
        
        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)
        
        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font=("Inter", 48))
        self.pomodoro_timer_label.pack(pady = 20)
        
        self.short_break_timer_label = ttk.Label(self.tab2, text="5:00", font=("Inter", 48))
        self.short_break_timer_label.pack(pady = 20)
        
        self.long_break_timer_label = ttk.Label(self.tab3, text="15:00", font=("Inter", 48))
        self.long_break_timer_label.pack(pady = 20)
        
        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")
        
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=20)
        
        self.start_button = ttk.Button(self.grid_layout, text="Start Timer", command=self.timer_threading)     
        self.start_button.grid(row=0, column=0)
        
        self.skip_button = ttk.Button(self.grid_layout, text="Skip", command=self.skip_clock)     
        self.skip_button.grid(row=0, column=1)
        
        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.reset_clock)     
        self.reset_button.grid(row=0, column=2)
        
        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Pomodoro: 0", font=("Inter", 16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)
        
        self.root.mainloop()
    
    def timer_threading (self):
        pass
        
    def timer (self):
        pass
    
    def reset_clock (self):
        pass
    
    def skip_clock (self):
        pass
        
Pomodoro()