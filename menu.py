import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageFilter, ImageTk
from tkmacosx import Button

# Function to blur the image and resize it
def blur_and_resize_image(image_path, blur_radius, size):
    image = Image.open(image_path)
    # Resize the image
    image = image.resize(size)
    # Apply Gaussian blur
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    return blurred_image

# Create a Tkinter window
window = tk.Tk()
window.title("MENU")
window.geometry("800x590")
window.resizable(0,0)


# Blur the image and set its size
background_image = blur_and_resize_image("hostelBuilding.jpg", blur_radius=3,size=(650,590))

# Convert the image to a Tkinter PhotoImage using ImageTk
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = ttk.Label(window, image=background_photo)
background_label.place(x=200, y=0, relwidth=1, relheight=1)

# menu frame
menu_frame=tk.Frame(window,bg="#00D4FF")
menu_frame.grid(row=0,column=0,sticky="w")

menu_label=tk.Label(menu_frame,text="DASHBOARD",fg="#D76500",bg="#00D4FF",font="verdana 20 bold underline")
menu_label.grid(row=0,column=0,sticky="w",padx=50,pady=5)

reg_std_btn=Button(menu_frame,width=200,height=40,text="Student Registration",bg="#00B203",font="verdana 15 bold",borderless=1)
reg_std_btn.grid(row=1,column=0,pady=5)

manage_std_btn=Button(menu_frame,width=200,height=40,text="Manage Student",bg="#00B203",font="verdana 15 bold",borderless=1)
manage_std_btn.grid(row=2,column=0,pady=5)

fees_btn=Button(menu_frame,width=200,height=40,text="Student Fees",bg="#00B203",font="verdana 15 bold",borderless=1)
fees_btn.grid(row=3,column=0,pady=5)

std_info_btn=Button(menu_frame,width=200,height=40,text="Student Info",bg="#00B203",font="verdana 15 bold",borderless=1)
std_info_btn.grid(row=4,column=0,pady=5)

reg_staff_btn=Button(menu_frame,width=200,height=40,text="Staff Registration",bg="#00B203",font="verdana 15 bold",borderless=1)
reg_staff_btn.grid(row=5,column=0,pady=5)

manage_staff_btn=Button(menu_frame,width=200,height=40,text="Manage Staff",bg="#00B203",font="verdana 15 bold",borderless=1)
manage_staff_btn.grid(row=6,column=0,pady=5)

staff_salary_btn=Button(menu_frame,width=200,height=40,text="Staff Salary",bg="#00B203",font="verdana 15 bold",borderless=1)
staff_salary_btn.grid(row=7,column=0,pady=5)

staff_info_btn=Button(menu_frame,width=200,height=40,text="Staff Info",bg="#00B203",font="verdana 15 bold",borderless=1)
staff_info_btn.grid(row=8,column=0,pady=5)

manage_room_btn=Button(menu_frame,width=200,height=40,text="Manage Room",bg="#00B203",font="verdana 15 bold",borderless=1)
manage_room_btn.grid(row=9,column=0,pady=5)

room_info_btn=Button(menu_frame,width=200,height=40,text="Room Info",bg="#00B203",font="verdana 15 bold",borderless=1)
room_info_btn.grid(row=10,column=0,pady=5)

food_menu_btn=Button(menu_frame,width=200,height=40,text="Food Menu",bg="#00B203",font="verdana 15 bold",borderless=1)
food_menu_btn.grid(row=11,column=0,pady=5)

logout_btn=Button(window,text="Logout",bg="red",font="verdana 15 bold",borderless=1)
logout_btn.place(x=685,y=555)

window.mainloop()
