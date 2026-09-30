import random

def empty_positions(game):
    return [i+1 for i,v in enumerate(game.board) if v==" "]

def computer_move(game,computer="O",player="X"):
    for p in empty_positions(game):
        game.board[p-1]=computer
        if game.check_winner(computer): return
        game.board[p-1]=" "
    for p in empty_positions(game):
        game.board[p-1]=player
        if game.check_winner(player):
            game.board[p-1]=computer; return
        game.board[p-1]=" "
    centre=(len(game.board)//2)+1
    if centre in empty_positions(game):
        game.board[centre-1]=computer; return
    p=random.choice(empty_positions(game))
    game.board[p-1]=computer

def get_position(game):
    while True:
        try:
            p=int(input(f"Choose position (1-{len(game.board)}): "))
            if 1<=p<=len(game.board): return p
            print("Invalid position!")
        except ValueError:
            print("Please enter a number.")

def computer_vs_player(game):
    print("\nYou = X\nComputer = O")
    while True:
        game.display_board()
        p=get_position(game)
        if not game.make_move(p,"X"):
            print("Position already taken!"); continue
        if game.check_winner("X"):
            game.display_board(); print("You win!"); return
        if game.is_full():
            game.display_board(); print("It's a draw!"); return
        print("Computer is thinking...")
        computer_move(game)
        if game.check_winner("O"):
            game.display_board(); print("Computer wins!"); return
        if game.is_full():
            game.display_board(); print("It's a draw!"); return
