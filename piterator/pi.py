import math
from tkinter import *

def calculate_pi():
    # Get the user-specified digit of pi
    digit = int(input_field.get())

    # Calculate the corresponding digit of pi
    pi = math.pi
    pi_string = str(pi)
    pi_digit = pi_string[digit]

    # Display the result in the output field
    output_field.config(text=f"The {digit}th digit of pi is: {pi_digit}")

# Create the main window
window = Tk()
window.title("Digit of Pi Calculator")

# Create a label for the input field
input_label = Label(window, text="Enter the digit of pi you want to calculate:")
input_label.pack()

# Create an input field where the user can enter the digit of pi they want to calculate
input_field = Entry(window)
input_field.pack()

# Create a button to trigger the calculation of the specified digit of pi
calculate_button = Button(window, text="Calculate Pi Digit", command=calculate_pi)
calculate_button.pack()

# Create a label for the output field
output_label = Label(window, text="The result will be displayed here:")
output_label.pack()

# Create an output field where the result will be displayed
output_field = Label(window)
output_field.pack()

# Run the main event loop to display the window
window.mainloop()
