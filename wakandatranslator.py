import tkinter
from PIL import Image, ImageTk, ImageFont, ImageDraw

# Funktion Clear
def clear():
    texteingabe.delete(1.0, tkinter.END)


# Text übersetzen in wakandanisch
def uebersetzen():
    eingabe = texteingabe.get(1.0, tkinter.END)

    font = ImageFont.truetype(font='WakandaForever_Regular.ttf', size=50)
    image = Image.new(mode='RGB', size=(650, 300), color='#9370db')
    draw = ImageDraw.Draw(im=image)
    draw.text(xy=(100, 100), text=eingabe, font=font, fill='black', anchor='mm')
    image.show()

   # img = ImageTk.PhotoImage()
   # textausgabe = tkinter.Frame(right_frame, image=img, width=650, height=300, bg="MediumPurple1", relief="flat")
   # textausgabe.grid(row=2, column=1, pady=5, padx=5)


root = tkinter.Tk()
root.title("Translator Wakanda")
root.config(bg="gray17")

left_frame = tkinter.Frame(root, width=300, height=600, bg="MediumPurple1")
left_frame.grid(row=0, column=0, padx=10, pady=5)

title_frame = tkinter.Frame(left_frame, width=250, height=50, bg="snow", relief="flat")
title_frame.grid(row=1, column=0, padx=5, pady=5)
tkinter.Label(left_frame, text="Übersetzer Wakandanisch", font=("Helvetica", 14, "bold"), background="snow").grid(row=1,
                                                                                                                  column=0)
logo = tkinter.PhotoImage(file="wakanda.png")
logo_frame = tkinter.Frame(left_frame, width=250, height=100, bg="snow", relief="flat")
logo_frame.grid(row=2, column=0, padx=5, pady=5)
tkinter.Label(left_frame, image=logo, background="snow").grid(row=2, column=0)

explanation_frame = tkinter.Frame(left_frame, width=250, height=415, bg="snow", relief="flat")
explanation_frame.grid(row=3, column=0, padx=5, pady=5)
tkinter.Label(left_frame, text="Hier könnt ihr euren Text in \nWakandisch übersetzen lassen.", font=("Helvetica", 12),
              background="snow", anchor="n").grid(row=3, column=0, pady=15, sticky='n')

button_frame = tkinter.Frame(left_frame, background="snow")
button_frame.grid(row=3, column=0)

eingabeButton = tkinter.Button(button_frame, text="Text übersetzen", command=uebersetzen, bg='goldenrod1', width=20)
eingabeButton.grid(row=3, column=0, pady=5)

clearButton = tkinter.Button(button_frame, text="Eingabe löschen", command=clear, bg='purple3', width=20)
clearButton.grid(row=4, column=0, pady=5)


right_frame = tkinter.Frame(root, width=600, height=600, bg="MediumPurple1")
right_frame.grid(row=0, column=1, padx=10, pady=5)

texteingabe = tkinter.Text(right_frame, width=50, height=8, font=("Helvetica", 18))
texteingabe.grid(row=1, column=1, pady=5, padx=5)

# textausgabe = tkinter.Frame(right_frame, width=650, height=300, bg="MediumPurple1", relief="flat")
# textausgabe.grid(row=2, column=1, pady=5, padx=5)


root.mainloop()
