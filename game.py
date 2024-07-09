from constants import beginner_swaras, intermediate_swaras, advanced_swaras
from audio_player import play_score
import os 
from points import points_file, read_or_initialize_points, update_points
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


def play_game():
    print("\n")
    print("Welcome to Name that Swara!\n")
    mode = input("Novice (0) Beginner (1), Intermediate (2), or Advanced mode (3): ")
    # ensure user entered 1 or 2 
    while (mode != '0') and (mode != '1') and (mode != '2') and (mode != '3'):
        mode = input("Enter only 1, 2, or 3!: ")
    print("")
    if mode == '0' or mode == '1':
        swaras = beginner_swaras
    elif mode == '2'    :
        swaras = intermediate_swaras
    else:
        swaras = advanced_swaras

    # function to generate 3 - 5 random swaras
    def generate_score(swaras, mode):
        import random
        if mode == '0':
            score = random.sample(swaras, 1) # return just 1 random swara
        else:
            score = random.sample(swaras, random.randint(2,int(mode)+2)) # random number of swaras between depending on mode (higher mode = more swaras)
        # add 'S' as first item in score list
        score.insert(0, 'S')
        # add '-' as last item in score list
        score.append('-')
        #print(score)
        return ' '.join(score)

    
    gamepoints=0 # initial gamepoints for score keeping
    points_dict = read_or_initialize_points(points_file) # read points from file
    onaroll = 0 # initial onaroll counter
    while True:
        score = generate_score(swaras, mode)
        play_score(score, 4, 35, 0, 'piano')
        if mode == '0' or mode == '1': 
            guess = input("Enter swaras separated by spaces (enter to hear again) : ")
            while guess == "": # repeat the audio for beginner mode only
                play_score(score, 4, 35, 0, 'piano')
                guess = input("Enter swaras separated by spaces (enter to hear again) : ")
            print("")
        else:
            guess = input("Enter swaras separated by spaces : ")

        # Calculate score
        if guess == score[:-2]: # remove last ' -' from score
            # count of characters without spaces
            gamepoints += len(guess.replace(" ", ""))*10 # 10 points per correct character
            print(f"Correct! Score={gamepoints}")
            onaroll += 1
            if onaroll == 5:
                gamepoints += 200 # grant extra points for 5 correct in a row
                print("Five correct in a row! You're on a roll! +200 points")
                onaroll = 0 # reset onaroll counter

        else:
            onaroll = 0 # reset onaroll counter
            print("Incorrect! The correct answer is: ", score[:-2])
            # count how many characters were guessed correctly
            same_chars = sum([1 for char in guess.replace(" ", "") if char in score.replace(" ", "")])
            gamepoints += same_chars*10 # 10 points per correct character
            print(f'{same_chars}/{len(guess.replace(" ", ""))} swaras were correct. Score = {gamepoints}')
        print("")
        play = input("Press Enter to play again or 'q' to quit: ")
        if play == 'q':
            points_dict['run_total_score']  += gamepoints
            
            print("")
            print("Thanks for playing Name that Swara!")
            print("")
            # check if gamepoints > highscore
            if gamepoints > points_dict['game_high_score']:
                points_dict['game_high_score'] = gamepoints
                print("New high score!")
            print(f"Score for this game {gamepoints}. \nHighest game score {points_dict['game_high_score']}.\nRunning total score {points_dict['run_total_score']}.")
            print("")

            update_points(points_file,points_dict) # update points in file
            
            return None
