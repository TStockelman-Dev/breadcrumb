from tkinter import Tk, BOTH, Canvas

def main():
    pass


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Breadcrumb")
        canvas = Canvas(self.root, width=self.width, height=self.height)
        canvas.pack()
        is_running = False

    def redraw(self):
        pass


if __name__ == "__main__":
    main()