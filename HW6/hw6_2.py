import random

class CandyCrush:
    def __init__(self, width, height, candy_types):
        self.width = width
        self.height = height
        self.candy_types = candy_types
        self.board = []
        self.score = 0
        self.moves = 0
        self.max_moves = width * height * 2  # 設定最大移動次數

    def initialize_board(self):
        self.board = [[random.randint(1, self.candy_types) for _ in range(self.width)] for _ in range(self.height)]

    def print_board(self):
        for row in self.board:
            print(' '.join(str(candy).rjust(2) for candy in row))
        print(f"Score: {self.score}")
        print(f"Moves left: {self.max_moves - self.moves}")

    def is_valid_move(self, x1, y1, x2, y2):
        return (abs(x1 - x2) == 1 and y1 == y2) or (abs(y1 - y2) == 1 and x1 == x2)

    def swap_candies(self, x1, y1, x2, y2):
        self.board[y1][x1], self.board[y2][x2] = self.board[y2][x2], self.board[y1][x1]

    def check_and_eliminate(self):
        eliminated = set()
        
        # Check horizontal
        for y in range(self.height):
            for x in range(self.width - 2):
                if self.board[y][x] == self.board[y][x+1] == self.board[y][x+2] != 0:
                    eliminated.update([(x, y), (x+1, y), (x+2, y)])

        # Check vertical
        for x in range(self.width):
            for y in range(self.height - 2):
                if self.board[y][x] == self.board[y+1][x] == self.board[y+2][x] != 0:
                    eliminated.update([(x, y), (x, y+1), (x, y+2)])

        # Eliminate and score
        for x, y in eliminated:
            self.score += self.board[y][x]
            self.board[y][x] = 0

        return len(eliminated) > 0

    def drop_candies(self):
        for x in range(self.width):
            empty = self.height - 1
            for y in range(self.height - 1, -1, -1):
                if self.board[y][x] != 0:
                    self.board[empty][x] = self.board[y][x]
                    empty -= 1
            for y in range(empty, -1, -1):
                self.board[y][x] = random.randint(1, self.candy_types)

    def play(self):
        self.initialize_board()
        while self.moves < self.max_moves:
            self.print_board()
            try:
                x1, y1, x2, y2 = map(int, input("Enter the coordinates to swap (x1 y1 x2 y2): ").split())
                if not (0 <= x1 < self.width and 0 <= y1 < self.height and 
                        0 <= x2 < self.width and 0 <= y2 < self.height):
                    raise ValueError("Coordinates out of range")
                if not self.is_valid_move(x1, y1, x2, y2):
                    raise ValueError("Invalid move")
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue

            self.swap_candies(x1, y1, x2, y2)
            self.moves += 1

            while self.check_and_eliminate():
                self.drop_candies()

            if self.moves >= self.max_moves:
                print("Game Over!")
                self.print_board()
                break

def main():
    print("Welcome to Candy Crush!")
    width = int(input("Enter the width of the board: "))
    height = int(input("Enter the height of the board: "))
    candy_types = int(input("Enter the number of candy types: "))

    game = CandyCrush(width, height, candy_types)
    game.play()

if __name__ == "__main__":
    main()
