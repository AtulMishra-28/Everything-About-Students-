from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
import time
from datetime import datetime

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Detection")

        title_lbl = Label(self.root, text="Face Detection", 
                          font=("times new roman", 30, "bold"), bg="white", fg="green")  
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load Images with Error Handling
        self.photoimg_left = self.load_image(r"E:\Atul's Project\fm\ex.jpg", (650, 700))
        self.photoimg_right = self.load_image(r"E:\Atul's Project\fm\ex.jpg", (950, 700))

        f_lbl1 = Label(self.root, image=self.photoimg_left)
        f_lbl1.place(x=0, y=55, width=650, height=700)

        f_lbl2 = Label(self.root, image=self.photoimg_right)
        f_lbl2.place(x=650, y=55, width=950, height=700)

        # Recognize Button
        b1_1 = Button(f_lbl2, text="Face Recognition", cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="orange", fg="white",
                      command=self.face_recog)
        b1_1.place(x=365, y=620, width=200, height=40)

    def load_image(self, path, size):
        """Load an image with error handling."""
        try:
            img = Image.open(path).resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except FileNotFoundError:
            print(f"Error: Image not found at {path}. Using blank image.")
            img = Image.new('RGB', size, (255, 255, 255))  # White Image
            return ImageTk.PhotoImage(img)

    def mark_attendance(self, id, roll, name, dep):
        """Marks attendance if the student is recognized."""
        if id == "Unknown":
            return  # Do not mark attendance for unknown faces

        today = datetime.now().strftime("%d/%m/%Y")
        with open("student.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            for line in myDataList:
                entry = line.strip().split(",")
                if len(entry) > 0 and entry[0] == str(id) and entry[-2] == today:
                    return  # Attendance already recorded

            now = datetime.now().strftime("%H:%M:%S")
            f.writelines(f"\n{id},{roll},{name},{dep},{now},{today},Present")

    def face_recog(self):
        """Face recognition function."""
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="tiger", database="face_recognizer"
                )
                my_cursor = conn.cursor()
            except mysql.connector.Error as err:
                print(f"Database Connection Error: {err}")
                return

            for (x, y, w, h) in faces:
                face_region = gray_image[y:y + h, x:x + w]
                id, confidence_score = clf.predict(face_region)
                confidence = int(100 * (1 - confidence_score / 300))

                if confidence > 77:
                    my_cursor.execute(f"SELECT Student_id, Name, Roll, Dep FROM student WHERE Student_id={id}")
                    result = my_cursor.fetchone()
                    if result:
                        id, name, roll, dep = result
                    else:
                        id, name, roll, dep = "Unknown", "Unknown", "Unknown", "Unknown"
                    color = (0, 255, 0)  # Green for recognized faces
                else:
                    id, name, roll, dep = "Unknown", "Unknown", "Unknown", "Unknown"
                    color = (0, 0, 255)  # Red for unrecognized faces

                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                cv2.putText(img, f"Student Id: {id}", (x, y - 105), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(img, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(img, f"Dep: {dep}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

                self.mark_attendance(id, roll, name, dep)

            conn.close()

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.2, 5, clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        fps_start_time = time.time()
        frame_count = 0

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = recognize(img, clf, faceCascade)

            frame_count += 1
            elapsed_time = time.time() - fps_start_time
            if elapsed_time >= 1.0:
                fps = frame_count / elapsed_time
                fps_start_time = time.time()
                frame_count = 0
                cv2.putText(img, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()