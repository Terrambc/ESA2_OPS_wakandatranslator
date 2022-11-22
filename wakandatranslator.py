from tkinter import *
import pyglet.font

# Zur Einbindung der customfont
pyglet.font.add_file('WakandaForever_Regular.ttf')
pyglet.font.load('Wakanda Forever')
print(pyglet.font.have_font('Wakanda Forever'))


# Funktion Clear
def clear():
    texteingabe.delete(1.0, END)
    textausgabe.delete(1.0, END)
    pass


# Text übersetzen in wakandanisch
def uebersetzen():
    textausgabe.delete(1.0, END)
    eingabe = texteingabe.get(1.0, END)
    textausgabe.insert(1.0, eingabe)
    pass


root = Tk()
root.title("Translator Wakanda")
root.config(bg="gray17")

# Create outer Frame widget
left_frame = Frame(root, width=300, height=600, bg="MediumPurple1")
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = Frame(root, width=600, height=600, bg="MediumPurple1")
right_frame.grid(row=0, column=1, padx=10, pady=5)

# create left inner Frame widget
# Titel
title_frame = LabelFrame(left_frame, width=250, height=50, bg="snow", relief="flat")
title_frame.grid(row=1, column=0, padx=5, pady=5)
Label(left_frame, text="Übersetzer Wakandanisch", font=("Helvetica", 14, "bold"), background="snow").grid(row=1,
                                                                                                          column=0)

# Wakanda Logo
logo = PhotoImage(file="wakanda.png")
logo_frame = LabelFrame(left_frame, width=250, height=100, bg="snow", relief="flat")
logo_frame.grid(row=2, column=0, padx=5, pady=5)
Label(left_frame, image=logo, background="snow").grid(row=2, column=0)

# Explanation with Aktion Buttons
explanation_frame = LabelFrame(left_frame, width=250, height=415, bg="snow", relief="flat")
explanation_frame.grid(row=3, column=0, padx=5, pady=5)
Label(left_frame, text="Hier könnt ihr euren Text in \nWakandisch übersetzen lassen.", font=("Helvetica", 12),
      background="snow", anchor="n").grid(row=3, column=0, pady=15, sticky='n')

# Buttons
button_frame = Frame(left_frame, background="snow")
button_frame.grid(row=3, column=0)

eingabeButton = Button(button_frame, text="Text übersetzen", command=uebersetzen, bg='goldenrod1', width=20)
eingabeButton.grid(row=3, column=0, pady=5)

clearButton = Button(button_frame, text="Eingabe löschen", command=clear, bg='purple3', width=20)
clearButton.grid(row=4, column=0, pady=5)

# Create right Frame Widgets
texteingabe = Text(right_frame, width=50, height=8, font=("Helvetica", 23))
texteingabe.grid(row=1, column=1, pady=5, padx=5)
texteingabe.insert(END, "Gebe hier deinen Text ein.")

textausgabe = Text(right_frame, width=50, height=15, font=('Wakanda Forever', 16), background="snow")
textausgabe.grid(row=2, column=1, pady=5, padx=5)

root.mainloop()
