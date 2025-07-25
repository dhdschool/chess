import chess
import chess.svg as vis
from abc import ABC
from random import choice
from typing import Generator, Any


    

class Bot(ABC):
    def __init__(self):
        pass
    
    def move(self, board):
        pass 

class RandomBot(Bot):
    def __init__(self):
        super().__init__()
        
    def move(self, board):
        moves = list(board.generate_legal_moves())
        move = choice(moves)
        board.push(move)
        
class MinimaxBot(Bot):
    def __init__(self, eval_fn, depth=3, is_white=True):
        super().__init__()
        
        self.depth = depth
        self.eval_fn = eval_fn
        
    def move(self, board: chess.Board):
        current_board = board.copy()
        best_move = self.find_best_move(current_board)
        board.push(best_move)
    
    def find_best_move(self, board):
        pass
        
    
class Person(Bot):
    def __init__(self):
        super().__init__()
        
    def move(self, board):  
        legal_moves = list(board.generate_legal_moves())
        print(legal_moves)
        
        move = chess.Move.from_uci(input("Please enter your move: "))
        while(move not in legal_moves):
            move = chess.Move.from_uci(input("Please enter your move: "))
            print("Illegal move detected, please, play a legal move...\n")
        
        board.push(move)

def save_board(board: chess.Board, fp="pictures/white.svg"):
    picture = vis.board(board=board)
    
    with open(fp, 'w') as file:
        file.write(picture)

def game(board: chess.Board, white: Bot, black: Bot) -> Generator[chess.Board, Any, None]:
    while not our_board.is_checkmate():
        print(f"Board points: {naive_points(our_board)}")
        white.move(our_board)
        yield board
        
        if not our_board.is_checkmate():
            print(f"Board points: {naive_points(our_board)}")
            black.move(our_board)
            yield board

if __name__ == '__main__':
    white = Person()
    black = RandomBot()
    
    our_board = chess.Board()
    our_game = game(our_board, white, black)
    for next_board in our_game:
        save_board(next_board, fp="pictures/game.svg")

    print(naive_points(our_board))
    
    
    
    

