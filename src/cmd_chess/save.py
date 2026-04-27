import json 
import os

file_path = "data/data.json"

def SaveGame(chess_board):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(chess_board, file)
        
        print("   <--Game Saved!-->")
    except Exception as error:
        print(error)


def LoadGame(chess_board):
    if not os.path.exists(file_path):
        return False
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            chess_board.clear
            chess_board.update(json.load(file))
            print("   <--Game Load!-->")
            return True
        
    except Exception as error:
        print(error)
        return False