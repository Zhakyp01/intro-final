from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1080x500')
root.resizable(0, 0)
root.title("AIU TRANSLATOR")
root.config(bg='cadetblue')

# HEADING
Label(root, text="TRANSLATOR", font="aharoni 25 bold", fg='gold', bg='red', width='80').pack()  # noqa
Label(root, text="Ala Too International University", font='aharoni 30 bold', bg='gold', fg='red', width='45').pack(side='bottom')  # noqa


# INPUT AND OUTPUT TEXT WIDGET
Label(root, text="Enter Text", font='aharoni 20 bold', bg='cadetblue').place(x=200, y=60)  # noqa
Input_text = Text(root, font='calibri 13', height=11, wrap=WORD, padx=5, pady=5, width=47)  # noqa
Input_text.place(x=30, y=100)


Label(root, text="Translation", font='aharoni 20 bold', bg='cadetblue').place(x=720, y=60)  # noqa
Output_text = Text(root, font='calibri 13', height=11, wrap=WORD, padx=5, pady=5, width=47)  # noqa
Output_text.place(x=600, y=100)
