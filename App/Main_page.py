from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from Guis import MainPage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"Gui\build_1\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def shift_(window):
    mc = MainPage()
    mc.shift(window)

    
def Main_Page():
    window = Tk()
    root_image = relative_to_assets('heart.png')
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
        353.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command= lambda:shift_(window=window),
        relief="flat"
    )
    button_1.place(
        x=795.0,
        y=420.0,
        width=300.0,
        height=73.10924530029297
    )
    window.resizable(False, False)
    window.mainloop()