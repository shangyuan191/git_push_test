import random

def generate_maze(N, M):
   """
   Generate a maze map with a clear path from the top-left cell to the bottom-right cell.
   
   Args:
       N (int): Number of rows in the maze
       M (int): Number of columns in the maze
       
   Returns:
       dict: A dictionary representing the maze, where keys are tuples of cell coordinates
             and values are integers representing the cell state (0 for empty, 1 for obstacle,
             2 for path)
   """
   maze = {(i, j): 0 for i in range(N) for j in range(M)}  # Initialize all cells as empty
   
   # Set the starting cell (top-left) and the ending cell (bottom-right) as part of the path
   maze[(0, 0)] = 2
   maze[(N - 1, M - 1)] = 2
   
   # Generate the path from the starting cell to the ending cell
   current_row, current_col = 0, 0
   while current_row < N - 1 or current_col < M - 1:
       if current_row == N - 1:  # If at the last row, move right
           maze[(current_row, current_col + 1)] = 2
           current_col += 1
       elif current_col == M - 1:  # If at the last column, move down
           maze[(current_row + 1, current_col)] = 2
           current_row += 1
       else:  # Choose a random direction (down or right)
           direction = random.choice([(1, 0), (0, 1)])
           next_row, next_col = current_row + direction[0], current_col + direction[1]
           maze[(next_row, next_col)] = 2
           current_row, current_col = next_row, next_col
   
   return maze

def add_obstacles(maze, min_obstacles, N, M):
   """
   Add a minimum number of obstacles randomly into the maze.
   
   Args:
       maze (dict): The maze dictionary
       min_obstacles (int): The minimum number of obstacles to add
       N (int): Number of rows in the maze
       M (int): Number of columns in the maze
       
   Returns:
       None
   """
   # Count the number of empty cells
   empty_cells = [(row, col) for row in range(N) for col in range(M) if maze.get((row, col)) == 0]
   
   # Add obstacles randomly until the minimum number is reached
   num_obstacles = 0
   while num_obstacles < min_obstacles:
       if not empty_cells:
           break  # No more empty cells to add obstacles
       row, col = random.choice(empty_cells)
       maze[(row, col)] = 1
       empty_cells.remove((row, col))
       num_obstacles += 1

def set_obstacle(maze, N, M):
   """
   Set an obstacle at a given coordinate in the maze.
   
   Args:
       maze (dict): The maze dictionary
       N (int): Number of rows in the maze
       M (int): Number of columns in the maze
       
   Returns:
       None
   """
   row = int(input("Enter the row coordinate (0 to {}) for the obstacle: ".format(N - 1)))
   col = int(input("Enter the column coordinate (0 to {}) for the obstacle: ".format(M - 1)))
   
   if row < 0 or row >= N or col < 0 or col >= M:
       print("Error: Coordinates out of bounds.")
       return
   
   if maze.get((row, col)) == 2:
       print("Error: Cannot set an obstacle on the path.")
       return
   
   maze[(row, col)] = 1

def remove_obstacle(maze, N, M):
   """
   Remove an obstacle from a given coordinate in the maze.
   
   Args:
       maze (dict): The maze dictionary
       N (int): Number of rows in the maze
       M (int): Number of columns in the maze
       
   Returns:
       None
   """
   row = int(input("Enter the row coordinate (0 to {}) to remove the obstacle: ".format(N - 1)))
   col = int(input("Enter the column coordinate (0 to {}) to remove the obstacle: ".format(M - 1)))
   
   if row < 0 or row >= N or col < 0 or col >= M:
       print("Error: Coordinates out of bounds.")
       return
   
   if maze.get((row, col)) == 2:
       print("Error: Cannot remove an obstacle from the path.")
       return
   
   if maze.get((row, col)) == 0:
       print("Error: No obstacle at the given coordinates.")
       return
   
   maze[(row, col)] = 0

def print_maze(maze, N, M):
   """
   Print the current state of the maze.
   
   Args:
       maze (dict): The maze dictionary
       N (int): Number of rows in the maze
       M (int): Number of columns in the maze
       
   Returns:
       None
   """
   for row in range(N):
       for col in range(M):
           cell_value = maze.get((row, col))
           if cell_value == 0:
               print(" ", end="")
           elif cell_value == 1:
               print("X", end="")
           else:
               print("O", end="")
       print()
def main():
    try:
        # Read the maze blueprint from the text file
        file_name = input("Enter the name of the file containing the maze blueprint: ")
        with open(file_name, 'r') as file:
            try:
                line = file.readline().strip()
                if not line:
                    raise ValueError("File is empty or invalid.")
                N, M = map(int, line.split())
            except ValueError:
                print("Error: Invalid file format. The first line should contain two integers separated by whitespace.")
                return
            pre_set_obstacles = set()
            for row in range(N):
                line = file.readline().strip()
                for col, char in enumerate(line):
                    if char == 'X':
                        pre_set_obstacles.add((row, col))
    except IOError:
        print("Error: File not found.")
        return

    # 其餘的程式碼保持不變...

   
   # Generate the maze with the pre-set obstacles
   maze = generate_maze(N,M)
   for obstacle in pre_set_obstacles:
       maze[obstacle] = 1
   
   # Ask the user for the minimum number of obstacles to add
   try:
       min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
       if min_obstacles < 0:
           raise ValueError("Minimum number of obstacles must be non-negative.")
   except ValueError as e:
       print(f"Error: {e}")
       return
   
   # Add random obstacles to the maze
   add_obstacles(maze, min_obstacles, N, M)
   
   # Print the initial maze state
   print_maze(maze, N, M)

   while True:
       choice = input("Enter 'set' to set an obstacle, 'remove' to remove an obstacle, or 'exit' to quit: ")
       
       if choice == 'set':
           set_obstacle(maze, N, M)
           print_maze(maze, N, M)
       elif choice == 'remove':
           remove_obstacle(maze, N, M)
           print_maze(maze, N, M)
       elif choice == 'exit':
           break
       else:
           print("Error: Invalid option. Please try again.")

if __name__ == "__main__":
   main()
