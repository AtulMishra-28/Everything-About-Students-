from tkinter import *
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # 1st Image
        img1 = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.f_lbl1 = Label(self.root, image=self.photoimg1)
        self.f_lbl1.place(x=0, y=0, width=500, height=130)

        # 2nd Image
        img2 = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.f_lbl2 = Label(self.root, image=self.photoimg2)
        self.f_lbl2.place(x=500, y=0, width=500, height=130)

        # 3rd Image
        img3 = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.f_lbl3 = Label(self.root, image=self.photoimg3)
        self.f_lbl3.place(x=1000, y=0, width=530, height=130)

        # Background Image
        img_bg = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        img_bg = img_bg.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        self.bg_lbl = Label(self.root, image=self.photoimg_bg)
        self.bg_lbl.place(x=0, y=130, width=1530, height=710)

        # Title Label
        title_lbl = Label(self.bg_lbl, text="Face Recognition Attendance System Software", 
                          font=("times new roman", 30, "bold"), bg="white", fg="red")  
        title_lbl.place(x=0, y=5, width=1530, height=50)  

        # Student Button
        img4 = Image.open(r"E:\Atul's Project\fm\stu.png")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.bg_lbl, image=self.photoimg4,command=self.students_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        # Student Details Button
        b1_1 = Button(self.bg_lbl, text="Student Details",command=self.students_details, cursor="hand2", font=("times new roman", 15, "bold"), 
                      bg="darkblue", fg="white")
        b1_1.place(x=200, y=320, width=220, height=40)  

        # Detect Face Button
        img5 = Image.open(r"E:\Atul's Project\fm\face.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(self.bg_lbl, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)

        # Detect Face Label Button
        b2_1 = Button(self.bg_lbl, text="Detect Face",command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), 
                      bg="darkblue", fg="white")
        b2_1.place(x=500, y=320, width=220, height=40)  

        # Attendance Face Button
        img6 = Image.open(r"E:\Atul's Project\fm\attendance.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(self.bg_lbl, image=self.photoimg6,command=self.attendance, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)  

        # Attendance Label Button
        b3_1 = Button(self.bg_lbl, text="Attendance", cursor="hand2",command=self.attendance, font=("times new roman", 15, "bold"), 
                      bg="darkblue", fg="white")
        b3_1.place(x=800, y=320, width=220, height=40)  

        # Help Desk Button
        img7 = Image.open(r"E:\Atul's Project\fm\help.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(self.bg_lbl, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)  

        # Help Desk Label Button
        b4_1 = Button(self.bg_lbl, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), 
                      bg="darkblue", fg="white")
        b4_1.place(x=1100, y=320, width=220, height=40)  

        # Train Face Button
        img8 = Image.open(r"E:\Atul's Project\fm\train.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(self.bg_lbl, image=self.photoimg8, cursor="hand2",command= self.train_data)
        b5.place(x=200, y=400, width=220, height=220)

        b5_1 = Button(self.bg_lbl, text="Train Face", cursor="hand2", font=("times new roman", 15, "bold"), 
                      bg="darkblue", fg="white",command= self.train_data)
        b5_1.place(x=200, y=600, width=220, height=40)  

        # Photos Button
        img9 = Image.open(r"E:\Atul's Project\fm\face.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(self.bg_lbl, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b6.place(x=500, y=400, width=220, height=220)

        b6_1 = Button(self.bg_lbl, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), 
                      bg="darkblue", fg="white")
        b6_1.place(x=500, y=600, width=220, height=40)  

        # Developer Button
        img10 = Image.open(r"E:\Atul's Project\fm\dev.png")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(self.bg_lbl, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=400, width=220, height=220)  

        b7_1 = Button(self.bg_lbl, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), 
                      bg="darkblue", fg="white")
        b7_1.place(x=800, y=600, width=220, height=40)  

        # Exit Button
        img11 = Image.open(r"E:\Atul's Project\fm\exit.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(self.bg_lbl, image=self.photoimg11, cursor="hand2")
        b8.place(x=1100, y=400, width=220, height=220)  

        b8_1 = Button(self.bg_lbl, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), 
                      bg="darkblue", fg="white")
        b8_1.place(x=1100, y=600, width=220, height=40) 

    #function buttons 
    def students_details(self):
        """Opens the student details window."""
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

     # 
    def open_img(self):
        os.startfile("data")

    def train_data(self):
        """Opens the train data window."""
        self.new_window = Toplevel(self.root)
        self.app =Train(self.new_window)

    def face_data(self):
        """Opens the face detect window."""
        self.new_window = Toplevel(self.root)
        self.app =FaceRecognition(self.new_window)

    def attendance(self):
        """Record the attendance """
        self.new_window=Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
