from Game.ConnectN.ConnectNGame import ConnectNGame
from MiniMax.MiniMaxAlgo import MiniMaxAlgo

if __name__ == '__main__':

    HUMAN_PLAYER = +1
    AI_PLAYER = -1

    SEARCH_DEPTH = 14

    game = ConnectNGame(6,7,4)

    algo = MiniMaxAlgo(
        SEARCH_DEPTH,
        AI_PLAYER,
        useVeryFast=True
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

        if winner is None:
            print(f'no possible moves')
            print('---game over---')
            run = False
            break

        turn = game.getTurn()
        print(f'turn: {turn}')

        if turn == HUMAN_PLAYER:
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

