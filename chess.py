import save

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
        if board.get(pos_key, ".") != ".":
            return False
        curr_r += dist_row
        curr_c += dist_column
    return True

def canMove(start_pos, end_pos):
    piece = chess_board.get(start_pos, "")
    if not piece: return False

    row_start, column_start = getCoords(start_pos)
    row_end, column_end = getCoords(end_pos)

    dist_row = abs(row_start - row_end)
    dist_column = abs(column_start - column_end)

    target_piece = chess_board.get(end_pos, "")
    if target_piece and piece.isupper() == target_piece.isupper():
        return False
    
    piece = piece.upper()
    match piece:
        case "♙":
            direction = -1
            start_row_pos = 6
            if dist_column == 0 and (row_end - row_start) == direction:
                return target_piece == ""
            
            if dist_column == 0 and row_start == start_row_pos and (row_end - row_start) == 2 * direction:
                mid_row = row_start + direction
                mid_pos = f"{"ABCDEFGH"[column_start]}{8 - mid_row}"
                return target_piece == "" and chess_board.get(mid_pos, "") == "" 
            
            if dist_column == 1 and (row_end - row_start) == direction:
                return target_piece != ""
            
        case "♕":
            if row_start == row_end or column_start == column_end or dist_row == dist_column:
                return isPathClear(chess_board, (row_start, column_start), (row_end, column_end))
        case "♔":
            return dist_row <= 1 and dist_column <= 1
        case "♘":
            return (dist_row == 1 and dist_column == 2) or (dist_row == 2 and dist_column == 1)
        case "♗":
            if dist_row == dist_column:
                return isPathClear(chess_board, (row_start, column_start), (row_end, column_end))
        case "♖":
            if row_start == row_end or column_start == column_end:
                return isPathClear(chess_board, (row_start, column_start), (row_end, column_end))
    
    return False

def makeMove(start_pos, end_pos):
    if canMove(start_pos, end_pos):
        chess_board[end_pos] = chess_board[start_pos]
        chess_board[start_pos] = ""
    else:
        print("!-----Can't move-----!")


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
                piece = "."
            row_str += f" {piece}"
        print (f"{row_str} |")
    print("  |-----------------|")
    print("  | A B C D E F G H |")
    print("  |_________________|")

    
def NextStepForPlayer():
    print(21*"-")
    print("What figure will you move?")
    start_pos = input()

    print("Where will you move you figure?")
    end_pos = input()

    makeMove(start_pos, end_pos)
    ChessBoardPrint()

def MainGame():
    print("  -----CMD-CHESS-----")
    ChessBoardPrint()

    while True:
        print(21*"-")
        print("Next step: 1")
        print("Save game: 2")
        print("Load game: 3")
        print("Exit: 0")
        print(21*"-")

        try:
            choise = int(input("Choose action: "))
        except TypeError:
            print("You should enter only numb1ers!")

        match choise:
            case 1:
                NextStepForPlayer() 
            case 2:
                save.SaveGame(chess_board)
                ChessBoardPrint()
            case 3:
                save.LoadGame(chess_board)
                ChessBoardPrint()
            case 0:
                break

MainGame()
