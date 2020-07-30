#! /usr/bin/env python3

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#https://stackoverflow.com/questions/32188180/from-matplotlib-backends-import-tkagg-importerror-cannot-import-name-tkagg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk
import sys

root = tk.Tk()
l1 = ttk.Label(text='Graph Page!')
l1.pack(pady=10,padx=10)

button1 = ttk.Button(text="Back to Home",
                    command=lambda: controller.show_frame(StartPage))
button1.pack()

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])



canvas = FigureCanvasTkAgg(f)
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

#toolbar = NavigationToolbar2Tk(canvas)
#toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        
root.mainloop()