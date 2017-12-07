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
        
        self.title("TO DO APP")
        self.geometry("500x750")
              
        self.backGroundColor_lib = ["whitesmoke","gainsboro"]
        self.fontcolor_lib = ["black"]

        if not tasks:
            self.tasks = []
            task1 = tk.Label(self, text="TASKS FOR TODAY", bg="darkgrey", fg="black", pady=20, font=("Times",23))
            task1.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(task1)
        
        else:
            self.tasks = []
            for i in range(len(tasks)):
                if i == 0:
                    task1 = tk.Label(self, text="TASKS FOR TODAY", bg="darkgrey", fg="black", pady=20, font=("Times",23))
                    task1.pack(side=tk.TOP, fill=tk.X)
                    self.tasks.append(task1)
                else:    
                    self.add(tasks[i])
                                
            
             
        self.task_create = tk.Text(self, height=3, bg="white", fg="black")
        
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()
        
        self.bind('<Return>', self.add_task)

    
    def add(self,txt,event=None):
         new_task = tk.Label(self, text = txt, pady=20)
         done_button = ttk.Button(new_task, text = "done",command = lambda:self.removeTask(done_button))
        
         backGroundIdx = len(self.tasks)%len(self.backGroundColor_lib)
         fontIdx = len(self.tasks)%len(self.fontcolor_lib)
        
         backGroundColor = self.backGroundColor_lib[backGroundIdx]
         fontColor = self.fontcolor_lib[fontIdx]
        
         new_task.configure(bg=backGroundColor,fg=fontColor,font=("Times",20))
        
         new_task.pack(side=tk.TOP, fill=tk.X)
         done_button.pack(side=tk.RIGHT)
                    
         self.tasks.append(new_task)
         
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
        self.tasks.remove(done_button.master)

    def on_closing(self):
        writefile = open("data.txt","w")
        for item in self.tasks:
            print(item.cget("text"),file=writefile)
        writefile.close()
        self.destroy()
    


if __name__ == "__main__":
    #reading previously saved tasks
    try:
        readfile = open("data.txt","r")
    except FileNotFoundError:
        file = open("data.txt","w")
        file.close()
        readfile=open("data.txt","r")
        
    tasks_lst=[]
    for line in readfile:
        line=line.strip()
        tasks_lst.append(line)
        
    #create todoApp    
    todo = tdList(tasks_lst)
    todo.protocol("WM_DELETE_WINDOW", todo.on_closing)
    todo.mainloop()
    
