class Board:

    WIDTH = 7
    HEIGHT = 6

    def __init__(self):
        self.positions = int('0' * WIDTH * (HEIGHT + 1), 2)
        self.negPlayerPositions = int('0' * WIDTH * (HEIGHT + 1), 2)
    
    def putPiece(self, piece, n):
        if self.board[self.topIndex[n] , n] != 0:
            self.topIndex[n] = self.topIndex[n] + 1

        self.board[self.topIndex[n] , n] = piece

    def hasConnectFour(self, player):

        # Horizontal check
        m = position & (position >> 7)
        if m & (m >> 14):
            return True
        # Diagonal \
        m = position & (position >> 6)
        if m & (m >> 12):
            return True
        # Diagonal /
        m = position & (position >> 8)
        if m & (m >> 16):
            return True
        # Vertical
        m = position & (position >> 1)
        if m & (m >> 2):
            return True

        return False

    def draw(self):
        for i in range(5,-2,-1):
            print('| ',end='')
            for j in range(7):
                if i == -1:
                    print('-',end='')
                elif self.board[i,j] == 1:
                    print('⬤',end='')
                elif self.board[i,j] == -1:
                    print('○',end='')
                else:
                    print(' ',end='')
                print(' ',end='')
            print('|',end='')
            print()

    def copy(self):
        newBoard = Board(
            _M=self.M,
            _N=self.N,
            _K=self.K,
        )

        newBoard.board = self.board.copy()
        newBoard.topIndex = self.topIndex.copy()

        return newBoard

    def getHash(self):
        s = ''.join((self.board + 1).flatten().astype('str'))
        return int(s)


if __name__ == '__main__':
    # board unit testing

    board = Board(6,7,4)

    moves = [
        (+1,3),
        (-1,2),
        (+1,5),
        (-1,2),
        (+1,4),
        (-1,2),
        (+1,2),
        (-1,4),
        (+1,5),
        (-1,4),
        (+1,6),
    ]
    
    for piece,col in moves:
        assert board.hasSequence() == (False,False)

        print(piece,col)
        board.putPiece(piece, col)

        board.draw()

    assert board.hasSequence() == (False,True)
    board.draw()
