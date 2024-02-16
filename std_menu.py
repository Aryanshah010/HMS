import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageFilter, ImageTk
from tkmacosx import Button
import homepage
import check_fee

def std_menupg(): 

    def homepg():
        window.destroy()
        homepage.main()

    def ck_fee():
        window.destroy()
        check_fee.fees()

    window = tk.Tk()
    window.title("MENU")
    window.resizable(0,0)
    window_width = 730
    window_height = 310
    
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)


    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Function to blur the image and resize it
    def blur_and_resize_image(image_path, blur_radius, size):
        image = Image.open(image_path)
        # Resize the image
        image = image.resize(size)
        # Apply Gaussian blur
        blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
        return blurred_image

    # Blur the image and set its size
    background_image = blur_and_resize_image("hostelBuilding.jpg", blur_radius=4,size=(580,590))

    # Convert the image to a Tkinter PhotoImage using ImageTk
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to display the background image
    background_label = ttk.Label(window, image=background_photo)
    background_label.place(x=198, y=0, relwidth=1, relheight=1)

    menu_frame=tk.Frame(window,bg="#00D4FF",width=115)
    menu_frame.grid(row=0,column=0,sticky="w")

    menu_label=tk.Label(menu_frame,text="DASHBOARD",fg="#D76500",bg="#00D4FF",font="verdana 20 bold underline")
    menu_label.grid(row=0,column=0,sticky="w",padx=14,pady=5)

    fees_btn=Button(menu_frame,width=200,height=70,text="Check Fees",bg="#00B203",font="verdana 15 bold",borderless=1,command=ck_fee)
    fees_btn.grid(row=1,column=0,pady=10)

    std_info_btn=Button(menu_frame,width=200,height=70,text="My Info",bg="#00B203",font="verdana 15 bold",borderless=1)
    std_info_btn.grid(row=2,column=0,pady=10)

    std_info_btn=Button(menu_frame,width=200,height=70,text="Food Menu",bg="#00B203",font="verdana 15 bold",borderless=1)
    std_info_btn.grid(row=3,column=0,pady=10)


    logout_btn=Button(window,text="Logout",bg="red",font="verdana 15 bold",borderless=1,command=homepg)
    logout_btn.place(x=610,y=270)


    window.mainloop()


if __name__=="__main__":
    std_menupg()