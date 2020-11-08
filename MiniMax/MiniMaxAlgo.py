class MiniMaxAlgo:

    def __init__(self, _searchDepth, aiPlayer):

        assert _searchDepth > 2

        self.searchDepth = _searchDepth
        
        if aiPlayer == -1:
            self.selectionFunc = min
        elif aiPlayer == +1:
            self.selectionFunc = max
        else:
            assert False

    def getBestMove(self, game):

        self.cache = {}

        bestMove,bestCost = self._minimax(game, self.selectionFunc, 0)

        print(f'best move cost=   {bestCost}')
        print(f'moves searched=   {len(self.cache)}')
        print(f'cache hits    =   {sum([h for _,_,h in self.cache.values()])}')

        return bestMove

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
        