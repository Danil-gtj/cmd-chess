from cmd_chess import save 
import random
import time
import os 
import sys

chess_board = {
    "A8": "♜", "B8": "♞", "C8": "♝", "D8": "♛", "E8": "♚", "F8": "♝", "G8": "♞", "H8": "♜", 
    "A7": "♟", "B7": "♟", "C7": "♟", "D7": "♟", "E7": "♟",  "F7": "♟", "G7": "♟", "H7": "♟", 
    "A6": "", "B6": "", "C6": "", "D6": "","E6": "",  "F6": "", "G6": "", "H6": "", 
    "A5": "", "B5": "", "C5": "", "D5": "","E5": "",  "F5": "", "G5": "", "H5": "", 
    "A4": "", "B4": "", "C4": "", "D4": "","E4": "",  "F4": "", "G4": "", "H4": "", 
    "A3": "", "B3": "", "C3": "", "D3": "","E3": "",  "F3": "", "G3": "", "H3": "", 
    "A2": "♙", "B2": "♙", "C2": "♙", "D2": "♙","E2": "♙",  "F2": "♙", "G2": "♙", "H2": "♙", 
    "A1": "♖", "B1": "♘", "C1": "♗", "D1": "♕","E1": "♔",  "F1": "♗", "G1": "♘", "H1": "♖" 
}

ascii_pieces = {
    "♜": "R", "♞": "N", "♝": "B", "♛": "Q", "♚": "K", "♟": "P",
    "♖": "r", "♘": "n", "♗": "b", "♕": "q", "♔": "k", "♙": "p"
}

USE_ASCII = sys.stdout.encoding.lower() != 'utf-8'

def getCoords(pos):
    files = "ABCDEFGH"
    column = files.index(pos[0].upper())
    row = 8 - int(pos[1])
    return row, column 

def isPathClear(board, start_coords, end_coords):
    row_start, column_start = start_coords
    row_end, column_end = end_coords
    
    dist_row = 0 if row_start == row_end else (1 if row_end > row_start else -1)
    dist_column = 0 if column_start == column_end else (1 if column_end > column_start else -1)
    
    curr_r, curr_c = row_start + dist_row, column_start + dist_column
    while (curr_r, curr_c) != (row_end, column_end):
        pos_key = f"{'ABCDEFGH'[curr_c]}{8 - curr_r}"
        if board.get(pos_key, "") != "":
            return False
        curr_r += dist_row
        curr_c += dist_column
    return True

def canMove(board, start_pos, end_pos):
    piece = board.get(start_pos, "")
    if not piece: return False

    row_start, column_start = getCoords(start_pos)
    row_end, column_end = getCoords(end_pos)

    dist_row = abs(row_start - row_end)
    dist_column = abs(column_start - column_end)

    target_piece = board.get(end_pos, "")
    white_pieces = "♙♘♗♖♕♔"

    if target_piece:
        is_piece_white = piece in white_pieces
        is_target_white = target_piece in white_pieces
        if is_piece_white == is_target_white:
            return False

    match piece:
        case "♙" | "♟":
            is_white = piece == "♙"
            direction = -1 if is_white else 1
            start_row_pos = 6 if is_white else 1
            
            if dist_column == 0 and (row_end - row_start) == direction:
                return target_piece == ""
            if dist_column == 0 and row_start == start_row_pos and (row_end - row_start) == 2 * direction:
                mid_row = row_start + direction
                mid_pos = f"{'ABCDEFGH'[column_start]}{8 - mid_row}"
                return target_piece == "" and board.get(mid_pos, "") == "" 
            if dist_column == 1 and (row_end - row_start) == direction:
                return target_piece != ""
        case "♕" | "♛":
            if row_start == row_end or column_start == column_end or dist_row == dist_column:
                return isPathClear(board, (row_start, column_start), (row_end, column_end))
        case "♔" | "♚":
            return dist_row <= 1 and dist_column <= 1
        case "♘" | "♞":
            return (dist_row == 1 and dist_column == 2) or (dist_row == 2 and dist_column == 1)
        case "♗" | "♝":
            if dist_row == dist_column:
                return isPathClear(board, (row_start, column_start), (row_end, column_end))
        case "♖" | "♜":
            if row_start == row_end or column_start == column_end:
                return isPathClear(board, (row_start, column_start), (row_end, column_end))
    return False


def findKing(board, color):
    king_symbol = "♔" if color == 'white' else "♚"
    for pos, piece in board.items():
        if piece == king_symbol:
            return pos
    return None

def is_check(board, color):
    king_pos = findKing(board, color)
    if not king_pos: return False 

    enemy_color = 'black' if color == 'white' else 'white'
    for pos, piece in board.items():
        if piece == "": continue
        
        is_enemy = (enemy_color == 'black' and piece in "♟♞♝♜♛♚") or \
                   (enemy_color == 'white' and piece in "♙♘♗♖♕♔")
        
        if is_enemy:
            if canMove(board, pos, king_pos):
                return True
    return False

def is_safe_move(board, start_pos, end_pos, color):
    if not canMove(board, start_pos, end_pos):
        return False
    
    temp_board = board.copy()
    temp_board[end_pos] = temp_board[start_pos]
    temp_board[start_pos] = ""
    
    return not is_check(temp_board, color)

def getAllLegalMoves(board, color):
    moves = []
    for start_pos, piece in board.items():
        if piece == "": continue
        
        is_black = piece in "♟♞♝♜♛♚"
        is_white = piece in "♙♘♗♖♕♔"
        
        if (color == 'black' and is_black) or (color == 'white' and is_white):
            for r in range(1, 9):
                for f in "ABCDEFGH":
                    end_pos = f"{f}{r}"
                    if is_safe_move(board, start_pos, end_pos, color):
                        moves.append((start_pos, end_pos))
    return moves

def check_game_status(board, color):
    legal_moves = getAllLegalMoves(board, color)
    
    if not legal_moves:
        if is_check(board, color):
            return "CHECKMATE"
        else:
            return "STALEMATE" 
    return "IN_PROGRESS"

def evaluateBoard(board):
    weights = {'♙': 100, '♘': 300, '♗': 300, '♖': 500, '♕': 900, '♔': 9000,
               '♟': -100, '♞': -300, '♝': -300, '♜': -500, '♛': -900, '♚': -9000}
    
    center_squares = ["D4", "E4", "D5", "E5"]
    middle_squares = ["C3", "D3", "E3", "F3", "C4", "F4", "C5", "F5", "C6", "D6", "E6", "F6"]

    score = 0
    for pos, piece in board.items():
        if piece:
            piece_val = weights.get(piece, 0)
            pos_bonus = 0
            if piece not in ["♔", "♚", "♖", "♜"]: 
                if pos in center_squares: pos_bonus = 15
                elif pos in middle_squares: pos_bonus = 5

            if piece in "♟♞♝♜♛♚":
                score += (piece_val - pos_bonus)
            else:
                score += (piece_val + pos_bonus)
    return score

def aiMove():
    legal_moves = getAllLegalMoves(chess_board, 'black')
    
    if not legal_moves:
        return False 

    best_moves = []
    best_value = 99999 

    for move in legal_moves:
        start, end = move
        temp_board = chess_board.copy()
        temp_board[end] = temp_board[start]
        temp_board[start] = ""
        
        board_value = evaluateBoard(temp_board)
        
        if board_value < best_value:
            best_value = board_value
            best_moves = [move] 
        elif board_value == best_value:
            best_moves.append(move) 

    if best_moves:
        s, e = random.choice(best_moves)
        print(f"AI move: {s} -> {e}")
        chess_board[e] = chess_board[s]
        chess_board[s] = ""
        return True


def ChessBoardPrint():
    board_numbers = "87654321"
    board_latters = "ABCDEFGH"

    print("   _________________")
    for number in board_numbers:
        row_str = f"{number} |"
        for latter in board_latters:
            cell = latter + number
            piece = chess_board.get(cell,"")
            
            if piece == "":
                display_piece = "."
            else:
                display_piece = ascii_pieces.get(piece, piece) if USE_ASCII else piece
            row_str += f" {display_piece}"
        print (f"{row_str} |")
    print("  |-----------------|")
    print("  | A B C D E F G H |")
    print("  |_________________|")

def StartPlay():
    while True:
        ChessBoardPrint()
        
        status = check_game_status(chess_board, 'white')
        if status == "CHECKMATE":
            print("\n*** MATE! You Lose! ***\n")
            break
        elif status == "STALEMATE":
            print("\n*** CHECK! Draw! ***\n")
            break
            
        if is_check(chess_board, 'white'):
            print("Warning: YOU KING IS IN CHECK!")

        print("Witch figure move? (or exit)")
        start_pos = input().strip().upper()
        if start_pos == "EXIT": break

        print("Where it move?")
        end_pos = input().strip().upper()

        print(21*"-")
        
        piece = chess_board.get(start_pos, "")
        if piece in "♙♘♗♖♕♔" and is_safe_move(chess_board, start_pos, end_pos, 'white'):
            chess_board[end_pos] = chess_board[start_pos]
            chess_board[start_pos] = ""
            
            ChessBoardPrint()
            
            ai_status = check_game_status(chess_board, 'black')
            if ai_status == "CHECKMATE":
                print("\n*** MATE! AI Won! ***\n")
                break
            elif ai_status == "STALEMATE":
                print("\n*** CHECK! Draw! ***\n")
                break
                
            print("AI thinks...")
            time.sleep(1)
            aiMove()
        else:
            print("!----- Illigal move (or your king under attack! ) -----!")
            time.sleep(1)

def MainGame():
    global USE_ASCII
    if os.name == 'nt':
        os.system('chcp 65001 > nul')

    print("  -----CMD-CHESS-----")

    while True:
        ChessBoardPrint()
        print("Start play: 1")
        print("Save game: 2")
        print("Load game: 3")
        print("Toggle Graphiscs: 4")
        print("Exit: 0")
        print(21*"-")

        user_choose = input("Your choose: ")

        try:
            choice = int(user_choose)
        except ValueError:
            print(21*"-")
            print("!!!Invalid choose!!!")
            continue

        match choice:
            case 1:
                StartPlay()
            case 2:
                save.SaveGame(chess_board)
            case 3:
                save.LoadGame(chess_board)
            case 4:
                USE_ASCII = not USE_ASCII
                print(f"Switched to {'ASCII' if USE_ASCII else 'Unicode'} mode!")
            case 0:
                break
            case _:
                print(21*"-")
                print("Invalid action!")

if __name__ == "__main__":
    MainGame()