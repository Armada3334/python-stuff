import random
from tkinter import *

def roll_die(num_sides):
  return random.randint(1, num_sides)

def roll_dice():
  # Check if the user entered a die type
  if die_type_input.get():
    # If a die type was entered, check if a modifier was also entered
    if modifier_input.get():
      # If a modifier was entered, convert the die type and the modifier to integers
      # and add the modifier to the roll
      die_type = int(die_type_input.get())
      modifier = int(modifier_input.get())
      roll = roll_die(die_type)
      total = roll + modifier
      if modifier >= 0:
        result_text.set("You rolled a " + str(total) + " (" + str(roll) + " + " + str(modifier) + ". d" + str(die_type) +  ")")
      else:
        result_text.set("You rolled a " + str(total) + " (" + str(roll) + str(modifier) + ". d" + str(die_type) +  ")")
    else:
      # If no modifier was entered, roll the die and display the result
      die_type = int(die_type_input.get())
      roll = roll_die(die_type)
      result_text.set("You rolled a " + str(roll) + " (d" + str(die_type) + ")")
  else:
    # If no die type was entered, assume d20
    if modifier_input.get():
      # If a modifier was entered, convert the die type and the modifier to integers
      # and add the modifier to the roll
      modifier = int(modifier_input.get())
      roll = roll_die(20)
      total = roll + modifier
      if modifier >= 0:
        result_text.set("You rolled a " + str(total) + " (" + str(roll) + " + " + str(modifier) + ". d20)")
      else:
        result_text.set("You rolled a " + str(total) + " (" + str(roll) + str(modifier) + ". d20)")
    else:
      # If no modifier was entered, roll the die and display the result
      roll = roll_die(20)
      result_text.set("You rolled a " + str(roll) + " on a d20")

root = Tk()
root.title("D&D Dice Roller")
root.geometry("500x300")

# Set the background color of the window to dark grey
root.configure(bg="#222222")

# Create a main frame to hold all the widgets
main_frame = Frame(root, bg="#222222")
main_frame.pack()

# Create a label for the die type input
die_type_label = Label(main_frame, text="Die Type:", font=("Arial", 18), bg="#222222", fg="white")
die_type_label.grid(row=0, column=0, padx=10, pady=10)

# Create a text entry field for the die type
die_type_input = Entry(main_frame, font=("Arial", 18), bg="#333333", fg="white")
die_type_input.grid(row=0, column=1, padx=10, pady=10)
# Create a label for the modifier input
modifier_label = Label(main_frame, text="Modifier:", font=("Arial", 18), bg="#222222", fg="white")
modifier_label.grid(row=1, column=0, padx=10, pady=10)

# Create a text entry field for the modifier
modifier_input = Entry(main_frame, font=("Arial", 18), bg="#333333", fg="white")
modifier_input.grid(row=1, column=1, padx=10, pady=10)

# Create a button to roll the die
roll_button = Button(main_frame, text="Roll", font=("Arial", 18), bg="#333333", fg="white", command=roll_dice)
roll_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the result
result_text = StringVar()
result_label = Label(main_frame, textvariable=result_text, font=("Arial", 18), bg="#222222", fg="white")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
