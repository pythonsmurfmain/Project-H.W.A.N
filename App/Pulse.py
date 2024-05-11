from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from Guis import MainPage,AidSync,synczen
from Backend_model import Symptom_checker

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Gui\build_3\assets\frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def P_H(window):
    ph = MainPage()
    ph.shift(window=window)


def P_AS(window):
    a_s = AidSync()
    a_s.shift(window=window) 
    
def P_SZ(window):
    sz = synczen()
    sz.shift(window=window)

def Pulse():
    window = Tk()

    window.geometry("1196x697")
    window.configure(bg = "#FFFFFF")
    window.title('Pulse')


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 697,
        width = 1196,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        598.0,
        348.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        714.5,
        288.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#150202",
        fg="#ffffff",
        highlightthickness=0,
        font=('Ubuntu',20,'bold'),
        wrap=tk.WORD,
        
    )
    entry_1.place(
        x=292.0,
        y=54.0,
        width=845.0,
        height=466.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        668.0,
        621.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#130101",
        fg="#ffffff",
        highlightthickness=0,
        font=('Ubuntu',15, 'bold')
    )
    entry_2.place(
        x=275.0,
        y=601.0,
        width=786.0,
        height=39.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: P_H(window=window),
        relief="flat"
    )
    button_1.place(
        x=64.0,
        y=161.0,
        width=107.0,
        height=106.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: P_AS(window=window),
        relief="flat"
    )
    button_2.place(
        x=7.0,
        y=397.0,
        width=225.0,
        height=81.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Symptom_checker(entry_1,entry_2),
        relief="flat"
    )
    button_3.place(
        x=1097.0,
        y=576.0,
        width=72.0,
        height=79.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: P_SZ(window=window),
        relief="flat"
    )
    button_4.place(
        x=0.0,
        y=300.0,
        width=239.0,
        height=77.0
    )
    window.resizable(False, False)
    window.mainloop()
Pulse()