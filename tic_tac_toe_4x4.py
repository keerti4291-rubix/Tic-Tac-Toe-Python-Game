class TicTacToe4x4:
    def __init__(self):
        self.size=4; self.board=[" "]*16
    def display_board(self):
        print()
        for r in range(4):
            s=r*4
            print(" | ".join(self.board[i] if self.board[i]!=" " else str(i+1) for i in range(s,s+4)))
            if r<3: print("---+"*3+"---")
        print()
    def make_move(self,p,symbol):
        i=p-1
        if 0<=i<16 and self.board[i]==" ":
            self.board[i]=symbol; return True
        return False
    def is_full(self): return " " not in self.board
    def check_winner(self,symbol):
        lines=[tuple(r*4+c for c in range(4)) for r in range(4)]
        lines += [tuple(r*4+c for r in range(4)) for c in range(4)]
        lines += [(0,5,10,15),(3,6,9,12)]
        return any(all(self.board[i]==symbol for i in line) for line in lines)
