from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from Guis import pulse,AidSync,synczen
from Backend_model import MainChatbot

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\HWAN\Gui\build_2\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def MC_P(window):
    p = pulse()
    p.shift(window=window)

def MC_AS(window):
    AS = AidSync()
    AS.shift(window=window)
    
def MC_SZ(window):
    sz = synczen()
    sz.shift(window=window)



def Main_chatbot():
    window = Tk()
    root_image = relative_to_assets('icon.png')
    icon = PhotoImage(file=root_image)
    window.iconphoto(True, icon)
    window.title('H.W.A.N : HealthWise Assistant & Navigator')

    window.geometry("1196x697")
    window.configure(bg = "#FFFFFF")


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
        749.5,
        302.5,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#000000",
        fg="#ffffff",
        highlightthickness=0,
        padx=5,
        font=('Ubuntu',20,'bold'),
        wrap=tk.WORD,
    )
    entry_1.place(
        x=374.0,
        y=73.0,
        width=751.0,
        height=457.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        706.0,
        643.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#000000",
        fg="#ffffff",
        highlightthickness=0,
        font=('Ubuntu',15,'bold'),
    )
    entry_2.place(
        x=375.0,
        y=624.0,
        width=662.0,
        height=37.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: MC_AS(window=window),
        relief="flat"
    )
    button_1.place(
        x=26.0,
        y=349.0,
        width=243.0,
        height=72.9000015258789
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: MC_SZ(window=window),
        relief="flat"
    )
    button_2.place(
        x=24.0,
        y=451.0,
        width=243.0,
        height=71.72246551513672
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: MainChatbot(entry_1,entry_2),
        relief="flat"
    )
    button_3.place(
        x=1092.0,
        y=615.0,
        width=65.0,
        height=61.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: MC_P(window=window),
        relief="flat"
    )
    button_4.place(
        x=26.0,
        y=250.0,
        width=243.0,
        height=69.0
    )
    window.resizable(False, False)
    window.mainloop()
Main_chatbot()