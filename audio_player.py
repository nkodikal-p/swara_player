from midiutil import MIDIFile
from constants import sargam, midi_program
import pygame
import tkinter as tk    
from tkinter import messagebox
import os 
import tempfile
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

def play_score(score, taal, bpm, metronome, instrument):
    # Create a new MIDI file with 2 tracks
    # check if midiutil is installed
    try:
        midi = MIDIFile(2)
    except Exception as e:
        messagebox.showwarning("MIDIUtil not installed", f'Please install MIDIUtil: pip install MIDIUtil')
        return

    # Split the score by spaces and create a list of lists
    elements = score.split()
    notes = [[element, 1] for element in elements] # " S R,G" --> [['S',1],['R,G',1]] --> S 1 beat, R+G 1 beat

    notes_beats = []
    # for multi-notes in one beat, split note on ',' and subdivide duration equally per split 
    #  [['S',1],['R,G',1]] turns into [['S',1],['R',0.5],['G',0.5]] --> S 1 beat, R&G 1/2 beat
    for note in notes:
        elements = note[0].split(',') #
        duration = note[1] / len(elements)
        for element in elements:
            notes_beats.append([element, duration])


    # midi.addprogramchange(track, channel, time, program)
    # Add instrument sound
    midi.addProgramChange(0, 0, 0, midi_program[instrument])

    # iterate through notes_beats
    timer = 0
    for note in notes_beats:
        # addNote(track, channel, pitch, time, duration, volume)
        if sargam[note[0]] != 21: 
            midi.addNote(0, 0, sargam[note[0]], timer , 60/bpm*note[1], 100) # vol 100 if note is not 21 (rest)
        else:
            midi.addNote(0, 0, sargam[note[0]], timer , 60/bpm*note[1], 1) # vol 100 if note is 21 (rest)
        timer += note[1]*60/bpm

    # Add metronome
    midi.addProgramChange(0, 1, 0, 115)
    if metronome == 1:
        for i in range(len(notes)):
            if i % taal == 0:   # woodblock clap every 4th beat (if taal = 4)
                midi.addNote(1, 1, 60, i*60/bpm , 1.0, 120)
        


    # Write MIDI file in temp directory
    with tempfile.NamedTemporaryFile(delete=False) as output_file:
        midi.writeFile(output_file)

    # Check if pygame is installed
    try:
        # Play MIDI file
        pygame.mixer.init()
        pygame.mixer.music.load(output_file.name)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.wait(1000)
    except Exception as e:
        messagebox.showwarning("Pygame not installed", f'Please install Pygame: pip install pygame')
        return

    
    # Delete the MIDI file
    os.remove(output_file.name)

# function to get values from GUI and play audio 
def play(score_text, taal_var, bpm_var, metronome_var, instrument_var):
    score = score_text.get("1.0", "end-1c")
    try:
        taal = int(taal_var.get())
        bpm = int(bpm_var.get())  # Get the bpm value from the bpm_entry widget
    except Exception as e:
        messagebox.showwarning("Invalid taal", f'Please add a number for Taal/BPM')
    metronome = metronome_var.get()
    instrument = instrument_var.get()
    try:
        play_score(score, taal, bpm, metronome, instrument)
    except Exception as e:
        messagebox.showwarning("Invalid note", f'You entered an invalid note, {str(e)}')

