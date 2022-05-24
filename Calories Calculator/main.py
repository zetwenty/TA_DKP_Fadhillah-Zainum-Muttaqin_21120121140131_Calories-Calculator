from cProfile import label
from cgitb import text
from tkinter import *
from rumus import *

def calculate():
    # -------------Input dan menampilkan data----------------

    # Data inputan GUI
    umur = float(umur_input.get())
    berat = float(berat_input.get())
    tinggi = float(tinggi_input.get())
    detakJ = float(detakJ_input.get())
    durasi = float(durasi_input.get())

    if gender.get() == 0:
        # Perhitungan pada laki-laki
        bmr = male_bmr(berat, tinggi, umur)
        calories_burned = male_caloriesB(detakJ, berat, umur, durasi)
    else:
        # Perhitungan pada perempuan
        bmr = female_bmr(berat, tinggi, umur)
        calories_burned = female_caloriesB(detakJ, berat, umur, durasi)
    
    
    bmi = bmi_cal(berat, tinggi)
    if bmi < 18.5:
        pesan="Berat badan kurang"
    elif bmi >= 18.5 and bmi <= 22.9:
        pesan="Berat badan normal"
    else:
        pesan="Berat badan berlebih"
    

    # Menampilkan data yang telah dihitung
    bmr_output.config(text=int(bmr))
    calorB_output.config(text=int(calories_burned))
    bmi_output.config(text=float(bmi))
    pesan_output.config(text=pesan)


def clear():
    # Mengosongkan inputan
    bmr_output.config(text="")
    calorB_output.config(text="")
    bmi_output.config(text="")
    pesan_output.config(text="")

    # Menghapus output
    umur_input.delete(0, END)
    berat_input.delete(0, END)
    tinggi_input.delete(0, END)
    detakJ_input.delete(0, END)
    durasi_input.delete(0, END)


root = Tk()
root.title("Calorie Calculator")
root.bind("<Return>", lambda x: calculate())
root.config(bg="lightblue")
app_title = Label(
    root, text="EXERCISE CALORIE CALCULATOR", pady=10, font=("Calibri 12 bold"), bg=("lightblue")
)
app_title.grid(row=0, column=0, columnspan=2)
gender = IntVar()

# ---------------- INPUT FRAME -------------------
input_frame = LabelFrame(root, text="Enter your data", padx=30, pady=20, bg="lightblue")
input_frame.grid(row=1, column=0, padx=10)

# Isi dari Input Frame
umur_label = Label(input_frame, text="Age")
umur_label.grid(row=0, column=0)
umur_label.config(bg="lightblue")
umur_input = Entry(input_frame, width=10)
umur_input.grid(row=0, column=1, columnspan=2)

tinggi_label = Label(input_frame, text="Height (cm)")
tinggi_label.grid(row=4, column=0, pady=[30, 30])
tinggi_label.config(bg="lightblue")
tinggi_input = Entry(input_frame, width=10)
tinggi_input.grid(row=4, column=1, columnspan=2)

berat_label = Label(input_frame, text="Weight (kg)")
berat_label.grid(row=5, column=0)
berat_label.config(bg="lightblue")
berat_input = Entry(input_frame, width=10)
berat_input.grid(row=5, column=1, columnspan=2)

durasi_label = Label(input_frame, text="Duration (Min)")
durasi_label.grid(row=6, column=0, pady=[30, 30])
durasi_label.config(bg="lightblue")
durasi_input = Entry(input_frame, width=10)
durasi_input.grid(row=6, column=1, columnspan=2)

detakJ_label = Label(input_frame, text="Heartrate")
detakJ_label.grid(row=8, column=0)
detakJ_label.config(bg="lightblue")
detakJ_input = Entry(input_frame, width=10)
detakJ_input.grid(row=8, column=1, columnspan=2)

# Pilihan jenis kelamin
r1 = Radiobutton(input_frame, text="Male", variable=gender, value=0)
r1.grid(row=10, column=0, pady=[10, 0])
r1.config(bg="lightblue")

r2 = Radiobutton(input_frame, text="Female", variable=gender, value=1)
r2.grid(row=10, column=1, pady=[10, 0])
r2.config(bg="lightblue")

# -------------------- OUTPUT FRAME --------------------
output_frame = LabelFrame(root, text="Output")
output_frame.grid(row=1, column=1, ipady=10, padx=20)
output_frame.config(bg="lightblue")

# Isi dari Output Frame
bmr_label = Label(output_frame, text="BMR", font="bold", bg="lightblue")
bmr_label.grid(row=1, column=0, padx=30, pady=[30, 0])
bmr_output = Label(output_frame, font=("Helvetica 15 bold"), bg="lightblue")
bmr_output.grid(row=2, column=0)

calorB_label = Label(output_frame, text="Calories Burned", font="bold", padx=25, bg="lightblue")
calorB_label.grid(row=3, column=0, pady=[30, 0])
calorB_output = Label(output_frame, font=("Helvetica 15 bold"), bg="lightblue")
calorB_output.grid(row=5, column=0)

bmi_label = Label(output_frame, text="BMI", font="bold", padx=25, bg="lightblue")
bmi_label.grid(row=7, column=0, pady=[30, 0])
bmi_output = Label(output_frame, font=("Helvetica 15 bold"), bg="lightblue")
bmi_output.grid(row=8, column=0)

pesan_output = Label(output_frame, font=("Helvetica 15 bold"), bg="lightblue")
pesan_output.grid(row=9, column=0, columnspan=2)

# Tombol Calculate
calculate_button = Button(root, width=15, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, pady=[20, 0], padx=20)

# Tombol Clear
clear_button = Button(root, width=15, text="Clear", command=clear)
clear_button.grid(row=2, column=1, pady=[20, 0])

# Tombol Exit
exit_button = Button(root, width=20, text="Exit", command=root.quit)
exit_button.grid(row=3, column=0, pady=[20, 10], columnspan=2)

root.mainloop()