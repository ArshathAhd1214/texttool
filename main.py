from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox, filedialog
import tkinter as tk
import sys
import os
from deep_translator import GoogleTranslator

import datetime
from gtts import gTTS
from playsound import playsound
import threading

# Initialize the Tkinter root window
def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
    
root = Tk()
root.title("Text Tool")
root.geometry("1030x570+290+140")
root.resizable(False, False)
root.config(bg="white")


# Set window icon
try:
    image_icon = PhotoImage(file="Images/icon.png")
    root.iconphoto(False, image_icon)
except Exception as e:
    print(f"Error loading icon: {e}")

# Header Frame
TOP_frame = Frame(root, bg="darkblue", width=1100, height=130)
TOP_frame.place(x=0, y=0)

# Logo
try:
    logo_icon = PhotoImage(file="Images/icon.png")
    Label(TOP_frame, image=logo_icon, bg="darkblue").place(x=40, y=20)
except Exception as e:
    print(f"Error loading logo: {e}")

Label(TOP_frame, text="Text Tool", font="Arial 20 bold", bg="darkblue", fg="white").place(x=190, y=20)

# Google Translate supported languages
languages = GoogleTranslator().get_supported_languages()

# Capitalize first letter for better display
languagesV = [lang.capitalize() for lang in languages]

# First language selection dropdown
combo1 = ttk.Combobox(root, values=languagesV, font=("Roboto", 10), state="readonly", width=15)
combo1.place(x=200, y=100)
combo1.set("English")  # Set default language

# Second language selection dropdown
combo2 = ttk.Combobox(root, values=languagesV, font=("Roboto", 10), state="readonly", width=15)
combo2.place(x=350, y=100)
combo2.set("Tamil")  # Set default language

# First text area
text_area = Text(root, font=("Roboto", 20), bg="#cbe7c2", relief=GROOVE, wrap=WORD)
text_area.place(x=40, y=140, width=600, height=200)

# Second text area
text_area2 = Text(root, font=("Roboto", 20), bg="#cbe7c2", relief=GROOVE, wrap=WORD)
text_area2.place(x=40, y=360, width=600, height=200)




Label(root, text="Voice", font="Arial 15 bold", fg="black", bg=root["bg"]).place(x=700, y=200)
Label(root, text="Speed", font="Arial 15 bold", fg="black", bg=root["bg"]).place(x=700, y=250)

# Gender Selection Combobox
gender_options = ["Male", "Female"]
gender_combobox = ttk.Combobox(root, values=gender_options, font=("Arial", 12), state="readonly", width=10)
gender_combobox.place(x=800, y=200)
gender_combobox.set("Male")  # Default selection

current_value = DoubleVar()
current_value.set(30)  # Set default value of the slider

# Function to get the current slider value
def get_current_value():
    return '{:.2f}'.format(current_value.get())

# Function to update the label when slider value changes
def slide_changed(event):
    value_label1.configure(text=get_current_value())

# Create a ttk.Style instance and configure the slider's appearance
style = ttk.Style()
style.configure("TScale",
                troughcolor=root.cget("bg"),  # Make the trough color match the window background
                sliderlength=20,  # Adjust the size of the slider knob
                background=root.cget("bg"),  # Remove the background color
                )

# Create the slider without background fill (transparent appearance)
slider = ttk.Scale(root, from_=30, to=250, orient="horizontal", command=slide_changed, variable=current_value, style="TScale")
slider.place(x=905, y=255)

# Create the label to display the slider value (without background fill, matches window background)
value_label1 = ttk.Label(root, text=get_current_value(), background=root.cget("bg"))  # Uses root's background color
value_label1.place(x=800, y=250)

bodybg = "lightgray"
framebg = "lightblue"

image_icon = PhotoImage(file="Images/speak.png")
btn = Button(root, compound=LEFT, image=image_icon, width=130, bg=bodybg, bd=0)
btn.place(x=700, y=380)

image_icon2 = PhotoImage(file="Images/download.png")
save = Button(root, compound=LEFT, image=image_icon2, width=130, bg=bodybg, bd=0)
save.place(x=850, y=380)

pdfupload = PhotoImage(file="Images/pdfimage.png")
upload_button = Button(root, image=pdfupload, bg=framebg, bd=0)
upload_button.place(x=950, y=57)  # Slightly pushed to the left

# Left side for audio upload button (slightly pushed to the left)
upload_audioimage = PhotoImage(file="Images/music.png")
upload_audio_button = Button(root, image=upload_audioimage, bg=framebg, bd=0)
upload_audio_button.place(x=880, y=57)  # Slightly pushed to the left

# Left side for translate button (slightly pushed to the left)
transimage = PhotoImage(file="Images/trans.png")
trans_button = Button(root, image=transimage, bg=framebg, bd=0)
trans_button.place(x=800, y=60)  # Slightly pushed to the left


micimage = PhotoImage(file="Images/mic.png")
mic_button = Button(root, image=micimage, bg=framebg, bd=0)
mic_button.place(x=50, y=305)

speakimage = PhotoImage(file="Images/otherspeaker.png")
speak_button = Button(root, image=speakimage, bg=framebg, bd=0)
speak_button.place(x=50, y=525)  

#pdf and text
# Assuming you have these dimensions for the window (root)
# Assuming you have these dimensions for the window (root)
window_width = 700  # Example width of the window
button_width = 80    # Smaller width for the button (adjust as needed)

# Calculate the X coordinate to place the button on the right
right_x = window_width - button_width - 100  # Adjusted to position the mode button further left

button_mode = True
choice = "Text"

def changemode():
    global button_mode
    global choice
    if button_mode:
        choice = "PDF"
        mode.config(image=pdfmode, activebackground="white")
        button_mode = False
    else:
        choice = "Text"
        mode.config(image=textmode, activebackground="white")
        button_mode = True

# Image for Text and PDF modes
textmode = PhotoImage(file="Images/modeText.png")
pdfmode = PhotoImage(file="Images/modePdf.png")  # Make sure you have an image for PDF mode

# Mode button (Small size, positioned on the right)
mode = Button(root, image=textmode, bg=framebg, bd=0, command=changemode)
mode.place(x=right_x, y=40)



root.mainloop()
