import os 
import tempfile
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Get the path to the Windows temporary directory
temp_dir = tempfile.gettempdir()
points_file = os.path.join(temp_dir,"swara_player_points.txt")
# read running points from points_file if it exists

# Function to read or initialize points
def read_or_initialize_points(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # File exists, read the points
        with open(file_path, 'r') as file:
            try:
                points = int(file.read())
            except ValueError:
                # Handle case where file is empty or contains invalid data
                points = 0
    else:
        # File does not exist, create it and initialize points to 0
        with open(file_path, 'w') as file:
            points = 0
            file.write(str(points))
    return points

# function to update points
def update_points(file_path, points):
    with open(file_path, 'w') as file:
        file.write(str(points))
