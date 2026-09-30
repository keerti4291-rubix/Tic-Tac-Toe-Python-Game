from tic_tac_toe_3x3 import TicTacToe3x3
from tic_tac_toe_4x4 import TicTacToe4x4
from tic_tac_toe_5x5 import TicTacToe5x5
from computer_vs_player import computer_vs_player
from player_vs_player import player_vs_player

def choose_board():
    while True:
        print("\nChoose board size:")
        print("1. 3 x 3")
        print("2. 4 x 4")
        print("3. 5 x 5")
        c=input("Enter choice: ").strip()
        if c=="1": return TicTacToe3x3()
        if c=="2": return TicTacToe4x4()
        if c=="3": return TicTacToe5x5()
        print("Invalid choice!")

def main():
    print("================================")
    print("       TIC TAC TOE")
    print("================================")
    while True:
        print("\n1. Computer vs Player")
        print("2. Player 1 vs Player 2")
        print("3. Exit")
        mode=input("Enter choice: ").strip()
        if mode=="3": break
        if mode not in ("1","2"):
            print("Invalid choice!"); continue
        game=choose_board()
        if mode=="1": computer_vs_player(game)
        else: player_vs_player(game)
        if input("\nPlay again? (y/n): ").strip().lower()!="y": break
    print("Thanks for playing!")

if __name__=="__main__":
    main()
