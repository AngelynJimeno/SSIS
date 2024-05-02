import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox
from tkinter import simpledialog
import re
#==============gui===========
win = tk.Tk()
win.geometry("800x580+15+50")
win.title("Student Information System")     

title_label = tk.Label(win, text="Student Information System", font=("Arial", 30, "bold"), border=8, relief=tk.GROOVE,bg="#455a64", foreground="#90a4ae")
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="Student Details", font=("Arial", 17, "bold"), bg="#455a64", fg="#90a4ae", bd=5,relief=tk.GROOVE)
detail_frame.place(x=20, y=90, width=260, height=466)

data_frame = tk.Frame(win, bg="#455864", bd=5, relief=tk.GROOVE)
data_frame.place(x=300, y=90, width=477, height=350)

addcourse_frame = tk.LabelFrame(win, text="Add Course", font=("Arial", 14, "bold"), bg="#455a64", fg="#90a4ae", bd=5,relief=tk.GROOVE)
addcourse_frame.place(x=300, y=450, width=230, height=107)

deletecourse_frame = tk.LabelFrame(win, text="Delete Course", font=("Arial", 14, "bold"), bg="#455a64", fg="#90a4ae", bd=5,relief=tk.GROOVE)
deletecourse_frame.place(x=546, y=450, width=230, height=65)

viewcourse_frame = tk.LabelFrame(win, text="", font=("Arial", 13, "bold"), bg="#455a64", fg="#90a4ae", bd=5,relief=tk.GROOVE)
viewcourse_frame.place(x=546, y=520, width=230, height=37)
viewcourse_button = tk.Button(viewcourse_frame, text="View Available Courses", bg="#455864", fg="#90a4ae")
viewcourse_button.pack(fill=tk.X)

#================
IDno = tk.StringVar()
name = tk.StringVar()
name1 = tk.StringVar()
name2 = tk.StringVar()
Yearlvl = tk.StringVar()
gender = tk.StringVar()
Coursecd = tk.StringVar()

search_by = tk.StringVar()
#================

# ==== ENTRY ====#
IDno_lbl = tk.Label(detail_frame, text="ID Number", font=('Arial', 9, "bold"), bg="#455864")
IDno_lbl.grid(row=0, column=0, padx=2, pady=2)

IDno_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 9),textvariable=IDno)
IDno_ent.grid(row=0, column=1, padx=2, pady=2)

name_lbl = tk.Label(detail_frame, text="Last Name", font=('Arial', 9, "bold"), bg="#455864")
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 9),textvariable=name)
name_ent.grid(row=1, column=1, padx=2, pady=2)

name1_lbl = tk.Label(detail_frame, text="First Name", font=('Arial', 9, "bold"), bg="#455864")
name1_lbl.grid(row=2, column=0, padx=2, pady=2)

name1_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 9),textvariable=name1)
name1_ent.grid(row=2, column=1, padx=2, pady=2)

name2_lbl = tk.Label(detail_frame, text="Middle Name", font=('Arial', 9, "bold"), bg="#455864")
name2_lbl.grid(row=3, column=0, padx=2, pady=2)

name2_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 9),textvariable=name2)
name2_ent.grid(row=3, column=1, padx=2, pady=2)


Yearlvl_lbl = tk.Label(detail_frame, text="Year Level", font=('Arial', 9, "bold"), bg="#455864")
Yearlvl_lbl.grid(row=4, column=0, padx=2, pady=2)

Yearlvl_ent = ttk.Combobox(detail_frame, text="Year Level", font=('Arial', 9), state="readonly",textvariable=Yearlvl)
Yearlvl_ent.grid(row=4, column=1, padx=2, pady=2)
Yearlvl_ent['values'] = ("1st Year", "2nd Year", "3rd Year", "4th Year")

gender_lbl = tk.Label(detail_frame, text="Gender", font=('Arial', 9, "bold"), bg="#455864")
gender_lbl.grid(row=5, column=0, padx=2, pady=2)

gender_ent = ttk.Combobox(detail_frame, text="Gender", font=('Arial', 9), state="readonly",textvariable=gender)
gender_ent.grid(row=5, column=1, padx=2, pady=2)
gender_ent['values'] = ("Male", "Female", "Other")

Coursecd_lbl = tk.Label(detail_frame, text="Course Code", font=('Arial', 9, "bold"), bg="#455864")
Coursecd_lbl.grid(row=6, column=0, padx=2, pady=2)
Coursecd_ent = ttk.Combobox(detail_frame, text="Course Code", font=('Arial', 9),textvariable=Coursecd)
Coursecd_ent.grid(row=6, column=1, padx=2, pady=2)

try:
    conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
    cursor = conn.cursor()
    cursor.execute("SELECT Coursecd FROM course")
    courses = cursor.fetchall()
    course_codes = [course[0] for course in courses]
    conn.close()
except pymysql.Error as e:
    messagebox.showerror("Error", f"Error fetching course codes: {e}")

Coursecd_ent['values'] = course_codes

#=================#

#=============funcs=======
def fetch_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
    curr = conn.cursor()
    curr.execute("SELECT * FROM `studata`")
    rows = curr.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', tk.END, values=row)
        conn.commit()
    conn.close()

def fill_entry_fields_on_update():
    cursor_row = student_table.focus()
    if cursor_row:
        content = student_table.item(cursor_row)['values']
        IDno.set(content[0])
        name.set(content[1])
        name1.set(content[2])
        name2.set(content[3])
        Yearlvl.set(content[4])
        gender.set(content[5])
        Coursecd.set(content[6])

def add_student():
    if IDno.get() == "" or name.get() == "" or name1.get() == "" or name2.get() == "":
        messagebox.showerror("Error!", "Please fill all entry fields!")
    elif not re.match(r'^\d{4}-\d{4}$', IDno.get()):
        messagebox.showerror("Error!", "Invalid ID format! It should be '0000-0000'.")
    elif Coursecd.get() not in course_codes:
        messagebox.showerror("Error!", "Course does not exist!")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
            cursor = conn.cursor()
            cursor.execute("SELECT ID FROM studata WHERE ID = %s", (IDno.get(),))
            existing_student = cursor.fetchone()
            if existing_student:
                messagebox.showerror("Error!", "Student with the same ID number already exists!")
            else:
                cursor.execute("INSERT INTO studata (ID, name, name1, name2, Yearlvl, gender, Coursecd) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                                (IDno.get(), name.get(), name1.get(), name2.get(), Yearlvl.get(), gender.get(), Coursecd.get()))
                conn.commit()
                conn.close()
                fetch_data()
                clear_entries()
                messagebox.showinfo("Success!", "Student added successfully!")
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error adding student: {e}")

#=========
def save_updated_student(student_id):
    new_id_number = IDno.get()
    new_last_name = name.get()
    new_first_name = name1.get()
    new_middle_name = name2.get()
    new_yearlvl = Yearlvl.get()
    new_gender = gender.get()
    new_course_code = Coursecd.get()

    try:
        # Check if the new ID already exists in the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
        cursor = conn.cursor()
        cursor.execute("SELECT ID FROM studata WHERE ID = %s AND ID != %s", (new_id_number, student_id))
        existing_student = cursor.fetchone()
        conn.close()

        if existing_student:
            messagebox.showerror("Error", f"Student with ID number '{new_id_number}' already exists!")
        else:
            # Update the student record
            conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
            cursor = conn.cursor()
            cursor.execute('''UPDATE studata SET ID=%s, name=%s, name1=%s, 
                           name2=%s, Yearlvl=%s, gender=%s, Coursecd=%s WHERE ID=%s''',
                           (new_id_number, new_last_name, new_first_name, new_middle_name, 
                           new_yearlvl, new_gender, new_course_code, student_id))
            conn.commit()
            conn.close()

            fetch_data()  # Refresh the table
            clear_entries()  # Clear entry fields

            messagebox.showinfo("Update Student", "Student information updated successfully!")
            
            # Reset the update button command to update_student()
            update_btn.config(command=update_student)

    except Exception as e:
        messagebox.showerror("Error", f"Error updating student: {e}")


# Function to populate the entry fields with the selected student's data for update
def update_student_window(student_id):
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM studata WHERE ID=%s", (student_id,))
        student_data = cursor.fetchone()

        if student_data:
            IDno.set(student_data[0])
            name.set(student_data[1])
            name1.set(student_data[2])
            name2.set(student_data[3])
            Yearlvl.set(student_data[4])
            gender.set(student_data[5])
            Coursecd.set(student_data[6])
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error updating student window: {e}")


# Function to update the student table with the data from the database
def update_student_table():
    student_table.delete(*student_table.get_children())

    try:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        for row in rows:
            student_table.insert('', tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Error updating student table: {e}")

# Update student button command
def update_student():
    selected_item = student_table.selection()
    if selected_item:
        for item in selected_item:
            student_id = student_table.item(item, 'values')[0]
            update_student_window(student_id)
            update_btn.config(command=lambda: save_updated_student(student_id))
            break
    else:
        messagebox.showerror("No Selection", "Please select a student from the table to update.")
#========


def delete_student():
    response = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?")
    if response:
        selected_item = student_table.focus()
        if selected_item:
            cursor_row = student_table.item(selected_item)
            content = cursor_row['values']
            student_id = content[0]
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
                curr = conn.cursor()
                curr.execute("DELETE FROM studata WHERE ID = %s", (student_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Delete Student", "Student record deleted successfully!")
                fetch_data()  # Refresh the table after deletion
                clear_entries()  # Clear the entry fields
            except pymysql.Error as e:
                messagebox.showerror("Delete Student", f"Error deleting student: {e}")
    else:
        messagebox.showinfo("Delete Cancelled", "Student deletion cancelled")


def clear_entries():
    IDno_ent.delete(0, tk.END)
    name_ent.delete(0, tk.END)
    name1_ent.delete(0, tk.END)
    name2_ent.delete(0, tk.END)
    Yearlvl_ent.set('')
    gender_ent.set('')
    Coursecd_ent.set('')


# ====Buttons====#
btn_frame = tk.Frame(detail_frame, bg="#455864", bd=5, relief=tk.GROOVE)
btn_frame.place(x=8, y=380, width=237, height=45)

add_btn = tk.Button(btn_frame, bg="#455864", text="Add", bd=5, font=("Arial", 8), width=6, command=add_student)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, bg="#455864", text="Update", bd=5, font=("Arial", 8), width=6)
update_btn.grid(row=0, column=1, padx=3, pady=2)
update_btn.config(command=update_student)

delete_btn = tk.Button(btn_frame, bg="#455864", text="Delete", bd=5, font=("Arial", 8), width=6)
delete_btn.grid(row=0, column=2, padx=2, pady=2)
delete_btn.config(command=delete_student)


clear_btn = tk.Button(btn_frame, bg="#455864", text="Clear", bd=5, font=("Arial", 8), width=6)
clear_btn.grid(row=0, column=3, padx=3, pady=2)
clear_btn.config(command=clear_entries)

# ===============#

# ====SEARCHING====#
search_frame = tk.Frame(data_frame, bg="#455864",bd=5, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search", bg="#455864", font=("Arial", 9, "bold"))
search_lbl.grid(row=0, column=0, padx=2, pady=2)

search_in = tk.Label(search_frame, font=("Arial", 9, "bold"),width=38,textvariable=search_by)
search_in.grid(row=0, column=1, padx=3, pady=2)

search_ent = tk.Entry(search_frame, font=("Arial", 9),width=38)
search_ent.insert(0, "Enter ID Number")
search_ent.grid(row=0, column=1, padx=3, pady=2)

def on_search_focus_in(event):
    if search_ent.get() == "Enter ID Number":
        search_ent.delete(0, tk.END)

search_ent.bind("<FocusIn>", on_search_focus_in)


search_btn = tk.Button(search_frame, text="Search", font=("Arial", 8, "bold"), bd=5, width=6, bg="#455864")
search_btn.grid(row=0, column=2, padx=3, pady=2)


refresh_btn = tk.Button(search_frame, text="Refresh", font=("Arial", 8, "bold"), bd=5, width=6, bg="#455864")
refresh_btn.grid(row=0, column=4, padx=3, pady=2)
refresh_btn.config(command=fetch_data)


main_frame = tk.Frame(data_frame, bg="#455864", bd=5, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

''' Last Name, First Name, Middle Name, Year Level, Gender, Course'''

student_table = ttk.Treeview(data_frame, columns=("ID Number","Last Name", "First Name", "Middle Name", "Year Level", "Gender", "Course"),yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("ID Number", text="ID Number")
student_table.heading("Last Name", text="Last Name")
student_table.heading("First Name", text="First Name")
student_table.heading("Middle Name", text="Middle Name")
student_table.heading("Year Level", text="Year Level")
student_table.heading("Gender", text="Gender")
student_table.heading("Course", text="Course")

student_table['show'] = 'headings'

student_table.column("ID Number", width=70)
student_table.column("Last Name", width=70)
student_table.column("First Name", width=70)
student_table.column("Middle Name", width=80)
student_table.column("Year Level", width=70)
student_table.column("Gender", width=70)
student_table.column("Course", width=70)

student_table.pack(fill=tk.BOTH, expand=True)

def search_student():
    search_text = search_ent.get()
    if search_text and search_text != "Enter ID Number":
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
            curr = conn.cursor()
            curr.execute("SELECT * FROM `studata` WHERE ID_Number=%s", (search_text,))
            rows = curr.fetchall()
            if len(rows) != 0:
                student_table.delete(*student_table.get_children())
                for row in rows:
                    student_table.insert('', tk.END, values=row)
            else:
                messagebox.showinfo("Search", "No matching records found.")
            conn.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error searching student: {e}")
    else:
        messagebox.showerror("Error", "Please enter valid ID Number to search.")

search_btn.config(command=search_student)

#============================
addCoursecd_ent = tk.Entry(addcourse_frame, bd=7, font=('Arial', 9))
addCoursecd_ent.grid(row=0, column=0, columnspan=2, padx=2, pady=2)
addCoursecd_ent.insert(0, "Enter Course Code")  

def on_add_course_focus_in(event):
    if addCoursecd_ent.get() == "Enter Course Code":
        addCoursecd_ent.delete(0, tk.END)

addCoursecd_ent.bind("<FocusIn>", on_add_course_focus_in)

addCoursetitle_ent = tk.Entry(addcourse_frame, bd=7, font=('Arial', 9))
addCoursetitle_ent.grid(row=1, column=0, columnspan=2, padx=2, pady=2)
addCoursetitle_ent.insert(0, "Enter Course Title")  

def on_add_title_focus_in(event):
    if addCoursetitle_ent.get() == "Enter Course Title":
        addCoursetitle_ent.delete(0, tk.END)

addCoursetitle_ent.bind("<FocusIn>", on_add_title_focus_in)

save_btn = tk.Button(addcourse_frame, bg="#455864", text="Save", bd=5, font=("Arial", 8, "bold"), width=6)
save_btn.grid(row=0, column=3, padx=2, pady=2)

def fetch_course_codes():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
        cursor = conn.cursor()
        cursor.execute("SELECT Coursecd FROM course")
        courses = cursor.fetchall()
        course_codes = [course[0] for course in courses]
        conn.close()
        Coursecd_ent['values'] = course_codes
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error fetching course codes: {e}")

def save_course():
    new_course_code = addCoursecd_ent.get()
    new_course_title = addCoursetitle_ent.get()

    if new_course_code == "" or new_course_code == "Enter Course Code":
        messagebox.showerror("Error!", "Please enter valid course code!")
    elif new_course_title == "" or new_course_title == "Enter Course Title":
        messagebox.showerror("Error!", "Please enter valid course title!")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM course WHERE Coursecd = %s", (new_course_code,))
            if cursor.fetchone():
                messagebox.showerror("Error", f"Course code '{new_course_code}' already exists!")
            else:

                cursor.execute("INSERT INTO course (Coursecd, CourseTitle) VALUES (%s, %s)", (new_course_code, new_course_title))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Course added successfully!")
                addCoursecd_ent.delete(0, tk.END)
                addCoursetitle_ent.delete(0, tk.END)
                fetch_course_codes()  
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error adding course: {e}")



save_btn.config(command=save_course)


delCoursecd_ent = tk.Entry(deletecourse_frame, bd=7, font=('Arial', 9))
delCoursecd_ent.grid(row=0, column=0, columnspan=2, padx=2, pady=2)
delCoursecd_ent.insert(0, "Enter Course Code")  

def on_del_course_focus_in(event):
    if delCoursecd_ent.get() == "Enter Course Code":
        delCoursecd_ent.delete(0, tk.END)

def on_del_course_key(event):
    delCoursecd_ent.unbind("<Key>")  

delCoursecd_ent.bind("<FocusIn>", on_del_course_focus_in)
delCoursecd_ent.bind("<Key>", on_del_course_key)

del_btn = tk.Button(deletecourse_frame, bg="#455864", text="Save", bd=5, font=("Arial", 8, "bold"), width=6)
del_btn.grid(row=0, column=3, padx=2, pady=2)

def delete_course():
    course_code = delCoursecd_ent.get()

    if course_code == "" or course_code == "Enter Course Code":
        messagebox.showerror("Error!", "Please enter valid course code!")
    else:
        response = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete course code {course_code}?")
        if response:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
                cursor = conn.cursor()
                
                cursor.execute("DELETE FROM studata WHERE Coursecd = %s", (course_code,))

                cursor.execute("DELETE FROM course WHERE Coursecd = %s", (course_code,))
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", f"Course code {course_code} and associated students deleted successfully!")
                delCoursecd_ent.delete(0, tk.END)
                fetch_course_codes() 
            except pymysql.Error as e:
                messagebox.showerror("Error", f"Error deleting course: {e}")
        else:
            messagebox.showinfo("Delete Cancelled", "Course deletion cancelled")

fetch_course_codes()


del_btn.config(command=delete_course)


fetch_data()
#student_table.bind("<ButtonRelease-1>", get_cursor)


#============================
def open_view_courses_dialog():
    dialog_window = tk.Toplevel(win)
    dialog_window.title("Available Courses")
    dialog_window.geometry("400x300")

    listbox_width = 40  
    listbox_height = 12  

    listbox = tk.Listbox(dialog_window, font=("Arial", 12), selectmode=tk.SINGLE, width=listbox_width, height=listbox_height)
    listbox.pack(padx=20, pady=10)

    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course")
        courses = cursor.fetchall()
        if courses:
            for course in courses:
                listbox.insert(tk.END, f"{course[0]} - {course[1]}")
        else:
            listbox.insert(tk.END, "No courses available.")
        conn.close()
    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error fetching courses: {e}")

    def edit_course():
        selected_index = listbox.curselection()
        if selected_index:
            selected_course = listbox.get(selected_index)
            new_course_code = simpledialog.askstring("Edit Course", "Enter new course code:")
            if new_course_code:
                if new_course_code in [course[0] for course in courses]:
                    messagebox.showerror("Error", "Course code already exists!")
                else:
                    old_course_code = selected_course.split()[0]
                    try:
                        conn = pymysql.connect(host="localhost", user="root", password="", database="ssisv2.1")
                        cursor = conn.cursor()

                        # Update course code in the course table
                        cursor.execute("UPDATE course SET Coursecd = %s WHERE Coursecd = %s", (new_course_code, old_course_code))

                        # Update course code in the studata table
                        cursor.execute("UPDATE studata SET Coursecd = %s WHERE Coursecd = %s", (new_course_code, old_course_code))

                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success", "Course updated successfully!")
                        dialog_window.destroy()
                        open_view_courses_dialog()
                    except pymysql.Error as e:
                        messagebox.showerror("Error", f"Error updating course: {e}")



    edit_button = tk.Button(dialog_window, text="Edit", command=edit_course)
    edit_button.pack(pady=10)

viewcourse_button.config(command=open_view_courses_dialog)


win.mainloop()
