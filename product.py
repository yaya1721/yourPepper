#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:38:57 2020

@author: liuchunting
"""


from PIL import ImageTk
from tkinter import *
import PIL
import tkinter as tk
import os
import time
from datetime import datetime as dt

# Class for the congrats messgae

class Congrat(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x400') 
        self.root.title("You have finished your study")
        self.root.resizable(width=True,height=True)  
        self.textLabel=tk.Label(self.root,text="Congradualation!! You can take some rest now",font=10).pack() 
        
        
        im=PIL.Image.open("cat.jpg")
        img=ImageTk.PhotoImage(im)
        imLabel=tk.Label(self.root,image=img).pack() # show the image
        self.root.wm_attributes("-topmost", "true")
        self.root.mainloop()

#############################################
# main() start here

   
hosts_abs_path="/etc/hosts"
redirect="127.0.0.1"
# List the website we want to block
websites_list=["youtube.com","www.youtube.com","facebook.com","www.facebook.com","www.netflix.com","www.instagram.com"]

study_slot=input("I need to study from ").split()
start=study_slot[0].split(":")
end=study_slot[2].split(":")

start_hour=int(start[0])
start_min=int(start[1])
end_hour=int(end[0])
end_min=int(end[1])


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,start_hour,start_min) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end_hour,end_min):
            #print("Go back to study!!!")
        with open(hosts_abs_path,"r+") as file:
            content=file.read()
            for website in websites_list:
                if website not in content:
                    file.write(redirect+" "+website+"\n")
    
    else:
        with open(hosts_abs_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        Congrat() # Show congrat window and guit the program


        

    
    
    
    
    
    
    
    