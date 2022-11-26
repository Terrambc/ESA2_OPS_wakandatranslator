import tkinter as tk
from functools import partial
from PIL import Image, ImageFont, ImageDraw


def clear(textinput, textoutput):
    """
    Clear the input and output
    :param textinput:
    :param textoutput:
    :return:
    """
    textinput.delete(1.0, tk.END)
    textoutput.delete(1.0, tk.END)


def translate(textinput, textoutput):
    """
    translate the textinput message to wakandanisch and
    put call a new function to insert the translated message as an image into the textoutput
    :param textinput:
    :param textoutput:
    :return:
    """
    textoutput.delete(1.0, tk.END)
    message = textinput.get(1.0, tk.END)
    # get_picture(message)

    txt = Image.new(mode='RGB', size=(600, 400), color='#9370db')
    font = ImageFont.truetype(font='WakandaForever_Regular.ttf', size=20)
    draw = ImageDraw.Draw(txt)
    draw.text(xy=(10, 10), text=message, font=font, fill='black')
    txt.save('message.png')
    del draw

    add_image(textoutput)


def add_image(textoutput):
    """
    insert the translated message as an image to textoutput
    :param textoutput:
    :return:
    """
    global my_image
    my_image = tk.PhotoImage(file='message.png')
    textoutput.image_create(tk.END, image=my_image)


def main():
    root = tk.Tk()
    root.title('Translator')
    root.config(bg="gray17")

    # left side
    outer_canvas = tk.Frame(root, width=370, height=570, bg='MediumPurple1')
    outer_canvas.grid(row=0, column=0, sticky=tk.E)
    outer_canvas.grid_propagate(False)
    frame = tk.Frame(outer_canvas, bg='snow', width=350, height=560)
    frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
    frame.grid_propagate(False)

    tk.Label(
        frame,
        text='Translator Wakandanisch',
        font=('Helvetica', 14, 'bold'),
        background='snow'
    ).grid(row=1, column=0, padx=10, pady=5)

    logo_image = tk.PhotoImage(file='wakanda.png')
    tk.Label(frame, image=logo_image, background='snow').grid(
        row=2, column=0, pady=5, padx=5
    )

    tk.Label(
        frame,
        text="Let you message be translated into wakandisch.",
        font=('Helvetica', 12),
        background='snow'
    ).grid(row=3, column=0, pady=15, padx=5, sticky=tk.NSEW)

    button_frame = tk.Frame(frame, background='snow', height=350)
    button_frame.grid(row=4, column=0, padx=5, pady=5, sticky=tk.NSEW)

    translate_button = tk.Button(
        button_frame, text="Translate message", bg='goldenrod1'
    )
    translate_button.grid(row=0, column=0, pady=5, padx=5, sticky=tk.NSEW)

    clear_button = tk.Button(
        button_frame, text="Delete message", bg='purple3'
    )
    clear_button.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NSEW)

    # right side
    frame = tk.Frame(root, bg='MediumPurple1')
    frame.grid(row=0, column=2, pady=5, padx=10)

    textinput = tk.Text(
        frame,
        width=50,
        height=8,
        font=('Helvetica', 16),
        bg='snow'
    )
    textinput.grid(row=0, column=0, padx=5, pady=5)
    textinput.insert(tk.END, "Insert your message here")

    textoutput = tk.Text(
        frame,
        width=75,
        height=22,
        bg='MediumPurple1'
    )
    textoutput.grid(row=2, column=0, padx=5, pady=5)

    translate_button["command"] = partial(translate, textinput, textoutput)
    clear_button["command"] = partial(clear, textinput, textoutput)

    root.mainloop()


if __name__ == '__main__':
    main()
