def load_map(file_path):
    # Load the map from the input file
    with open(file_path, 'r') as file:
        # Read the size of the map
        n, m = map(int, file.readline().split())

        # Read the map matrix
        map_matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))
            map_matrix.append(row)

        # Read the obstacle positions
        obstacles = []
        for _ in range(4):
            top, left, bottom, right = map(int, file.readline().split())
            obstacles.append((top, left, bottom, right))

    return n, m, map_matrix, obstacles

def save_result(file_path, result_map, path_length, game_point):
    # Save the result map to the output file
    with open(file_path, 'w') as file:
        # Write the result map
        for row in result_map:
            file.write(' '.join(map(str, row)) + '\n')

        # Write the path length and game point
        file.write(f"Path Length: {path_length}\n")
        file.write(f"Game Point: {game_point}\n")

# Main function
def main():
    # Load the map from the input file
    file_path = 'map1.txt'  # Replace with the actual file path
    n, m, map_matrix, obstacles = load_map(file_path)

    # Perform the Hide and Seek game logic here
    # ...

    # Save the result map to the output file
    result_file_path = 'result1.txt'  # Replace with the actual file path
    save_result(result_file_path, result_map, path_length, game_point)

if __name__ == '__main__':
    main()
    # Define the Map class
    class Map:
        def __init__(self, n, m, map_matrix):
            self.n = n
            self.m = m
            self.map_matrix = map_matrix

    # Define the Agent class
    class Agent:
        def __init__(self, position):
            self.position = position

    # Define the Obstacle class
    class Obstacle:
        def __init__(self, top, left, bottom, right):
            self.top = top
            self.left = left
            self.bottom = bottom
            self.right = right

    # Create an instance of the Map class
    map_obj = Map(n, m, map_matrix)

    # Create an instance of the Agent class
    agent_obj = Agent((0, 0))  # Replace with the actual starting position

    # Create a list of Obstacle objects
    obstacles_obj = []
    for obstacle in obstacles:
        obstacles_obj.append(Obstacle(*obstacle))