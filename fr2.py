from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Detection")
        
        title_lbl = Label(self.root, text="Face Detection ", 
                          font=("times new roman", 30, "bold"), bg="white", fg="green")  
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Left Image
        image_left = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        image_left = image_left.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(image_left)

        f_lbl1 = Label(self.root, image=self.photoimg_left)
        f_lbl1.place(x=0, y=55, width=650, height=700)

        # Right Image 
        image_right = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        image_right = image_right.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(image_right)

        f_lbl2 = Label(self.root, image=self.photoimg_right)
        f_lbl2.place(x=650, y=55, width=950, height=700)

        # Recognize Button
        b1_1 = Button(f_lbl2, text="Face Recognition", cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="orange", fg="white",
                      command=self.face_recog)
        b1_1.place(x=365, y=620, width=200, height=40)

    #============ Face Recognition Function ===============
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="tiger", database="face_recognizer"
                )
                my_cursor = conn.cursor()

                my_cursor.execute(f"SELECT Name FROM student WHERE Student_id={id}")
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute(f"SELECT Roll FROM student WHERE Student_id={id}")
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute(f"SELECT Dep FROM student WHERE Student_id={id}")
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
