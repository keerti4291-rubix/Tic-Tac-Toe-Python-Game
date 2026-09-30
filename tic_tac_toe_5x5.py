class TicTacToe5x5:
    def __init__(self):
        self.size=5; self.board=[" "]*25
    def display_board(self):
        print()
        for r in range(5):
            s=r*5
            print(" | ".join(self.board[i] if self.board[i]!=" " else str(i+1) for i in range(s,s+5)))
            if r<4: print("---+"*4+"---")
        print()
    def make_move(self,p,symbol):
        i=p-1
        if 0<=i<25 and self.board[i]==" ":
            self.board[i]=symbol; return True
        return False
    def is_full(self): return " " not in self.board
    def check_winner(self,symbol):
        lines=[tuple(r*5+c for c in range(5)) for r in range(5)]
        lines += [tuple(r*5+c for r in range(5)) for c in range(5)]
        lines += [(0,6,12,18,24),(4,8,12,16,20)]
        return any(all(self.board[i]==symbol for i in line) for line in lines)
