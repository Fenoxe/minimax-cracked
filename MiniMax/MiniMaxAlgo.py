from connect4_minimax_fast import minimax as minimax_v1
from connect4_minimax_veryfast import minimax as minimax_v2,convert_to_bitstrings

class MiniMaxAlgo:

    def __init__(self, _searchDepth, aiPlayer, _useFast=False, _useVeryFast=False):

        assert _searchDepth > 2

        self.searchDepth = _searchDepth

        self.useFast = _useFast
        self.useVeryFast = _useVeryFast

        if aiPlayer == -1:
            self.selectionFunc = min
        elif aiPlayer == +1:
            self.selectionFunc = max
        else:
            assert False

    def getBestMove(self, game):

        self.cache = {}

        if self.useVeryFast:
            position, mask = convert_to_bitstrings(game.board)
            bestMove,bestCost = minimax_v2(position, mask, self.searchDepth)
        elif self.useFast:
            str_state = self.getStrState(game)
            bestMove,bestCost = minimax_v1(str_state, 'A', self.searchDepth, float('-inf'), float('+inf'), self.cache)
        else:
            bestMove,bestCost = self._minimax(game, self.selectionFunc, 0)

        print(f'best move cost=   {bestCost}')
        print(f'moves searched=   {len(self.cache)}')

        return bestMove

    def getStrState(self, game):
        board = game.board.board
        s = ''

        for i in range(5,-1,-1):
            for j in range(7):
                if board[i,j] == 1:
                    s += 'H'
                elif board[i,j] == -1:
                    s += 'A'
                else:
                    s += ' '
        
        return s

    def _minimax(self, game, selectionFunc, depth):
        
        if depth > self.searchDepth:
            return None,game.cost()

        gameHash = game.getHash()

        if gameHash in self.cache:
            m,c,h = self.cache[gameHash]
            self.cache[gameHash] = (m, c, h+1)
            return (m,c)

        nextSelectionFunc = min if selectionFunc is max else max

        moves = game.getMoves()

        bestMove = -1
        bestCost = -1 * selectionFunc(float('-inf'), float('+inf'))
        for move in moves:

            nextGame = game.copy()
            nextGame.doMove(move)

            _,cost = self._minimax(nextGame, nextSelectionFunc, depth + 1)

            bestMove,bestCost = selectionFunc(((bestMove, bestCost),(move,cost)), key=lambda x: x[1])

        self.cache[gameHash] = (bestMove,bestCost, 0)

        return bestMove,bestCost
        