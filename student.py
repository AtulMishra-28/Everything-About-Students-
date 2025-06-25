from tkinter import *
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # 1st Image
        img1 = Image.open(r"E:\Atul's Project\ex.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.f_lbl1 = Label(self.root, image=self.photoimg1)
        self.f_lbl1.place(x=0, y=0, width=500, height=130)

        # 2nd Image
        img2 = Image.open(r"E:\Atul's Project\ex.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.f_lbl2 = Label(self.root, image=self.photoimg2)
        self.f_lbl2.place(x=500, y=0, width=500, height=130)

        # 3rd Image
        img3 = Image.open(r"E:\Atul's Project\ex.jpg")
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.f_lbl3 = Label(self.root, image=self.photoimg3)
        self.f_lbl3.place(x=1000, y=0, width=530, height=130)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
