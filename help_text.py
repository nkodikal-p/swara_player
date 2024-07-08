import tkinter as tk
import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


ragas_index = {'Adana' : 'S R m P d n S_ - S_ d n P - m P g m R S',

    'Bahar' : 'S m - P m g m - n P m - m n D N S_ - n P m - P m - g m R S -',

    'Basant' : 'S G M d N S_ - S_ N d P M G M N d M G r S',

    'Bhairav' : 'S r G m P d N S_ - S_ N d P m G r S -',

    'Bihag' : 'S G m P N S_ - S_ N D,P M P G m G R,S - S_ N D P M G m G R S',

    'Bhoopali' : 'S R G P D S_ - S_ D P G R S',

    'Bageshree' : 'S g m D n S_ - S_ n D m P D g m g R S',

    'Khamaaj' : 'S G m P D N S_ - S_ n D P m G R G S - _N S G m P',

    'Durga' : 'S R m P D S_ - S_ D P D m R S - D S',

    'Yaman' : '- _N R S - _N R G M P D N S_ - S_ N D P M G R S -  _N R S',

    'Bhimpalasi' : '- _n S g m P n S_ - S_ n D P m g R S - _n S - P - _n S',

    'Kafi' : 'S R g m P D n S_ - - S_ n D P m g R S -',

    'Jaijaivanti' : 'S - D - n R - R g R S - G m P m G R - R m P N S_ - S_ n D P m G R g R S - - N S - D - n R S',

    'Bihag' : 'S G m P N S_ - S_ N DP M P G m G RS - S_ N D P M G m G R S',

    'Desh' : 'S R m P N S_ - S_ n D P D m G R G - N S',

    'Deskhar' : 'S R G P D S_ - S_ D P D G P G R S',

    'Tilak Kamod' : '- P - N S R G S - S R m P N S_ - S_ P D m G S R G S - N - P - N S R G S',

    'Kedar' : 'S M P D N S_ - - S_ N D P - M P D P - m m R S  -',

    'Marwa' : 'S - D - N r G M D N S_ - - S_ N D M G r S - - N - D S - N r S -',

    'Puriya' : '- _N r G M D N S_ - - S_ N D M - G M D - G M G r S -',

    'Puriya Dhanashree' : '- _N r S - - _N r G M P - M d N S_ - S_ N d P M G M r G r S',

    'Bilaskhani Todi' : 'S r g P d S_ - S_ r_ n d - P - P d n d m g r - r g r S',

    'Gurjari Todi' : 'S r g M d N S_ - S_ N d M d M g r g r S  - - d - N S',

    'Bhinna Shadja' : 'S G m D N S_ - - S_ N D m G S -',

    'Sohani' : 'S G M D N S_ - - S_ N D N D M G r S -',

    'Chandrakauns' : 'S g m d N S_ - S_ N d m g m g S - N S',

    'Charukeshi' : 'S R G m P d n S_ - S_ n d P m G R S - d - n S',

    'Darbari Kanada' : 'S R g m P d n S_ - S_ d n P m P g m R S',

    'Hameer' : 'S G m N D P - G m D N S_ - S_ N D P M P D P G m P G m R S -',

    'Jaunpuri' : 'S R m P d n S_ - S_ n d P m g R S',

    'Jog' : 'S G m P n S_ - - S_ n P m g S - n S -',

    'Kirwani' : 'S R g m P d N S_ - - S_ N d P m g R S -',

    'Komal Rishabh Asavari' : 'S r m P d S_ - - S_ r_ n d m P d m g r g r - n -  d r S -',

    'Lalit' : '- N r G M d N S_ - - S_ N d - M d M m - G M G r S -',

    'Madhuvanti' : '- _N S g M P N S_ - - S_ N D P M g M g R S - _N S -',

    'Madhmad Saarang' : '- n S - R m P n S_ - - S_ n P m R S -',

    'Miya Malhar' : '- N S - m R P - g m R S - m R P n D N S_ - - S_ n D n P - m P g g m R S -',

    'Malkauns' : 'S g m d n S_ - - S_ n d m g S -',

    'Maru Bihag' : 'S G M P N S_ - - S_ N D P M G M G R S -',

    'Megh or Megh Malhar' : 'S (m)R m P - n S_ - - S_ n P m R S - R - n S -',

    'Multani' : '- N S g M P N S_ - - S_ N d P M g r S -',

    'Patdeep' : '- N S g m P N S_ - - S_ N D P m g R S - N S -',

    'Puriya Kalyan' : 'S r G M P D N S_ - S_ N D P M G r G r S',

    'Brindavani Sarang' : 'S R m P N S_ - S_ n P m R S - N S',

    'Shankara' : 'S G P N D S_ - S_ N P G - P D P G - P R,G R,S',

    'Shree' : 'S r M P N S_ - S_ r_ N d P M P d M G r S',

    'Shuddha Kalyan' : 'S R G P D S_ - S_ N D P M G R S - G R G P R S',

    'Shuddha Sarang' :'- N S R M P N S_ - S _ N D P M P M m R S - N S',

    'Shyam Kalyan' : '- N S R M P N S_ - - S_ N D P M P D P G m P G m R S - N S -',

    'Sohani' : 'S G M D N S_ - - S_ N D N D M G r S -',

    'Bibhas' : 'S r G P d S_ - S_ d P G r S',
    }


# Help button command
def show_help(root):
    help_text = """
    example score you can enter: 
    S G P - R,G R S 
    S, G, P 1 beat each
    - one beat rest
    R,G half beat each

    #  S   Shadja (Sa)    
    #  r   Komal Rishabh (Re)    
    #  R   Shuddha Rishabh (Re)    
    #  g   Komal Gandhar (Ga)    
    #  G   Shuddha Gandhar (Ga)    
    #  m   Shuddha Madhyam (Ma)    
    #  M   Teevra Madhyam (Ma)    
    #  P   Pancham (Pa)    
    #  d   Komal Dhaivat (Dha)    
    #  D   Shuddha Dhaivat (Dha)    
    #  n   Komal Nishad (Ni)    
    #  N   Shuddha Nishad (Ni)    
    #  -   One beat rest.  
    #  ,   Combine notes in one beat
    #      R,G = 1/2 beat R + 1/2 beat G
    #  _N  Lower octave Ni. 
    #      Any note preceded by _ is a lower octave note.
    #  S_  Higher octave Sa. 
    #      Any note followed by _ is a higher octave note.

    """

    # Create new window
    help_window = tk.Toplevel(root)
    help_window.title("Help")

    # Create text widget
    help_widget = tk.Text(help_window,width=80, height=40, font=('Consolas', 12))
    help_widget.pack(padx=10, pady=10)

    # Insert help text
    help_widget.insert(tk.END, help_text)

