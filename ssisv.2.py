import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import re
import mysql.connector
from mysql.connector import Error


try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        database="ssis"  
    )

    if db.is_connected():
        print("Connected to MySQL")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `add`")
    records = cursor.fetchall()

    for record in records:
        print(record)

except Error as e:
    print("Error:", e)


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

# ==== ENTRY ====#
IDno_lbl = tk.Label(detail_frame, text="ID Number", font=('Arial', 9, "bold"), bg="#455864")
IDno_lbl.grid(row=0, column=0, padx=2, pady=2)

IDno_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 9))
IDno_ent.grid(row=0, column=1, padx=2, pady=2)

name_lbl = tk.Label(detail_frame, text="Last Name", font=('Arial', 9, "bold"), bg="#455864")
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 9))
name_ent.grid(row=1, column=1, padx=2, pady=2)

name1_lbl = tk.Label(detail_frame, text="First Name", font=('Arial', 9, "bold"), bg="#455864")
name1_lbl.grid(row=2, column=0, padx=2, pady=2)

name1_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 9))
name1_ent.grid(row=2, column=1, padx=2, pady=2)

name2_lbl = tk.Label(detail_frame, text="Middle Name", font=('Arial', 9, "bold"), bg="#455864")
name2_lbl.grid(row=3, column=0, padx=2, pady=2)

name2_ent = tk.Entry(detail_frame, bd=7, font=('Arial', 9))
name2_ent.grid(row=3, column=1, padx=2, pady=2)


Yearlvl_lbl = tk.Label(detail_frame, text="Year Level", font=('Arial', 9, "bold"), bg="#455864")
Yearlvl_lbl.grid(row=4, column=0, padx=2, pady=2)

Yearlvl_ent = ttk.Combobox(detail_frame, text="Year Level", font=('Arial', 9), state="readonly")
Yearlvl_ent.grid(row=4, column=1, padx=2, pady=2)
Yearlvl_ent['values'] = ("1st Year", "2nd Year", "3rd Year", "4th Year")

gender_lbl = tk.Label(detail_frame, text="Gender", font=('Arial', 9, "bold"), bg="#455864")
gender_lbl.grid(row=5, column=0, padx=2, pady=2)

gender_ent = ttk.Combobox(detail_frame, text="Gender", font=('Arial', 9), state="readonly")
gender_ent.grid(row=5, column=1, padx=2, pady=2)
gender_ent['values'] = ("Male", "Female", "Other")

Coursecd_lbl = tk.Label(detail_frame, text="Course Code", font=('Arial', 9, "bold"), bg="#455864")
Coursecd_lbl.grid(row=6, column=0, padx=2, pady=2)
Coursecd_ent = ttk.Combobox(detail_frame, text="Course Code", font=('Arial', 9))
Coursecd_ent.grid(row=6, column=1, padx=2, pady=2)
#=================#

# ====Buttons====#
btn_frame = tk.Frame(detail_frame, bg="#455864", bd=5, relief=tk.GROOVE)
btn_frame.place(x=8, y=380, width=237, height=45)  

add_btn = tk.Button(btn_frame, bg="#455864", text="Add", bd=5, font=("Arial", 8), width=6)
add_btn.grid(row=0, column=0, padx=2, pady=2)

update_btn = tk.Button(btn_frame, bg="#455864", text="Update", bd=5, font=("Arial", 8), width=6)
update_btn.grid(row=0, column=1, padx=3, pady=2)

delete_btn = tk.Button(btn_frame, bg="#455864", text="Delete", bd=5, font=("Arial", 8), width=6)
delete_btn.grid(row=0, column=2, padx=2, pady=2)

clear_btn = tk.Button(btn_frame, bg="#455864", text="Clear", bd=5, font=("Arial", 8), width=6)
clear_btn.grid(row=0, column=3, padx=3, pady=2)


# ===============#

# ====SEARCHING====#
search_frame = tk.Frame(data_frame, bg="#455864",bd=5, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search", bg="#455864", font=("Arial", 9, "bold"))
search_lbl.grid(row=0, column=0, padx=2, pady=2)

search_in = tk.Label(search_frame, font=("Arial", 9, "bold"),width=38)
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

main_frame = tk.Frame(data_frame, bg="#455864", bd=5, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

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

student_table.column("ID Number", width=100)
student_table.column("Last Name", width=100)
student_table.column("First Name", width=100)
student_table.column("Middle Name", width=100)
student_table.column("Year Level", width=100)
student_table.column("Gender", width=100)
student_table.column("Course", width=100)

student_table.pack(fill=tk.BOTH, expand=True)

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
#======================
def open_view_courses_dialog():
    dialog_window = tk.Toplevel(win)
    dialog_window.title("Available Courses")

    listbox = tk.Listbox(dialog_window, font=("Arial", 12), selectmode=tk.SINGLE)
    listbox.pack(padx=20, pady=10)

    edit_button = tk.Button(dialog_window, text="Edit")
    edit_button.pack(pady=10)


#====================
def add_student():
    id_number = IDno_ent.get()
    last_name = name_ent.get()
    first_name = name1_ent.get()
    middle_name = name2_ent.get()
    yearlvl = Yearlvl_ent.get()
    gender = gender_ent.get()
    course_code = Coursecd_ent.get()

    if id_number and last_name and first_name and middle_name and yearlvl and gender and course_code:
        try:
            cursor.execute("INSERT INTO students (id_number, last_name, first_name, middle_name, year_level, gender, course_code) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (id_number, last_name, first_name, middle_name, yearlvl, gender, course_code))
            db.commit()
            messagebox.showinfo("Success", "Student added successfully!")
            clear_entries()
            update_student_table()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error adding student: {e}")
    else:
        messagebox.showerror("Missing Information", "Please fill in all fields.")

def delete_student():
    response = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?")
    if response:
        selected_item = student_table.selection()
        if selected_item:
            student_id = student_table.item(selected_item, 'values')[0]
            try:
                cursor.execute("DELETE FROM students WHERE id_number = %s", (student_id,))
                db.commit()
                messagebox.showinfo("Delete Student", "Student record deleted successfully!")
                update_student_table()
            except mysql.connector.Error as e:
                messagebox.showerror("Delete Student", f"Error deleting student: {e}")
    else:
        messagebox.showinfo("Delete Cancelled", "Student deletion cancelled")

def save_updated_student(student_id):
    new_id_number = IDno_ent.get()
    new_last_name = name_ent.get()
    new_first_name = name1_ent.get()
    new_middle_name = name2_ent.get()
    new_yearlvl = Yearlvl_ent.get()
    new_gender = gender_ent.get()
    new_course_code = Coursecd_ent.get()

    try:
        cursor.execute("UPDATE students SET id_number = %s, last_name = %s, first_name = %s, middle_name = %s, year_level = %s, gender = %s, course_code = %s WHERE id_number = %s",
                       (new_id_number, new_last_name, new_first_name, new_middle_name, new_yearlvl, new_gender, new_course_code, student_id))
        db.commit()
        messagebox.showinfo("Update Student", "Student information updated successfully!")
        clear_entries()
        update_student_table()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error updating student: {e}")

def clear_entries():
    IDno_ent.delete(0, tk.END)
    name_ent.delete(0, tk.END)
    name1_ent.delete(0, tk.END)
    name2_ent.delete(0, tk.END)
    Yearlvl_ent.set('')
    gender_ent.set('')
    Coursecd_ent.set('')

def update_student_table():
    student_table.delete(*student_table.get_children())
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        for student in students:
            student_table.insert('', 'end', values=student)
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error fetching students: {e}")
#====================

win.mainloop()