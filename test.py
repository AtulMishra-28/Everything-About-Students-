from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk  # Import ttk for Combobox
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # 1st Header Image
        img1 = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.f_lbl1 = Label(self.root, image=self.photoimg1)
        self.f_lbl1.place(x=0, y=0, width=500, height=130)

        # 2nd Header Image
        img2 = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.f_lbl2 = Label(self.root, image=self.photoimg2)
        self.f_lbl2.place(x=500, y=0, width=500, height=130)

        # 3rd Header Image
        img3 = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.f_lbl3 = Label(self.root, image=self.photoimg3)
        self.f_lbl3.place(x=1000, y=0, width=530, height=130)

        # Background Image (Loaded Separately)
        img_bg = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        img_bg = img_bg.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)

        self.bg_lbl = Label(self.root, image=self.photoimg_bg)
        self.bg_lbl.place(x=0, y=130, width=1530, height=710)

        # Title Label
        title_lbl = Label(self.bg_lbl, text="Student Management System",
                          font=("times new roman", 30, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=5, width=1530, height=45)

        # Main Frame
        main_frame = Frame(self.bg_lbl, bg="white", bd=2, relief=RIDGE)
        main_frame.place(x=10, y=55, width=1500, height=650)

        # Left Label Frame (Student Details)
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=720, height=630)

        # Left Frame Image
        image_left = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        image_left = image_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(image_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=710, height=130)

        # Current Course Information Frame (Inside Student Details)
        course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Current Course Information", font=("times new roman", 12, "bold"))
        course_frame.place(x=10, y=140, width=700, height=110)  # Adjusted to fit inside left_frame

        # Department
        dep_lbl = Label(course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_lbl.grid(row=0, column=0, pady=10, padx=10, sticky=W)

        dep_combo = ttk.Combobox(course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"), width=20, state="readonly")
        dep_combo["values"] = ("Select Department", "Bsc.IT", "Bsc.Cs", "B.Com", "BAF", "BAMMC", "BSC")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # Course
        course_lbl = Label(course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")  # Corrected label text
        course_lbl.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(course_frame, textvariable=self.var_course, font=("times new roman", 13, "bold"), width=20, state="readonly")  # Fixed missing ttk reference
        course_combo["values"] = ("Select Course", "IT", "CS", "Mechanical", "Civil")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_lbl = Label(course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_lbl.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(course_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), width=20, state="readonly")  # Fixed missing ttk reference
        year_combo["values"] = ("Select Year", "FY", "SY", "TY")  # Corrected "Select Course" to "Select Year"
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        sem_lbl = Label(course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        sem_lbl.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(course_frame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), width=20, state="readonly")  # Fixed missing ttk reference
        sem_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6")  # Corrected "Select Course" to "Select Semester"
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)  # Fixed `year_comb` typo

        # class student information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=10, y=255, width=700, height=350)

        # Student ID
        studentId_lbl = Label(class_student_frame, text="Student ID: ", font=("times new roman", 13, "bold"), bg="white")
        studentId_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_lbl = Label(class_student_frame, text="Student Name: ", font=("times new roman", 13, "bold"), bg="white")
        studentName_lbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_lbl = Label(class_student_frame, text="Class Division : ", font=("times new roman", 13, "bold"), bg="white")
        class_div_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20, font=("times new roman", 12, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll no
        rollno_lbl = Label(class_student_frame, text="Roll no: ", font=("times new roman", 13, "bold"), bg="white")
        rollno_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        rollno_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        rollno_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_lbl = Label(class_student_frame, text="Gender: ", font=("times new roman", 13, "bold"), bg="white")
        gender_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"), width=16, state="readonly")  # Fixed missing ttk reference
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=9, pady=10, sticky=W)

        # DOB
        dob_lbl = Label(class_student_frame, text="DOB: ", font=("times new roman", 13, "bold"), bg="white")
        dob_lbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_lbl = Label(class_student_frame, text="Email : ", font=("times new roman", 13, "bold"), bg="white")
        email_lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone no
        phone_lbl = Label(class_student_frame, text="Phone : ", font=("times new roman", 13, "bold"), bg="white")
        phone_lbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_lbl = Label(class_student_frame, text="Address : ", font=("times new roman", 13, "bold"), bg="white")
        address_lbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher's Name
        teacher_name_lbl = Label(class_student_frame, text="Teacher's Name : ", font=("times new roman", 13, "bold"), bg="white")
        teacher_name_lbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take photo sample", value="yes")
        radiobtn1.grid(row=6, column=0, padx=10, pady=5, sticky=W)

        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No photo sample", value="no")
        radiobtn2.grid(row=6, column=1, padx=10, pady=5, sticky=W)

        # Button Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=220, width=680, height=55)  # Adjusted position and size

        # Save Button
        save_btn = Button(btn_frame, command=self.add_data, text="Save", font=("times new roman", 12, "bold"),
                          width=17, bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=5, pady=5)

        # Update Button
        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"),
                            width=17, bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=5, pady=5)

        # Delete Button
        delete_btn = Button(btn_frame, text="Delete", font=("times new roman", 12, "bold"),
                            width=17, bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=5, pady=5)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", font=("times new roman", 12, "bold"),
                           width=17, bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=5, pady=5)

        # Second button frame
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=10, y=280, width=620, height=45)  # Adjusted y position

        # Take Photo Button
        take_photo_btn = Button(btn_frame1, text="Take Photo", font=("times new roman", 12, "bold"),
                                width=32, bg="blue", fg="white")  # Increased width to fit properly
        take_photo_btn.grid(row=0, column=0, padx=5, pady=5)

        # Update Photo Button
        update_photo_btn = Button(btn_frame1, text="Update Photo", font=("times new roman", 12, "bold"),
                                  width=32, bg="blue", fg="white")  # Increased width for balance
        update_photo_btn.grid(row=0, column=1, padx=5, pady=5)

        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Other Student Info", font=("times new roman", 12, "bold"))
        right_frame.place(x=740, y=10, width=730, height=630)  # Adjusted spacing

        image_right = Image.open(r"E:\Atul's Project\fm\ex.jpg")
        image_right = image_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(image_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=710, height=130)

        # search student
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search Student", font=("times new roman", 12, "bold"))
        search_frame.place(x=10, y=140, width=700, height=70)

        search_lbl = Label(search_frame, text="Search by: ", font=("times new roman", 15, "bold"), bg="white")
        search_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), width=20, state="readonly")
        search_combo["values"] = ("Select", "Roll no ", "Phone no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", font=("times new roman", 12, "bold"),
                            width=10, bg="blue", fg="white")  # Increased width to fit properly
        search_btn.grid(row=0, column=2, padx=5, pady=5)

        show_all = Button(search_frame, text="Take Photo", font=("times new roman", 12, "bold"),
                          width=10, bg="blue", fg="white")  # Increased width to fit properly
        show_all.grid(row=0, column=3, padx=5, pady=5)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=215, width=700, height=300)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Define columns for the Treeview
        self.student_table = ttk.Treeview(table_frame, columns=("department", "course", "year", "sem", "id", "name", "div", "roll no", "gender"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Set headings for each column
        self.student_table.heading("department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll no", text="Roll no")
        self.student_table.heading("gender", text="Gender")

        # Set column widths
        self.student_table.column("department", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll no", width=100)
        self.student_table.column("gender", width=100)

        # Scrollbar configuration
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Pack the Treeview
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Functions
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error ", "All Fields are required ", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="tiger", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "Student details has been added. successfully ", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # Fetch Data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="tiger", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    # Get Cursor
    def get_cursor(self, event):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # Update Function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error ", "All Fields are required ", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want update the students details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="tiger", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student info Updated Successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()