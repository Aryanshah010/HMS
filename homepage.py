from tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkmacosx import Button
from PIL import Image, ImageFilter, ImageTk

def blur_and_resize_image(image_path, blur_radius, size):
    image = Image.open(image_path)
    # Resize the image
    image = image.resize(size)
    # Apply Gaussian blur
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    return blurred_image

window = tk.Tk()
window.title("HOMEPAGE")
window.geometry("600x483")
window.resizable(0,0)

background_image = blur_and_resize_image("hostelBuilding.jpg", blur_radius=4,size=(600,485))

# Convert the image to a Tkinter PhotoImage using ImageTk
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = ttk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)


def show_contact_menu():
    contact_menu.post(contact_label.winfo_rootx(), contact_label.winfo_rooty() + contact_label.winfo_height())

def show_about_menu():
    about_menu.post(about_label.winfo_rootx(), about_label.winfo_rooty() + about_label.winfo_height())

# Create a label
contact_label = ttk.Label(window,text="Contacts")
contact_label.grid(row=0, column=0,sticky="w",padx=5,pady=5)

# Create a custom menu
contact_menu = tk.Menu(window, tearoff=0)

# Add contact options to the menu
contact_menu.add_command(label="Phone: 9815905635")
contact_menu.add_command(label="Phone: 9815851973")
contact_menu.add_command(label="Phone: 9807633375")
contact_menu.add_command(label="Phone: 9811834250")

contact_menu.add_command(label="Email: 230282@softwarica.edu.np")
contact_menu.add_command(label="Email: 230546@softwarica.edu.np")
contact_menu.add_command(label="Email: 230549@softwarica.edu.np")
contact_menu.add_command(label="Email: 230511@softwarica.edu.np")

# Configure the label to show the contact menu when clicked
contact_label.bind("<Button-1>", lambda event: show_contact_menu())


about_label=ttk.Label(window,width=5,text="About")
about_label.grid(row=0,column=1,sticky="w",padx=5,pady=5)

about_menu=tk.Menu(window,tearoff=0)


about_menu.add_command(label="This is Hostel Management System created by Aryan,Aaditya,Archana and Raju.")
about_menu.add_command(label="In this app admin stores the record of students,staff and rooms.")
                      

# Bind the menu to the label
about_label.bind("<Button-1>", lambda event: show_about_menu())

for_admin_label=Label(window,width=20,bg="#00EA63",fg="black",text="FOR ADMIN",font=("verdana 13 bold"))
for_admin_label.place(x=20,y=390)

register_btn=Button(window,width=75,text="Register",bg="#E7E300",font=("verdana 14 bold"),borderless=1)
register_btn.place(x=20,y=425)

login_btn=Button(window,width=70,text="Login",bg="#D700DA",font=("verdana 14 bold"),borderless=1)
login_btn.place(x=135,y=425)

for_std_label=Label(window,width=12,bg="#00EA63",fg="black",text="FOR STUDENT",font=("verdana 13 bold"))
for_std_label.place(x=455,y=390)

login_btn=Button(window,width=70,text="Login",bg="#F3A200",font=("verdana 14 bold"),borderless=1)
login_btn.place(x=480,y=425)


window.mainloop()