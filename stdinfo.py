from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkmacosx import Button
import menu

def stdinfopg():

    def dashpg():
        window.destroy()
        menu.dashboard()

    def on_scroll(*args):
        std_info.yview(*args)

    window = tk.Tk()
    window.title("STUDENTS INFO")
    window.resizable(0,0)
    window_width = 1250
    window_height = 280
    
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)


    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    frame=Frame(window)
    frame.pack(pady=10)

    # scroll bar
    ver_scroll_bar=ttk.Scrollbar(frame, orient=VERTICAL,command=on_scroll)
    ver_scroll_bar.pack(side=RIGHT,fill=Y)

    hor_scroll_bar=ttk.Scrollbar(frame, orient=HORIZONTAL)
    hor_scroll_bar.pack(side=BOTTOM,fill=X)
    
    # Treeview

    std_info=ttk.Treeview(frame,yscrollcommand=ver_scroll_bar.set,xscrollcommand=hor_scroll_bar.set)

    ver_scroll_bar.config(command=std_info.yview)

    hor_scroll_bar.config(command=std_info.xview)

    # defining columns
    std_info["columns"]=("S-ID","Date of Admission","First Name","Middle Name","Last Name","Ph No","Std Address","Building","Room No","Room Status","G First Name","G Middle Name","G Last Name","G Ph No","G Address")

    std_info.column("#0",width=0,minwidth=0)
    std_info.column("S-ID",anchor="w",width=50,minwidth=80)
    std_info.column("Date of Admission",anchor="w",width=120,minwidth=120)
    std_info.column("First Name",anchor="w",width=100,minwidth=130)
    std_info.column("Middle Name",anchor="w",width=100,minwidth=130)
    std_info.column("Last Name",anchor="w",width=100,minwidth=130)
    std_info.column("Ph No",anchor="w",width=105,minwidth=105)
    std_info.column("Std Address",anchor="w",width=140,minwidth=140)
    std_info.column("Building",anchor="w",width=60,minwidth=65)
    std_info.column("Room No",anchor="w",width=60,minwidth=65)
    std_info.column("Room Status",anchor="w",width=75,minwidth=75)
    std_info.column("G First Name",anchor="w",width=120,minwidth=120)
    std_info.column("G Middle Name",anchor="w",width=120,minwidth=120)
    std_info.column("G Last Name",anchor="w",width=120,minwidth=120)
    std_info.column("G Ph No",anchor="w",width=105,minwidth=105)
    std_info.column("G Address",anchor="w",width=160,minwidth=160)

    std_info.heading("#0",text="",anchor="w")
    std_info.heading("S-ID",text="S-ID",anchor="w")
    std_info.heading("Date of Admission",text="Date of Admission",anchor="w")
    std_info.heading("First Name",text="First Name",anchor="w")
    std_info.heading("Middle Name",text="Middle Name",anchor="w")
    std_info.heading("Last Name",text="Last Name",anchor="w")
    std_info.heading("Ph No",text="Ph No",anchor="w")
    std_info.heading("Std Address",text="Std Address",anchor="w")
    std_info.heading("Building",text="Building",anchor="w")
    std_info.heading("Room No",text="Room No",anchor="w")
    std_info.heading("Room Status",text="Room Status",anchor="w")
    std_info.heading("G First Name",text="G First Name",anchor="w")
    std_info.heading("G Middle Name",text="G Middle Name",anchor="w")
    std_info.heading("G Last Name",text="G Last Name",anchor="w")
    std_info.heading("G Ph No",text="G Ph No",anchor="w")
    std_info.heading("G Address",text="G Address",anchor="w")

    std_info.pack(padx=2)

    back_btn=Button(window,text="Back",bg="#DA00D6",font="verdana 15 bold",command=dashpg)
    back_btn.place(x=1120,y=240)

   
    window.mainloop()

if __name__=="__main__":
    stdinfopg()