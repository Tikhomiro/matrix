from tkinter import Frame, Tk, Canvas
import random as rd

class Matrix(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = Canvas(master, bg= 'black')
        self.canvas.place(relx=0,rely=0,relheight=1,relwidth=1)

        self.velocidad = [i for i in range(0,30,5)]
        self.pos = [i for i in range(-200, 200, 20)]
        self.letters = []
        self.green = 0
        self.chars = ['1', '5', '7', 's', 'u', 'k', 'a']

        self.draw()
        self.update()


    def draw(self):
        for x in range(0, 1920,20):
            y = rd.choice(self.pos)
            for j in range(0, 250, 30):
                self.obj = self.canvas.create_text(20+x, -200+y+j, text = rd.choice(self.chars), fill='green2')
                self.letters.append(self.obj)


    def update(self):
        for letter in self.letters:
            v = rd.choice(self.velocidad)
            self.green += 5
            color = "#{:02x}{:02x}{:02x}".format(0,self.green,0)
            self.canvas.itemconfig(letter, fill=color)
            self.canvas.move(letter,0,v)
            y = self.canvas.coords(self.obj)
            if self.green >= 250:
                self.green = 0

        if y[1] >= 800:
            self.draw()
            if y[1] >= 1200:
                self.letters.clear()
                self.canvas.delete('all')

        self.canvas.after(80,self.update)


if __name__ == "__main__":
    root = Tk()
    root.title("Matrix")
    root.attributes("-fullscreen", True)
    root.config(bg= 'black')
    app = Matrix(root)
    app.mainloop()