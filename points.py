import os 
import tempfile
import json

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Get the path to the Windows temporary directory
temp_dir = tempfile.gettempdir()
points_file = os.path.join(temp_dir,"swara_player_points.json")
# read running points from points_file if it exists

# Function to read or initialize points

def read_or_initialize_points(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # File exists, read the points
        with open(file_path, 'r') as file:
            try:
                points_dict = json.load(file)
            except ValueError:
                # Handle case where file contains invalid JSON
                points_dict = {"game_high_score": 0,"run_total_score": 0}
    else:
        # File does not exist, create it and initialize points to 0
        points_dict = {"game_high_score": 0,"run_total_score": 0}
        with open(file_path, 'w') as file:
            json.dump(points_dict, file)
    return points_dict

# function to update points
def update_points(file_path, points_dict):
    with open(file_path, 'w') as file:
        json.dump(points_dict, file)
