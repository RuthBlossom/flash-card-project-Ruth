# Flash Card App

This is a simple flash card application built with Python and Tkinter for learning French vocabulary. It allows users to practice French words by displaying them on flash cards and providing their English translations.

![Capture Flash card 2](https://github.com/user-attachments/assets/109729ec-7e1e-4712-8708-241deb5bceed)

![Capture Flash card 3](https://github.com/user-attachments/assets/55edd058-0bea-493e-8830-c7e63c79c8f4)




## Features

- **Interactive Flash Cards**: Users can view French words on the front side of the card and their English translations on the back side.
- **Automatic Card Flipping**: The app automatically flips the flash card after 5 seconds to reveal the English translation.
- **Mark as Known**: Users can mark words as known, which removes them from the list of words to learn and proceeds to the next word.
- **Persistent Data Storage**: The app stores the list of words to learn in a CSV file, ensuring that progress is saved between sessions.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 
- Tkinter (usually included with Python)

## Installation

1. Clone this repository:


2. Navigate to the project directory:


3. Run the application:

```
python main.py
```

## Usage

- Upon launching the application, a flash card with a French word will be displayed.
- After 5 seconds, the card will automatically flip to reveal the English translation.
- Click the green checkmark button if you know the word, or the red cross button if you don't.
- Words marked as known will be removed from the list, and the app will proceed to the next word.

## Customization

- You can customize the flash card images and data files by replacing the existing files in the `images` and `data` directories, respectively.
