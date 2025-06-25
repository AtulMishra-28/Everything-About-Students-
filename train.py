from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Train Data")
        
        title_lbl = Label(self.root, text="Training Facial Dataset", 
                          font=("times new roman", 30, "bold"), bg="white", fg="red")  
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
        image_top = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        image_top = image_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(image_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        # Train Button
        b1_1 = Button(self.root, text="Train Dataset", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        # Bottom image
        image_bottom = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        image_bottom = image_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(image_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=350)

    # Train classifier for all images
    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "No dataset found in 'data' directory")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []

        for image_path in path:
            try:
                filename = os.path.split(image_path)[1]
                file_id = int(filename.split('.')[1])  # Extract ID from filename

                img = Image.open(image_path).convert('L')  # Convert to Grayscale
                img = img.resize((200, 200), Image.Resampling.LANCZOS)  # Resize for speed
                imageNp = np.array(img, 'uint8')

                faces.append(imageNp)
                ids.append(file_id)

                # cv2.imshow("Training", imageNp)  # Disable for faster processing
                cv2.waitKey(1)
            except Exception as e:
                print(f"Skipping {image_path}: {e}")

        if not faces:
            messagebox.showerror("Error", "No valid images found for training")
            return

        ids = np.array(ids)

        try:
            # Train the Classifier
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.setRadius(1)  # Optimized for speed
            clf.setGridX(8)
            clf.setGridY(8)

            clf.train(faces, ids)
            clf.write("classifier.xml")  # Save a single classifier
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training completed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {e}")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
