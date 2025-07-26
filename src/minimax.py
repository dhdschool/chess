import chess

def naive_points(board: chess.Board):
    points = {
        chess.QUEEN:9,
        chess.ROOK:5,
        chess.BISHOP:3,
        chess.KNIGHT:3,
        chess.PAWN:1,
        chess.KING:0
    }
    
    if board.is_checkmate() and board.turn == chess.WHITE:
        return -1000
    
    elif board.is_checkmate() and board.turn == chess.BLACK:
        return 1000

    elif board.is_stalemate():
        return 0
    
    
    white_score = 0
    black_score = 0
    for type in chess.PIECE_TYPES:
        #board.pieces()
        white_pieces = board.pieces(
            piece_type=type,
            color = chess.WHITE
        )
        
        black_pieces = board.pieces(
            piece_type=type,
            color = chess.BLACK
        )
        
        white_score += len(white_pieces) * points[type]
        black_score += len(black_pieces) * points[type]
    
    return white_score - black_score

class Node:
    def __init__(self, chess_board: chess.Board):
        self.parent = None
        self.board = chess_board
        self.depth = 0  
      
        self.children = []
        self.score = naive_points(self.board)
    
    def adopt_child(self, node):
        self.children.append(node)
        node.parent = self
        node.depth = self.depth + 1

class Tree:
    def __init__(self, 
                 initial_board: chess.Board, 
                 max_depth: int=3):
        self.alpha = float('-inf')
        self.beta = float('inf')
        self.max_depth = max_depth
        
        root_boards = [initial_board.copy().push(move) for move in initial_board.legal_moves]
        self.root_nodes = [Node(x) for x in root_boards]
        
        is_white = initial_board.turn == chess.WHITE
        
        scores = [self.generate_tree(node, is_white=is_white) for node in self.root_nodes]
        self.optimal_value = min(scores) if not is_white else max(scores)
        self.optimal_move = initial_board.legal_moves[scores.index(self.optimal_value)]
            
    def generate_tree(self, node: Node, depth:int=0, is_white:bool =True) -> None:
        if depth > self.max_depth:
            if is_white: self.alpha = max(self.alpha, node.score)
            else: self.beta = min(self.beta, node.score)
            return node.score
        
        if is_white and node.score > self.beta: return node.score
        elif not is_white and node.score < self.alpha: return node.score
        
        board_copys = [node.board.copy().push(move) for move in node.board.legal_moves]
        [node.adopt_child(Node(board)) for board in board_copys]
        
        scores = [self.generate_tree(child, depth+1, not is_white) for child in node.children]
        if is_white: return max(scores)
        else: return min(scores)