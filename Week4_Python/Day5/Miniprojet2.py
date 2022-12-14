def affichage(t):
    print(f"""
    Welcome to TIC TAC TOE
    
    TIC TAC TOE
    *****************
    *   {t['0'][0]} | {t['0'][1]} | {t['0'][2]}   *
    *  ---|---|---  *
    *   {t['1'][0]} | {t['1'][1]} | {t['1'][2]}   *
    *  ---|---|---  *
    *   {t['2'][0]} | {t['2'][1]} | {t['2'][2]}   *
    *****************
    """)


def player_input(player):
    print(f"\tPlayer {player}'s turn...\n")
    row = input('\tEnter row: ')
    column = input('\tEnter column: ')
    while True :
        if int(row) > 3 or int(row) < 1 < 1:
            print("\tline incorrect")
        elif int(column) > 3 or int(column) < 1:
            print("\tcolumn incorrect")
        else:
            break
        row = input('\tEnter row: ')
        column = input('\tEnter column: ')
    row = str(int(row) -1)#-1 parceque le tableau commence à 0
    column = str(int(column) -1)
    return row, column


def check_win(t):
    z = [0]
    x = [0]
    for i in range(0, 2):
        z.append(0)
        x.append(0)
    for j in range(0, 3):
        for i in range(0, 3):
            z[i] = 0
            x[i] = 0
        for i in range(0, 3):
            if t[str(i)][i].lower() == 'x':
                x[0] += 1
            if t[str(j)][i].lower() == 'x':
                x[1] += 1
            if t[str(i)][j].lower() == 'x':
                x[2] += 1
            if t[str(i)][i] == '0':
                z[0] += 1
            if t[str(j)][i] == '0':
                z[1] += 1
            if t[str(i)][j] == '0':
                z[2] += 1
        if 3 in z:
            return "\tPlayer 0's the winner"
        if 3 in x:
            return "\tPlayer X's the winner"
    return False


def play(player, t):
    while True:
        index = player_input(player)
        ind = int(index[1])
        if t[index[0]][ind] == ' ': # il nous faut vérifer si la case est occupé ou pas
            t[index[0]][ind] = player
            return t
        else:
            print('\tCase occupée')

def main():
    t = {
        '0': [],
        '1': [],
        '2': []
    }
    for x in t:
        for i in range(0, 3):
            t[x].append(' ')

    # Début du jeu avec X
    player = '0'
    while True:
        if player == '0':
            player = 'X'
        else:
            player = '0'
        affichage(t)
        t = play(player, t)
        win = check_win(t)
        affichage(t)
        if win:
            print(win)
            return True


main()