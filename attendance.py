from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, filedialog
import os
import csv

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Attendance Management System")

        # Variables 
        self.var_attend_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_status = StringVar()
        
        self.mydata = []

        # Header Image
        img = Image.open(r"E:\Atul's Project\fm\attendance.jpg").resize((1530, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=1530, height=200)

        # Title Label
        Label(self.root, text="Attendance Management System", font=("times new roman", 30, "bold"), bg="white", fg="red").place(x=0, y=200, width=1530, height=45)
        
        # Main Frame
        main_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        main_frame.place(x=10, y=250, width=1500, height=600)

        # Left Frame
        left_frame = LabelFrame(main_frame, text="Attendance Details", font=("times new roman", 12, "bold"), bg="white", bd=2, relief=RIDGE)
        left_frame.place(x=10, y=10, width=720, height=580)

        # Input Fields
        labels = [
            ("Attendance ID:", self.var_attend_id),
            ("Roll No:", self.var_attend_roll),
            ("Student Name:", self.var_attend_name),
            ("Department:", self.var_attend_dep),
            ("Time:", self.var_attend_time),
            ("Date:", self.var_attend_date),
            ("Attendance Status:", self.var_attend_status)
        ]
        
        for i, (label, var) in enumerate(labels):
            Label(left_frame, text=label, font=("times new roman", 13, "bold"), bg="white").grid(row=i, column=0, padx=10, pady=5, sticky=W)
            if label == "Attendance Status:":
                self.attendance_status = ttk.Combobox(left_frame, font=("times new roman", 13, "bold"), width=16, state="readonly", textvariable=self.var_attend_status)
                self.attendance_status["values"] = ("Status", "Present", "Absent")
                self.attendance_status.current(0)
                self.attendance_status.grid(row=i, column=1, padx=10, pady=5, sticky=W)
            else:
                ttk.Entry(left_frame, width=20, font=("times new roman", 12, "bold"), textvariable=var).grid(row=i, column=1, padx=10, pady=5, sticky=W)

        # Buttons
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=300, width=700, height=50)

        Button(btn_frame, text="Import CSV", command=self.importCsv, font=("times new roman", 12, "bold"), width=17, bg="blue", fg="white").grid(row=0, column=0, padx=5, pady=5)
        Button(btn_frame, text="Export CSV", command=self.exportCsv, font=("times new roman", 12, "bold"), width=17, bg="blue", fg="white").grid(row=0, column=1, padx=5, pady=5)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"), width=17, bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=5, pady=5)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"), width=17, bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=5, pady=5)

        # Right Frame (Table)
        right_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
        right_frame.place(x=750, y=10, width=720, height=580)

        # Scrollbars and Table
        scroll_x = Scrollbar(right_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(right_frame, orient=VERTICAL)
        self.Attendance_table = ttk.Treeview(right_frame, columns=("ID", "Roll", "Name", "Dep", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Attendance_table.xview)
        scroll_y.config(command=self.Attendance_table.yview)

        self.Attendance_table.heading("ID", text="Attendance ID")
        self.Attendance_table.heading("Roll", text="Roll No")
        self.Attendance_table.heading("Name", text="Student Name")
        self.Attendance_table.heading("Dep", text="Department")
        self.Attendance_table.heading("Time", text="Time")
        self.Attendance_table.heading("Date", text="Date")
        self.Attendance_table.heading("Attendance", text="Status")
        self.Attendance_table["show"] = "headings"
        self.Attendance_table.pack(fill=BOTH, expand=1)
        self.Attendance_table.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self):
        self.Attendance_table.delete(*self.Attendance_table.get_children())
        for row in self.mydata:
            self.Attendance_table.insert("", END, values=row)

    def importCsv(self):
        self.mydata.clear()
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            with open(file_path, newline="") as file:
                reader = csv.reader(file)
                self.mydata = list(reader)
                self.fetchData()

    def exportCsv(self):
        try:
            if len(self.mydata) < 1:
                messagebox.showerror("No Data", "No Data Was Found to Export", parent=self.root)
                return
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if file_path:
                with open(file_path, mode="w", newline="") as file:
                    writer = csv.writer(file, delimiter=",")
                    for i in self.mydata:
                        writer.writerow(i)
                    messagebox.showinfo("Success", "Data exported successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
        
    def get_cursor(self, event=""):
        cursor_row = self.Attendance_table.focus()
        content = self.Attendance_table.item(cursor_row)
        rows = content['values']
        if rows:
            self.var_attend_id.set(rows[0])
            self.var_attend_roll.set(rows[1])
            self.var_attend_name.set(rows[2])
            self.var_attend_dep.set(rows[3])
            self.var_attend_time.set(rows[4])
            self.var_attend_date.set(rows[5])
            self.var_attend_status.set(rows[6])

     # reset data 
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_status.set("Status")

    def update_data(self):
        selected_item = self.Attendance_table.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to update!", parent=self.root)
            return

        content = self.Attendance_table.item(selected_item)
        row_data = content["values"]

        for index, row in enumerate(self.mydata):
            if row == row_data:
                self.mydata[index] = [
                    self.var_attend_id.get(),
                    self.var_attend_roll.get(),
                    self.var_attend_name.get(),
                    self.var_attend_dep.get(),
                    self.var_attend_time.get(),
                    self.var_attend_date.get(),
                    self.var_attend_status.get()
                ]
                break

        self.fetchData()
        messagebox.showinfo("Success", "Attendance record updated successfully!", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
