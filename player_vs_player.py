def get_position(game):
    while True:
        try:
            p=int(input(f"Choose position (1-{len(game.board)}): "))
            if 1<=p<=len(game.board): return p
            print("Invalid position!")
        except ValueError:
            print("Please enter a number.")

def player_vs_player(game):
    player="X"
    print("\nPlayer 1 = X\nPlayer 2 = O")
    while True:
        game.display_board()
        p=get_position(game)
        if not game.make_move(p,player):
            print("Position already taken!"); continue
        if game.check_winner(player):
            game.display_board(); print(f"Player {player} wins!"); return
        if game.is_full():
            game.display_board(); print("It's a draw!"); return
        player="O" if player=="X" else "X"
