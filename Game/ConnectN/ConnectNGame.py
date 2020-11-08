from .Board import Board
from ..Game import Game

class ConnectNGame(Game):

    def __init__(self, _boardHeight, _boardWidth, _numForSequence, isCopy=False):
        self.board = None
        
        if not isCopy:
            self.board = Board(
                _M=_boardHeight,
                _N=_boardWidth,
                _K=_numForSequence,
            )

        self.boardHeight = _boardHeight
        self.boardWidth = _boardWidth
        self.numForSequence = _numForSequence
        
        self.turn = 1

    def doMove(self, move):
        self.board.putPiece(self.turn, move)

        self.turn *= -1

    def winner(self):
        negWon,posWon = self.board.hasSequence()
        if not len(self.board.getNonEmptyColumns()):
            return None

        if negWon: return -1
        if posWon: return +1
        
        return 0

    def getMoves(self):
        validCols = self.board.getNonEmptyColumns()

        return validCols

    def getTurn(self):
        return self.turn

    def draw(self):
        self.board.draw()

    def copy(self):
        newGame = ConnectNGame(self.boardHeight, self.boardWidth, self.numForSequence, isCopy=True)

        newGame.board = self.board.copy()
        newGame.turn = self.turn

        return newGame

    def cost(self):
        negWon, posWon = self.board.hasSequence()

        if negWon:
            return -1000
        
        if posWon:
            return +1000

        return 0

    def getHash(self):
        return self.board.getHash()

if __name__ == '__main__':

    game = ConnectNGame(6,7,4)

    moves = [4,3,5,1,5,3,2,6,2,0,3]

    for move in moves:
        game.doMove(move)
        game.draw()

    print(game.winner())
    print(game.getMoves())