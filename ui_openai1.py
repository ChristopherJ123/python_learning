import tkinter as tk


class CircleUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_circle()

    def create_circle(self):
        x0, y0, x1, y1 = 50, 50, 150, 150  # Set the coordinates of a bounding box for the circle
        self.canvas = tk.Canvas(self, width=200, height=200)
        self.canvas.pack()
        self.canvas.create_oval(x0, y0, x1, y1, fill="blue")  # Create a circle within the bounding box


root = tk.Tk()
app = CircleUI(master=root)
app.mainloop()
