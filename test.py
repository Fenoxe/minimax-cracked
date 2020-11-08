from Game.ConnectN.ConnectNGame import ConnectNGame
from MiniMax.MiniMaxAlgo import MiniMaxAlgo

if __name__ == '__main__':

    SEARCH_DEPTH = 6

    game = ConnectNGame(6,7,4)

    game.doMove(3)

    algo = MiniMaxAlgo(SEARCH_DEPTH,-1)

    algo.getBestMove(game)
