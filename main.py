import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=20)
window.config(padx=30, pady=30, bg="#2c3e50")

weight_input_label = tkinter.Label(text="Enter Your Weight (kg)", font=('Arial', 15, 'normal'), fg='white',
                                   bg="#2c3e50")
weight_input_label.config(fg="white")
weight_input_label.pack()

weight_input = tkinter.Entry(width=20)
weight_input.pack(pady=5)

height_input_label = tkinter.Label(text="Enter Your Height (cm)", font=('Arial', 15, 'normal'), fg="white",
                                   bg="#2c3e50")
height_input_label.config(fg="white")
height_input_label.pack()

height_input = tkinter.Entry(width=20)
height_input.pack(pady=5)


def calculate_bmi():
    try:
        if not weight_input.get() or not height_input.get():
            result_label.config(text="Enter both weight and height!")
            return

        weight = float(weight_input.get())
        height = float(height_input.get())

        result = weight / ((height / 100) ** 2)
        if result < 18.5:
            result_label.config(text=f"Your BMI is: {result:.2f}. You are a underweight", fg='blue')

        elif 18.5 <= result <= 24.9:
            result_label.config(text=f"Your BMI is {result:.2f}. You are a normal weight", fg='green')

        elif 25 <= result <= 29.9:
            result_label.config(text=f"Your BMI is {result:.2f}. You are a overweight", fg='orange')

        elif 30 <= result <= 34.9:
            result_label.config(text=f"Your BMI is {result:.2f}. You are a obesity ( class 1 )", fg='red')

        elif 35 <= result <= 39.9:
            result_label.config(text=f"Your BMI is {result:.2f}. You are obesity ( class 2 )", fg='red')

        else:
            result_label.config(text=f" Your BMI is {result:.2f}. You are extreme obesity", fg='darkred')

    except ValueError:
        result_label.config(text="Enter a valid number!", fg='red')


calculate_button = tkinter.Button(text='Calculate', command=calculate_bmi)
calculate_button.config(pady=5)
calculate_button.pack()


def clear_fields():
    weight_input.delete(0, tkinter.END)
    height_input.delete(0, tkinter.END)
    result_label.config(text="")


clear_button = tkinter.Button(text="Clear", command=clear_fields)
clear_button.pack(pady=5)

result_label = tkinter.Label(text="", font=('Arial', 15, 'normal'))
result_label.pack(pady=10)

window.mainloop()
