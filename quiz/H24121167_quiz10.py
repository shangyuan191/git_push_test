import os
import random
import time
from collections import deque

# Helper functions
def get_key():
    import termios, sys, tty
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def generate_food_pos(obstacles, snake, existing_food_pos=None):
    while True:
        food_pos = (random.randint(0, height - 1), random.randint(0, width - 1))
        if food_pos not in snake and food_pos not in obstacles and food_pos != existing_food_pos:
            return food_pos

def move_snake(snake, direction):
    head = snake[-1]
    if direction == 'up':
        new_head = (head[0] - 1, head[1])
        if new_head[0] < 0:
            new_head = (height - 1, new_head[1])
    elif direction == 'down':
        new_head = (head[0] + 1, head[1])
        if new_head[0] >= height:
            new_head = (0, new_head[1])
    elif direction == 'left':
        new_head = (head[0], head[1] - 1)
        if new_head[1] < 0:
            new_head = (new_head[0], width - 1)
    else:
        new_head = (head[0], head[1] + 1)
        if new_head[1] >= width:
            new_head = (new_head[0], 0)
    snake.append(new_head)
    return new_head

# Initialize game settings
normal_food_symbol = 'π'
special_food_symbol = 'X'
obstacle_symbol = '█'
snake_symbol = '■'
empty_symbol = ' '

# Get terminal size
terminal_size = os.get_terminal_size()
width = terminal_size.columns
height = terminal_size.lines - 2  # Leave space for the score line

# Initialize game state
snake = deque([(height // 2, width // 4 + i) for i in range(3)])  # Initial snake length = 3
direction = 'right'
speed = 0.2  # Initial speed
is_paused = False
normal_food_count = 0
special_food_count = 0
game_over = False

# Generate obstacles
obstacles = []
obstacle_count = int(width * height * 0.05)  # 5% of the game screen
for _ in range(obstacle_count):
    obstacle_length = random.randint(5, 10)
    orientation = random.choice(['horizontal', 'vertical'])
    if orientation == 'horizontal':
        start_x = random.randint(0, width - obstacle_length)
        start_y = random.randint(0, height - 1)
        obstacles.extend([(start_y, start_x + i) for i in range(obstacle_length)])
    else:
        start_x = random.randint(0, width - 1)
        start_y = random.randint(0, height - obstacle_length)
        obstacles.extend([(start_y + i, start_x) for i in range(obstacle_length)])

# Generate initial food positions
normal_food_pos =generate_food_pos(obstacles, snake)
special_food_pos =generate_food_pos(obstacles, snake, normal_food_pos)

# Game loop
while not game_over:
    # Handle user input
    key = get_key()
    if key == 'q':
        break
    elif key == ' ':
        is_paused = not is_paused
    elif not is_paused:
        if key == 'w' and direction != 'down':
            direction = 'up'
        elif key == 's' and direction != 'up':
            direction = 'down'
        elif key == 'a' and direction != 'right':
            direction = 'left'
        elif key == 'd' and direction != 'left':
            direction = 'right'

    if not is_paused:
        # Move the snake
        new_head = move_snake(snake, direction)

        # Check for collisions
        if new_head in snake or new_head in obstacles:
            game_over = True
        elif new_head == normal_food_pos:
            snake.append(new_head)
            normal_food_count += 1
            normal_food_pos = generate_food_pos(obstacles, snake)
        elif new_head == special_food_pos:
            if len(snake) > 1:
                snake.popleft()
            special_food_count += 1
            special_food_pos = generate_food_pos(obstacles, snake, normal_food_pos)

        # Accelerate snake movement
        speed *= 0.99

    # Clear the screen
    os.system('clear' if os.name == 'posix' else 'cls')

    # Draw the game screen
    for y in range(height):
        for x in range(width):
            if (y, x) in snake:
                print(snake_symbol, end='')
            elif (y, x) == normal_food_pos:
                print(normal_food_symbol, end='')
            elif (y, x) == special_food_pos:
                print(special_food_symbol, end='')
            elif (y, x) in obstacles:
                print(obstacle_symbol, end='', bg='red')
            else:
                print(empty_symbol, end='')
        print()

    # Print score
    print(f"Normal food eaten: {normal_food_count}, Special food eaten: {special_food_count}")

    # Pause if needed
    if is_paused:
        print("Game paused. Press space to resume.")
    else:
        time.sleep(speed)

# Game over
if game_over:
    print("Game Over!")
    if new_head in snake:
        print("You collided with yourself.")
    else:
        print("You collided with an obstacle.")
else:
    print("You quit the game.")
print(f"Final score: Normal food eaten: {normal_food_count}, Special food eaten: {special_food_count}")
