#!/usr/bin/env python2.7
import ttk
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image, ImageTk
import Core


def askToQuit():
    if tkMessageBox.askyesno("Confirm!", "Do you really want to quit such an awesome program? "):
        sys.exit()

class MainWindow:
    def __init__(self, hello):
        try:
            hello.title('CSS Minifier v1.0')
            hello.protocol('WM_DELETE_WINDOW', askToQuit)
            self.bg_image = ImageTk.PhotoImage(Image.open("src/bg.png"))

            w = self.bg_image.width()
            h = self.bg_image.height()
            hello.geometry("%dx%d" % (w, h))
            hello.resizable(width=False, height=False)
            #hello.wm_attributes("-transparentcolor", "white")

            self.bglabel = Label(hello, image=self.bg_image)
            self.bglabel.pack(side='top', fill='both', expand='yes')
            self.bglabel.image = self.bg_image

            self.PathNameFrame = Frame(self.bglabel)
            self.PathNameFrame.pack(fill=None, expand=True, pady=10, padx=10)

            self.MFrame = Frame(self.bglabel)
            self.MFrame.pack(fill=X, expand=True, pady=10, padx=10)

            self.BottomFrame = Frame(self.bglabel)
            self.BottomFrame.pack(fill=X, expand=True, side=BOTTOM)

            self.label1 = Label(self.PathNameFrame, text="Enter File Path :", anchor=CENTER)
            self.label1.pack(side=TOP, fill=None)

            self.entry1 = Text(self.PathNameFrame, height=1, width=60)
            self.entry1.pack(side=TOP)

            self.bbutton = ttk.Button(self.PathNameFrame, text="Browse")
            self.bbutton.pack(side=BOTTOM, fill=None, padx=5)
            self.bbutton.bind("<Button-1>", lambda event: self.getFileName(hello))

            helloButton1 = ttk.Button(self.MFrame, text="Minify")
            helloButton1.pack(side=BOTTOM, padx=10, pady=10, anchor=CENTER, fill=None, expand=True)
            helloButton1.bind("<Button-1>", lambda event: self.minify())

            self.status = Label(self.BottomFrame, text="Ready.", bd=1, relief=SUNKEN, anchor=CENTER, bg='light green')
            self.status.pack(side=BOTTOM, fill=X)

        except:
            return

    def getFileName(self,root):
        root.iconify()
        self.entry1.delete(0.0, END)
        fileName = askopenfilename(initialdir='/', title='Choose CSS file to minify')
        print fileName
        self.entry1.insert(0.0, fileName)
        self.status.configure(text="Ready.", bg='light green')
        root.deiconify()


    def minify(self):
        filename = StringVar()
        filename=self.entry1.get(0.0, END)
        filename = filename.strip("\n")
        with open(filename, 'r') as source:
            lines = source.readlines()

        lines = Core.replace_tabs(lines)
        lines = Core.remove_trailing_white_spaces(lines)
        lines = Core.remove_blank_lines(lines)
        lines = Core.remove_comments(lines)
        lines = Core.remove_blank_lines(lines)
        lines = Core.optimize_lines(lines)
        lines = Core.condense_lines(lines)

        destination = filename.replace(".css", "_min.css")
        dest = open(destination, "w")
        dest.writelines(lines)

        self.status.configure(text="File Minified!", bg='light green')



def main():
    hello = Tk()
    RootWindow = MainWindow(hello)
    hello.mainloop()
    #filename = ""
    #filename = raw_input("Enter the file to minify : ")
    #minify(filename)

if __name__ == "__main__":
    main()
