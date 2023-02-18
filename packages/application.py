from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("GraphicAppPythonTemplate")
        self.geometry("1500x850")
        self.buttons = {}
        self.texts = {}
        self.labels = {}

        self.create_button(text="Quit", name="quit_button", bg='red', fg='white', height=1, width=10, font=('Calibri', 20), command=self.quit)
        self.buttons['quit_button'].pack(side=BOTTOM)

        self.create_text(name="testing", text="Does this work ?")
        self.create_variablelabel(text_variable_name="testing", font=("Calibri", 20))
        self.labels['testing'].pack(side=TOP)

    def create_button(self, name, text, bg, fg, height, width, font, command):
        self.buttons[name] = Button(self, text=text, bg=bg, fg=fg, height=height, width=width, font=font, command=command)

    def create_text(self, name, text):
        self.texts[name] = StringVar()
        self.texts[name].set(text)

    def create_variablelabel(self, text_variable_name, font):
        self.labels[text_variable_name] = Label(self, textvariable=self.texts[text_variable_name], font=font)

    def create_canva(self):
        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        # place canvas
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    def create_animation(self, func, lines, columns, interval, blit):
        plt.style.use('fivethirtyeight')
        plt.gcf().subplots(lines, columns)

        FuncAnimation(plt.gcf(), func=func, interval=interval, blit=blit)