from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkmacosx import Button
import std_menu


def fees():
     
    def on_scroll(*args):
        date_amt_box.yview(*args)

    def stdmenupg():
        window.destroy()
        std_menu.std_menupg()

    window = tk.Tk()
    window.title("FEE RECORD")
    window.resizable(0,0)
    window_width = 500
    window_height = 260
    
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)


    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    frame=Frame(window)
    frame.pack(pady=5)

    # scroll bar
    ver_scroll_bar=ttk.Scrollbar(frame, orient=VERTICAL,command=on_scroll)
    ver_scroll_bar.pack(side=RIGHT,fill=Y)


    date_amt_box = ttk.Treeview(frame,yscrollcommand=ver_scroll_bar.set)
    ver_scroll_bar.config(command=date_amt_box.yview)

    # defining columns
    date_amt_box['columns'] = ("Date", "Amount")
    date_amt_box.column("#0", width=0, minwidth=0)  
    date_amt_box.column("Date", anchor=CENTER, width=250, minwidth=250)
    date_amt_box.column("Amount", anchor=CENTER, width=250, minwidth=250)
    
    date_amt_box.heading("#0", text="", anchor=CENTER)
    date_amt_box.heading("Date", text="Date", anchor=CENTER)
    date_amt_box.heading("Amount", text="Amount", anchor=CENTER)
    
    date_amt_box.pack(padx=2)

    back_btn = Button(window, text="Back", width=100, height=30, bg="#F33400", fg="black", font=("verdana 13 bold"),borderless=1,command=stdmenupg)
    back_btn.place(x=385,y=220)
 

    window.mainloop()

if __name__=="__main__":
    fees()




















