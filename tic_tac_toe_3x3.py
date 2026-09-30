class TicTacToe3x3:
    def __init__(self):
        self.size=3; self.board=[" "]*9
    def display_board(self):
        print()
        for r in range(3):
            s=r*3
            print(" | ".join(self.board[i] if self.board[i]!=" " else str(i+1) for i in range(s,s+3)))
            if r<2: print("---+---+---")
        print()
    def make_move(self,p,symbol):
        i=p-1
        if 0<=i<9 and self.board[i]==" ":
            self.board[i]=symbol; return True
        return False
    def is_full(self): return " " not in self.board
    def check_winner(self,symbol):
        lines=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(all(self.board[i]==symbol for i in line) for line in lines)
