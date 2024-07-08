#   Python program to play text based sargam as audio
#   Nilesh Kodikal 11 June 2024
#

import tkinter as tk
from tkinter import ttk, scrolledtext
from help_text import show_help, ragas_index
from constants import midi_program
from audio_player import play
from game import play_game
import sys

root = tk.Tk()
root.title("Swara Player")

# Scrollable Text widget for score
score_text = scrolledtext.ScrolledText(root, width=50, height=10, font=('Courier New', 14))
score_text.grid(column=0, row=0, columnspan=5, sticky='ew', padx=10,pady=10)  


# Radiobuttons for instrument selection
instrument_var = tk.StringVar(value='flute')  # Set default instrument to 'piano'
for i, instrument in enumerate(midi_program.keys()):
    rb = tk.Radiobutton(root, text=instrument, variable=instrument_var, value=instrument)
    rb.grid(column=i%4, row=2+i//4, pady=2)  # Arrange the radio buttons in a 2x4 grid starting from column 0

# Checkbutton for metronome
metronome_var = tk.IntVar(value='0')
metronome_check = tk.Checkbutton(root, text="Metronome", variable=metronome_var)
metronome_check.grid(column=0, row=4, pady=10)  

# Label for taal entry
taal_label = tk.Label(root, text="Taal:")
taal_label.grid(column=1, row=4 , sticky='e', pady=10)

# Entry for taal
taal_var = tk.StringVar(value='4')  # Set default tempo to 4
taal_entry = tk.Entry(root, textvariable=taal_var, width=6)
taal_entry.grid(column=2, row=4, pady=10)  # Increase columnspan to 6

# Create a StringVar to hold the bpm value
bpm_var = tk.StringVar(value='60')

# Create a Label for the bpm Entry
bpm_label = tk.Label(root, text="BPM:")
bpm_label.grid(column=3, row=4, pady=10)  # Adjust the row and column as needed

# Create the bpm Entry
bpm_entry = tk.Entry(root, textvariable=bpm_var, width=6)
bpm_entry.grid(column=4, row=4 , pady=10, sticky='w')  # Adjust the row and column as needed

# Play button
play_button = tk.Button(root, text="Play ⯈", command=lambda: play(score_text, taal_var, bpm_var, metronome_var, instrument_var), bg='#7adb50', font=('Helvetica', 12) )
play_button.grid(column=3, row=6, pady=20)


# Help button
help_button = tk.Button(root, text="Help", command=lambda: show_help(root))
help_button.grid(column=0, row=6)

# Game button

game_button = tk.Button(root, text="Play Game")
game_button.grid(column=1, row=6)

def on_game_button_click():
    root.iconify()  # Minimize the window
    play_game()  # Call the function to play the game
    root.deiconify()

# Update the button binding
game_button.bind("<Button-1>", lambda event: on_game_button_click())

# combo-box for raga selection
raga_var = tk.StringVar()
raga_combo = ttk.Combobox(root, textvariable=raga_var, values=sorted(list(ragas_index.keys())))
raga_combo.grid(column=2, row=6, pady=20)

# Set the default value of the combo box to the first key of ragas_index
if ragas_index:  # Check if ragas_index is not empty
    raga_var.set(list(ragas_index.keys())[0])

# Function to update score_text based on raga selection
def update_score_text(event):
    # Get the selected raga
    selected_raga = raga_var.get()
    # Look up the corresponding value in ragas_index
    raga_value = ragas_index.get(selected_raga, '')
    # Clear the current content of score_text
    score_text.delete('1.0', tk.END)
    # Insert the new raga value
    score_text.insert(tk.END, raga_value)

# Bind the update function to the ComboBox selection event
raga_combo.bind('<<ComboboxSelected>>', update_score_text)

# # Desired window size
# window_width = 600
# window_height = 400

# # Get screen width and height
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Calculate x and y coordinates
# x = (screen_width / 2) - (window_width / 2) + 150
# y = (screen_height / 2) - (window_height / 2) 

# # Set the window's geometry
# root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))


root.mainloop()