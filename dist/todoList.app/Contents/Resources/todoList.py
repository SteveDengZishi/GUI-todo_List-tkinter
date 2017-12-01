#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:43:47 2017

@author: stevedeng
"""

import tkinter as tk
from tkinter import ttk

class tdList(tk.Tk):
    def __init__(self, tasks=None):
        
        super().__init__()
        
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
            
        self.title("TO DO APP")
        self.geometry("500x750")
        
        task1 = tk.Label(self, text="TASKS FOR TODAY", bg="thistle", fg="black", pady=20, font=("Times",23))
        
        self.tasks.append(task1)
        
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)
            
        self.task_create = tk.Text(self, height=3, bg="white", fg="black")
        
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()
        
        self.bind('<Return>', self.add_task)
        
        self.backGroundColor_lib = ["palegreen","lightskyblue","mistyrose","lightsalmon","wheat","beige","azure","paleturquoise","lavender","plum","lightcyan"]
        self.fontcolor_lib = ["black","orangered","maroon","darkcyan","darkslategray","purple","seagreen"]
    
    
    def add_task(self, event=None):
        new_text = self.task_create.get(1.0,tk.END).strip()
        
        if len(new_text) > 0:
            new_task = tk.Label(self, text = new_text, pady=20)
            done_button = ttk.Button(new_task, text = "done",command = lambda:self.removeTask(done_button))
            
            backGroundIdx = len(self.tasks)%len(self.backGroundColor_lib)
            fontIdx = len(self.tasks)%len(self.fontcolor_lib)
            
            backGroundColor = self.backGroundColor_lib[backGroundIdx]
            fontColor = self.fontcolor_lib[fontIdx]
            
            new_task.configure(bg=backGroundColor,fg=fontColor,font=("Times",20))
            
            new_task.pack(side=tk.TOP, fill=tk.X)
            done_button.pack(side=tk.RIGHT)
            
            self.tasks.append(new_task)
            
        self.task_create.delete(1.0, tk.END)
        
    def removeTask(self, done_button):
        done_button.pack_forget()
        done_button.master.pack_forget()
    
if __name__ == "__main__":
    todo = tdList()
    todo.mainloop()
