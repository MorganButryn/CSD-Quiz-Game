#!/usr/bin/python3
# Morgan Butryn and Max Turner
# 2020-3-10
"""GUI-based trivia game"""

#imports
import pickle
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
        self.btn_hist = tk.Button(self, text="History", font=MEDIUM, command=self.go_hist)
        self.btn_hist.grid(row = 1, column = 1, sticky = "news")
        
        self.btn_geo = tk.Button(self, text="Geography", font=MEDIUM, command=self.go_geo)
        self.btn_geo.grid(row = 2, column = 1, sticky = "news")
        
        self.btn_music = tk.Button(self, text="Music", font=MEDIUM, command=self.go_music)
        self.btn_music.grid(row = 3, column = 1, sticky = "news")
        
        self.btn_games = tk.Button(self, text="Video Games", font=MEDIUM, command=self.go_games)
        self.btn_games.grid(row = 4, column = 1, sticky = "news")
        
        self.btn_rand = tk.Button(self, text="Random", font=MEDIUM, command=self.go_rand)
        self.btn_rand.grid(row = 5, column = 1, sticky = "news")
        
        self.btn_back = tk.Button(self, text="Back", font=MEDIUM, command=self.go_back)
        self.btn_back.grid(row = 6, column = 1, sticky = "news")
        
    def go_hist(self):
        QuizGame.quiz_type = 1
        QuizGame.count = 1
        QuizGame.score = 0
        Screen.current = 3
        Screen.switch_frame()
        
    def go_geo(self):
        QuizGame.quiz_type = 2
        QuizGame.count = 1
        QuizGame.score = 0
        Screen.current = 3
        Screen.switch_frame()
        
    def go_music(self):
        QuizGame.quiz_type = 3
        QuizGame.count = 1
        QuizGame.score = 0
        Screen.current = 3
        Screen.switch_frame()
        
    def go_games(self):
        QuizGame.quiz_type = 4
        QuizGame.count = 1
        QuizGame.score = 0
        Screen.current = 3
        Screen.switch_frame()
    
    def go_rand(self):
        QuizGame.quiz_type = 0
        QuizGame.count = 1
        QuizGame.score = 0
        Screen.current = 3
        Screen.switch_frame()        
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()
        
class QuizGame(Screen):
    quiz_type = 0
    count = 1
    score = 0
    def __init__(self):
        Screen.__init__(self)
        
        # 0 = random
        # 1 = history
        # 2 = geography
        # 3 = music
        # 4 = games
        
        pfile = open("questions.pickle", "rb")
        self.questions = pickle.load(pfile)
        pfile.close()
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 2)
        
        #Entry boxes
        self.ent_count = tk.Entry(self, font=MEDIUM)
        self.ent_count.insert(0, "Question #1")
        self.ent_count.grid(row = 0, column = 0, sticky = "news")
        self.ent_count.configure(state = "disabled")
        
        self.ent_score = tk.Entry(self, font=MEDIUM, text = "Score: 0")
        self.ent_score.grid(row = 0, column = 1, sticky = "news")
        self.ent_score.configure(state = "disabled")
        
        self.ent_a = tk.Entry(self, font=SMALL)
        self.ent_a.grid(row = 2, column = 1, sticky = "news")
        self.ent_a.configure(state = "disabled")
        
        self.ent_b = tk.Entry(self, font=SMALL)
        self.ent_b.grid(row = 3, column = 1, sticky = "news")
        self.ent_b.configure(state = "disabled")
        
        self.ent_c = tk.Entry(self, font=SMALL)
        self.ent_c.grid(row = 4, column = 1, sticky = "news")
        self.ent_c.configure(state = "disabled")
        
        self.ent_d = tk.Entry(self, font=SMALL)
        self.ent_d.grid(row = 5, column = 1, sticky = "news")
        self.ent_d.configure(state = "disabled")
        
        #Radio Buttons
        self.answer = tk.IntVar(self)
        self.answer.set(0)
        
        self.rad_a = tk.Radiobutton(self, text = "A.", font=SMALL, variable=self.answer, value = 1, fg = "black")
        self.rad_a.grid(row = 2, column = 0, sticky = "news")
        
        self.rad_b = tk.Radiobutton(self, text = "B.", font=SMALL, variable=self.answer, value = 2, fg = "black")
        self.rad_b.grid(row = 3, column = 0, sticky = "news")
        
        self.rad_c = tk.Radiobutton(self, text = "C.", font=SMALL, variable=self.answer, value = 3, fg = "black")
        self.rad_c.grid(row = 4, column = 0, sticky = "news")
        
        self.rad_d = tk.Radiobutton(self, text = "D.", font=SMALL, variable=self.answer, value = 4, fg = "black")
        self.rad_d.grid(row = 5, column = 0, sticky = "news")
        
        #Scrolledtext
        self.scr_question = ScrolledText(self, height = 12, width = 12)
        self.scr_question.grid(row = 1, column = 0, columnspan = 2, sticky = "news")
        self.scr_question.configure(state = "disabled")
        
        #Buttons
        self.btn_mainmenu = tk.Button(self, text="Main Menu", font=MEDIUM, command=self.mainmenu)
        self.btn_mainmenu.grid(row = 6, column = 0, sticky = "news")
        
        self.btn_submit = tk.Button(self, text="Submit", font=MEDIUM, command=self.nextquestion)
        self.btn_submit.grid(row = 6, column = 1, sticky = "news")
        
    def mainmenu(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def nextquestion(self):
        QuizGame.count += 1

        self.ent_count.configure(state = "normal")
        self.ent_count.delete(0, "end")
        self.ent_count.insert(0, "Question #"+str(QuizGame.count))
        self.ent_count.configure(state = "disabled")
    
class ScoreEntry(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        #Labels
        self.lbl_title = tk.Label(self, text="Your Score", font=LARGE)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 3, sticky = "news") 
        
        self.lbl_name = tk.Label(self, text="Enter Name:", font=LARGE)
        self.lbl_name.grid(row = 2, column = 0, columnspan = 3, sticky = "news")
        
        #Entry boxes
        self.ent_score = tk.Entry(self, font=MEDIUM)
        self.ent_score.grid(row = 1, column = 1, sticky = "news")
        self.ent_score.configure(state = "disabled")
        
        self.ent_name = tk.Entry(self, font=MEDIUM)
        self.ent_name.grid(row = 3, column = 1, sticky = "news")
        
        #Buttons
        self.btn_submit = tk.Button(self, text="Submit", font=MEDIUM, command=self.enter_score)
        self.btn_submit.grid(row = 4, column = 1, sticky = "news")
        
    def enter_score(self):
        Screen.current = 0
        Screen.switch_frame()        

    
#main
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x420")
    root.title("Quiz Game")
    
    screens = [MainMenu(), HighScores(), QuizSelect(), QuizGame(), ScoreEntry()]
    #screens[0] = Main Menu
    #screens[1] = High Scores
    #screens[2] = Quiz Selection
    #screens[3] = Game Screen
    #screens[4] = Score Entry
    
    for i in range(len(screens)):
        screens[i-1].grid(row = 0, column = 0, sticky = "news")
    
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    Screen.current = 4
    Screen.switch_frame()
    
    root.mainloop()    #must be last line