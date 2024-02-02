import functions
import pyperclip
from CTkMessagebox import CTkMessagebox
from pathlib import Path
import customtkinter
from tkinter import Tk, Canvas, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def generate(box):
    text = functions.create_password(int(length_options.get()), check_1.get(),
                                     check_2.get(), check_3.get(), check_4.get())
    if text == "None":
        box.configure(state="normal")
        box.delete(0.0, "end")
        box.configure(state="disabled")
        CTkMessagebox(
            title="Error", message="You have to check atleast one Option!", icon="cancel")
    else:
        box.configure(state="normal")
        box.delete(0.0, "end")
        box.insert(0.0, text)
        box.configure(state="disabled")


def copy(text):
    pyperclip.copy(text)
    CTkMessagebox(title="Copied", message="You have successfully copied the Password!",
                  icon="check", option_1="Thanks!")


window = Tk()

window.geometry("700x387")
window.configure(bg="#7C7C7C")
window.title("Password Generator")


canvas = Canvas(
    window,
    bg="#7C7C7C",
    height=387,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    50.0,
    77.0,
    anchor="nw",
    text="Include Symbols:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    333.0,
    77.0,
    anchor="nw",
    text="(e.g. @#$%)",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    333.0,
    119.0,
    anchor="nw",
    text="(e.g. 123456)",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    333.0,
    161.0,
    anchor="nw",
    text="(e.g. abcdefgh)",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    333.0,
    203.0,
    anchor="nw",
    text="(e.g. ABCDEFGH)",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    50.0,
    35.0,
    anchor="nw",
    text="Password length:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    50.0,
    119.0,
    anchor="nw",
    text="Include Numbers:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    50.0,
    161.0,
    anchor="nw",
    text="Include Lowercase Characters:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    50.0,
    203.0,
    anchor="nw",
    text="Include Uppercase Characters:",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    50.0,
    324.0,
    anchor="nw",
    text="Your new Password:",
    fill="#000000",
    font=("Inter", 15 * -1)
)
values = []
for i in range(8, 33):
    values.append(f"{i}")
length_options = customtkinter.CTkOptionMenu(
    window, values=values, height=20, width=200, corner_radius=6, fg_color="#D9D9D9", button_color="#D9D9D9",
    button_hover_color="#C2C2C2", dropdown_text_color="black", text_color="black")

length_options.place(
    x=305.0,
    y=39,
)


entry_1 = customtkinter.CTkTextbox(
    window,
    state="disabled",
    width=280.0,
    height=23.0,
    border_color="black",
    border_width=2,
    font=("Inter", 15 * -1)
)
entry_1.place(
    x=305.0,
    y=318.0,
)

check_1 = customtkinter.CTkCheckBox(
    window, text="", height=15, width=15, checkbox_height=20, checkbox_width=20)
check_1.place(
    x=304.0,
    y=77,
)
check_2 = customtkinter.CTkCheckBox(
    window, text="", height=15, width=15, checkbox_height=20, checkbox_width=20)
check_2.place(
    x=304.0,
    y=119,
)
check_3 = customtkinter.CTkCheckBox(
    window, text="", height=15, width=15, checkbox_height=20, checkbox_width=20)
check_3.place(
    x=304.0,
    y=161,
)
check_4 = customtkinter.CTkCheckBox(
    window, text="", height=15, width=15, checkbox_height=20, checkbox_width=20)
check_4.place(
    x=304.0,
    y=203,
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#7C7C7C",
    command=lambda: copy(entry_1.get(0.0, "end")),
    relief="flat"
)
button_1.place(
    x=600.0,
    y=319.00030517578125,
    width=75.0,
    height=35.0
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#7C7C7C",
    command=lambda: generate(entry_1),
    relief="flat"
)
button_2.place(
    x=305.0,
    y=251.0,
    width=219.0,
    height=39.0
)
window.resizable(False, False)
window.mainloop()
