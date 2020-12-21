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


language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values=language, width=22)
src_lang.place(x=20, y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=890, y=60)
dest_lang.set('choose output language')


# Define function

def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(1.0, END), src=src_lang.get(), dest=dest_lang.get())  # noqa

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)


# Translate Button
trans_btn = Button(root, text='Translate', font='arial 15 bold', pady=5, fg='white', command=Translate, bg='red', activebackground='orange red')  # noqa
trans_btn.place(x=478, y=180)


root.mainloop()
