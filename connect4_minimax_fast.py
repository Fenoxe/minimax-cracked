def minimax(state, player, depth, a, b, cache):

    if state in cache:
        return cache[state]

    if not depth:
        out = (None,cost(state))
        cache[state] = out
        return out

    c = cost(state)
    if c:
        cache[state] = (None,c)
        return (None,c)

    if player == 'H':

        bestCost = float('-inf')
        bestMove = -1

        for move in getMoves(state):

            foundCost = minimax(doMove(state, move, player), 'A', depth - 1, a, b, cache)[1]
            if foundCost > bestCost:
                bestCost = foundCost
                bestMove = move

            a = max(a, bestCost)
            if a >= b:
                break
    
    else: # player = 'A'
        
        bestCost = float('+inf')
        bestMove = -1

        for move in getMoves(state):

            foundCost = minimax(doMove(state, move, player), 'H', depth - 1, a, b, cache)[1]

            if foundCost < bestCost:
                bestCost = foundCost
                bestMove = move

            b = min(b, bestCost)
            if b <= a:
                break
    
    cache[state] = (bestMove,bestCost)

    return bestMove,bestCost

def getMoves(state):
    for i in range(7):
        if state[i] == ' ':
            yield i
            

def cost(state):
    # horizontal
    for i in range(6):
        for j in range(4):
            c = state[7 * i + j]
            if c == ' ':
                continue
            for o in range(1,4):
                if state[7 * i + (j + o)] != c:
                    found = False
                    break
                found = True
            if found:
                r = 1000 if c == 'H' else -1000
                return r

    # vertical
    for j in range(7):
        for i in range(3):
            c = state[7 * i + j]
            if c == ' ':
                continue
            for o in range(1,4):
                if state[7 * (i + o) + j] != c:
                    found = False
                    break
                found = True
            if found:
                r = 1000 if c == 'H' else -1000
                return r

    return 0

def costDP(state):
    # n^2 runtime dp approach
    table = [
        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0]],
        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0]],
        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0]],
        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0]],
        [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0]],
        [[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[1,1]],
    ]

    cost = 0

    for i in range(5,-1,-1):
        for j in range(6,-1,-1):

            if i < 5:
                if state[7 * i + j] == state[7 * (i+1) + j] != ' ':
                    table[i][j][1] = table[i+1][j][1] + 1
                    if table[i][j][1] >= 4:
                        p = state[7 * i + j]
                        if p == 'H':
                            return 1000
                            cost += 1000
                        else:
                            return -1000
                            cost -= 1000

            if j < 6:
                if state[7 * i + j] == state[7 * i + (j + 1)] != ' ':
                    table[i][j][0] = table[i][j+1][0] + 1
                    if table[i][j][0] >= 4:
                        p = state[7 * i + j]
                        if p == 'H':
                            return 1000
                            cost += 1000
                        else:
                            return -1000
                            cost -= 1000
    return 0
    return cost

def doMove(state, move, player):
    for i in range(5, -1, -1):
        if state[7 * i + move] == ' ':
            return ''.join([state[: 7 * i + move], player, state[7 * i + move + 1 :]])

def printState(state):
    for i in range(6):
        print(' '.join(state[7 * i : 7 * (i+1)]))
    print()
