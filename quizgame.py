#!/usr/bin/python3
# Morgan Butryn and Max Turner
# 2020-3-10
"""GUI-based trivia game"""

#imports
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import random

LARGE = ("Verdana", "20")
MEDIUM = ("Verdana", "14")
SMALL = ("Verdana", "12")

#classes
class Screen(tk.Frame):
    current = 0
    def __init__(self):
        tk.Frame.__init__(self)
        
    def switch_frame():
        screens[Screen.current].tkraise()
        
class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        #Labels
        self.lbl_title = tk.Label(self, text="Quiz Game", font=LARGE)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        
        #Buttons
        self.btn_play = tk.Button(self, text="Play", font=MEDIUM, command=self.go_play)
        self.btn_play.grid(row = 1, column = 1, sticky = "news")
        
        self.btn_scores = tk.Button(self, text="High Scores", font=MEDIUM, command=self.go_scores)
        self.btn_scores.grid(row = 2, column = 1, sticky = "news")
        
        self.btn_quit = tk.Button(self, text="Quit", font=MEDIUM, command=quit)
        self.btn_quit.grid(row = 3, column = 1, sticky = "news")
        
    def go_scores(self):
        Screen.current = 1
        Screen.switch_frame()
    
    def go_play(self):
        Screen.current = 2
        Screen.switch_frame()
        
class HighScores(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        #Labels
        self.lbl_title = tk.Label(self, text="High Scores", font=LARGE)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        
        #Buttons
        self.btn_update = tk.Button(self, text="Update scores", font=MEDIUM, command=self.update_scores)
        self.btn_update.grid(row = 2, column = 1, sticky = "news")        
        
        self.btn_back = tk.Button(self, text="Back", font=MEDIUM, command=self.go_back)
        self.btn_back.grid(row = 3, column = 1, sticky = "news")        
        
        #Scrolledtext
        self.scr_scores = ScrolledText(self, height = 16, width = 50, font = SMALL)
        self.scr_scores.grid(row = 1, column = 1, sticky = "news")
        self.scr_scores.configure(state = "disabled")
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def update_scores(self):
        self.scr_scores.configure(state="normal")
        self.scr_scores.delete(0.0, "end")
        self.scr_scores.configure(state="disabled")
        
class QuizSelect(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)        
        
        #Labels
        self.lbl_title = tk.Label(self, text="Select a quiz:", font=LARGE)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 3, sticky = "news")        
        
        #Buttons
        self.btn_hist = tk.Button(self, text="History", font=MEDIUM)
        self.btn_hist.grid(row = 1, column = 1, sticky = "news")
        
        self.btn_geo = tk.Button(self, text="Geography", font=MEDIUM)
        self.btn_geo.grid(row = 2, column = 1, sticky = "news")
        
        self.btn_music = tk.Button(self, text="Music", font=MEDIUM)
        self.btn_music.grid(row = 3, column = 1, sticky = "news")
        
        self.btn_games = tk.Button(self, text="Video Games", font=MEDIUM)
        self.btn_games.grid(row = 4, column = 1, sticky = "news")
        
        self.btn_back = tk.Button(self, text="Back", font=MEDIUM, command=self.go_back)
        self.btn_back.grid(row = 5, column = 1, sticky = "news")
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()    
    
#main
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x420")
    root.title("Quiz Game")
    
    screens = [MainMenu(), HighScores(), QuizSelect()]
    #screens[0] = Main Menu
    #screens[1] = High Scores
    #screens[2] = Quiz Selection
    
    for i in range(len(screens)):
        screens[i-1].grid(row = 0, column = 0, sticky = "news")
    
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    
    Screen.current = 0
    Screen.switch_frame()
    
    root.mainloop()    #must be last line