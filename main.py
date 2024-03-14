# Import necessary libraries
from tkinter import *
import pandas
import random

# Set background color
BACKGROUND_COLOR = "#B1DDC6"

# Attempt to read data from the CSV file, handle the case if the file is not found
try:
	data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
	# If the file is not found, read the original data from another CSV file
	original_data = pandas.read_csv("data/french_words.csv")
	to_learn = original_data.to_dict(orient="records")
else:
	# If data is successfully read from the file, convert it to a dictionary
	to_learn = data.to_dict(orient="records")

# Global variable to store the current flash card
current_card = {}


# Function to display the next flash card
def next_card():
	global current_card, flip_timer
	# Cancel any ongoing flip timer
	window.after_cancel(flip_timer)

	# Pick a random word from the data
	current_card = random.choice(to_learn)

	# Update the flash card Canvas with the new word
	canvas.itemconfig(card_title, text="French", fill="black")
	canvas.itemconfig(card_word, text=current_card['French'], fill="black")
	canvas.itemconfig(card_background, image=card_front_image)

	# Set a timer to automatically flip the card after 5000 milliseconds (5 seconds)
	flip_timer = window.after(5000, func=flip_card)


# Function to flip the flash card and show the English translation
def flip_card():
	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word, text=current_card['English'], fill="white")
	canvas.itemconfig(card_background, image=card_back_image)


# Function to handle when the user marks a word as known
def is_known():
	# Remove the current word from the to_learn list
	to_learn.remove(current_card)
	# Display the next flash card
	next_card()
	# Update the CSV file with the remaining words to learn
	data = pandas.DataFrame(to_learn)
	data.to_csv("data/words_to_learn.csv", index=False)
	# Display the next flash card again
	next_card()


# Create the main window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set a timer to automatically flip the card after 5000 milliseconds (5 seconds)
flip_timer = window.after(5000, func=flip_card)

# Create the flash card Canvas with image and text
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Create a title for the flash card
card_title = canvas.create_text(400, 100, font=("Arial", 40, "italic"))

# Create the word text on the flash card
card_word = canvas.create_text(400, 200, font=("Arial", 50, "bold",))

# Position the canvas in the window
canvas.grid(row=0, column=0, columnspan=2, pady=(10, 0))

# Create buttons for wrong and right answers
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0, pady=(10, 10))

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1, pady=(10, 10))

# Initialize the flash card with a random word
next_card()

# Start the Tkinter main loop
window.mainloop()

