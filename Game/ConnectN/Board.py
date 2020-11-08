import numpy as np
from scipy.signal import convolve2d

class Board:

    def __init__(self, _M, _N, _K):
        """
        _M: height board                                          \n
        _N: width board                                           \n
        _K: needed pieces in a row or column to be a sequence     \n
        """
        self.board = np.zeros((_M,_N), dtype=np.int8)
        self.topIndex = [0 for _ in range(_N)]
        self.horSolKernel = np.ones((1,_K))
        self.verSolKernel = np.ones((_K,1))
        self.M = _M
        self.N = _N
        self.K = _K

    def getNonEmptyColumns(self):
        return [i for i in range(self.N) if self.topIndex[i] != (self.M - 1)]

    def getTopPiece(self, n):
        return self.board[self.topIndex[n] , n]

    def putPiece(self, piece, n):
        if self.board[self.topIndex[n] , n] != 0:
            self.topIndex[n] = self.topIndex[n] + 1

        self.board[self.topIndex[n] , n] = piece

    def hasSequence(self):
        horizontal = convolve2d(self.board, self.horSolKernel, mode='valid')
        vertical = convolve2d(self.board, self.verSolKernel, mode='valid')

        hasPosSequence = np.any(horizontal == self.K) + np.any(vertical == self.K)
        hasNegSequence = np.any(horizontal == -self.K) + np.any(vertical == -self.K)

        return (hasNegSequence , hasPosSequence)

    def draw(self):
        print(self.board)

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
