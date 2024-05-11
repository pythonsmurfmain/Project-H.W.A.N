from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from Guis import MainPage,pulse,synczen
from Backend_model import AidSync
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\HWAN\Gui\build_4\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def as_h(window):
    h = MainPage
    h.shift(window=window)

def as_p(window):
    p = pulse()
    p.shift(window=window)

def as_sz(window):
    sz = synczen()
    sz.shift(window=window)

def Aid_sync():
    window = Tk()

    window.geometry("1196x694")
    window.configure(bg = "#FFFFFF")
    window.title('AidSync')


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 694,
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
        351.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        722.5,
        272.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#0C0000",
        fg="#ffffff",
        highlightthickness=0,
        wrap=tk.WORD,
        font=('Ubuntu',20,'bold')
    )
    entry_1.place(
        x=297.0,
        y=48.0,
        width=851.0,
        height=446.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: AidSync(entry_1,entry_2),
        relief="flat"
    )
    button_1.place(
        x=1109.0,
        y=564.0,
        width=76.0,
        height=82.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: as_h(window=window),
        relief="flat"
    )
    button_2.place(
        x=50.0,
        y=153.0,
        width=154.0,
        height=159.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: as_sz(window=window),
        relief="flat"
    )
    button_3.place(
        x=26.0,
        y=336.0,
        width=204.0,
        height=70.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: as_p(window=window),
        relief="flat"
    )
    button_4.place(
        x=26.0,
        y=447.0,
        width=204.0,
        height=70.125
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        678.5,
        613.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#0C0000",
        fg="#ffffff",
        highlightthickness=0,
        font=('Ubuntu',20,'bold')
    )
    entry_2.place(
        x=297.0,
        y=593.0,
        width=763.0,
        height=39.0
    )
    window.resizable(False, False)
    window.mainloop()
Aid_sync()