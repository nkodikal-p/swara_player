# swara_player
Simple Python app for training yourself to identify swaras in Hindustani Classical Music
![image](https://github.com/nkodikal-p/swara_player/assets/174972654/f45d4490-4d12-46a7-9e9c-0945dabfe55b)

Enter swaras in the text box and press Play to hear the audio. Example swaras can be filled by selecting a raga from the combo-box as show in the above snip.
Syntax for swaras: 
```
S   Shadja (Sa)    
r   Komal Rishabh (Re)    
R   Shuddha Rishabh (Re)    
g   Komal Gandhar (Ga)    
G   Shuddha Gandhar (Ga)    
m   Shuddha Madhyam (Ma)    
M   Teevra Madhyam (Ma)    
P   Pancham (Pa)    
d   Komal Dhaivat (Dha)    
D   Shuddha Dhaivat (Dha)    
n   Komal Nishad (Ni)    
N   Shuddha Nishad (Ni)    
-   One beat rest.  
,   Combine notes in one beat
    R,G = 1/2 beat R + 1/2 beat G
_N  Lower octave Ni. 
    Any note preceded by _ is a lower octave note.
S_  Higher octave Sa. 
    Any note followed by _ is a higher octave note.

    Example score you can enter: 
    S G P - R,G R S 
    S, G, P 1 beat each
    - one beat rest
    R,G half beat each
```
## Taal
When the Metrnonome is switched On, a _Click_ will be heard every _Taal_ beats. 
For example, if Taal is entered as 4, a click will be heard every 4th swara beat.

## Play Game
A command-line interface game to train your ears to identify swaras. 
User picks a level (Novice/Beginner/Intermediate/Advanced). A series of swaras will be heard (the first note is always _S_). The goal is to identify the notes correctly. Each correct note will earn 10 points. 
```
Welcome to Name that Swara!

Novice (0) Beginner (1), Intermediate (2), or Advanced mode (3): 1

Enter swaras separated by spaces (enter to hear again) : S S R

Correct! Score=30

Press Enter to play again or 'q' to quit:
Enter swaras separated by spaces (enter to hear again) : S D P

Correct! Score=60

Press Enter to play again or 'q' to quit: q

Thanks for playing Name that Swara!
Score for this game 60. Running total score 4040


```

### Dependencies
Needs `pygame` and `midiutils` to be installed. 
To install these modules, type  `pip install pygame` and `pip install MIDIUtil`. 
