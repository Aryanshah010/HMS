from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkmacosx import Button
import menu

def food():

    def adminMenu():
        window.destroy()
        menu.dashboard()

    
    window = tk.Tk()
    window.title("FOOD MENU")
    window.resizable(0,0)
    window_width = 630
    window_height = 650

    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    img = Image.open("foodMenu.jpg")
    img = img.resize((600, 600), Image.BICUBIC)  
    FoodMenu = ImageTk.PhotoImage(img)
    image = Label(image=FoodMenu, border=0)
    image.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)

    back_btn=Button(window,text="Back",bg="#DA00D6",font="verdana 15 bold",command=adminMenu)
    back_btn.place(x=10,y=615)



    window.mainloop()

if __name__=="__main__":
    food()