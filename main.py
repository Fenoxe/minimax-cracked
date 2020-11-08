from Game.ConnectN.ConnectNGame import ConnectNGame
from MiniMax.MiniMaxAlgo import MiniMaxAlgo

if __name__ == '__main__':

    HUMAN_PLAYER = +1
    AI_PLAYER = -1

    BOARD_WIDTH = 7
    BOARD_HEIGHT = 6
    NUM_FOR_SEQ = 4

    SEARCH_DEPTH = 4

    game = ConnectNGame(
        BOARD_HEIGHT,
        BOARD_WIDTH,
        NUM_FOR_SEQ
    )

    algo = MiniMaxAlgo(
        SEARCH_DEPTH,
        AI_PLAYER
    )

    run = True

    while run:
        
        game.draw()

        winner = game.winner()
        if winner:
            print(f'winner: {winner}')
            print('---game over---')
            run = False
            break

        turn = game.getTurn()
        print(f'turn: {turn}')

        if True or turn == HUMAN_PLAYER:
            moves = game.getMoves()
            print(f'moves: {moves}')

            move = None
            while move not in moves:
                move = input('select a move: ')
                move = int(move)
        
        elif turn == AI_PLAYER:
            print('algo finding best move...')

            move = algo.getBestMove(game)
        
        game.doMove(move)

