#!/usr/bin/python3
# Morgan Butryn and Max Turner
# 2020-3-10
"""Makes/resets question pickle file for quizgame.py"""
import pickle

#[0] is the question
#[1] is the answer
#[2], [3], and [4] are the wrong answers

history = {1:["What year did the war of 1812 begin?", "1812", "1811", "1810", "1813"]}

geography = {1:["What is the capital city of Australia?", "Canberra", "Melbourne", "Perth", "Sydney"]}

music = {1:["Who finished Mozart's Requiem?", "Suessmayr", "Beethoven", "Bach", "Mozart"]}

games = {1:["What day did the Elder Scrolls V: Skyrim release?", "11/11/11", "10/10/10", "12/12/12", "13/13/13"]}

questions = [history, geography, music, games]
pfile = open("questions.pickle", "wb")
pickle.dump(questions, pfile)
pfile.close()