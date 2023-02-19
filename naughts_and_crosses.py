import random

'''

Program to play naughts and crosses, either multiplayer or an easy, medium
hard mode against the computer

'''

def finished(board,winner):
'''
Calculates winner of the game
'''
    for r in range(3):
        if board[r][0] == "X" and board[r][1] == "X" and board[r][2] == "X":
            winner = 1
        if board[r][0] == "O" and board[r][1] == "O" and board[r][2] == "O":
            winner = 2
        else:
            pass
    for c in range(3):
        if board[0][c] == "X" and board[1][c] == "X" and board[2][c] == "X":
            winner = 1
        if board[0][c] == "O" and board[1][c] == "O" and board[2][c] == "O":
            winner = 2
        else:
            pass
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        winner = 1
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        winner = 2
    else:
        pass
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        winner = 1
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        winner = 2
    else:
        pass
    return winner
    
def easy(board,items):
'''
Easy mode: computer has no strategy, places randomly
'''
    row = random.randint(0,2)
    collumn = random.randint(0,2)
    while board[row][collumn] != "-":
        row = random.randint(0,2)
        collumn = random.randint(0,2)
    board[row][collumn] = items[1]
    return board

def medium(board,items,mode):
'''
Medium mode: if computer can win (eg 2 x's in a row) it will know to place the third
'''
    placed = False
    for r in range(3):
        for c in range(3):
            nums = [0,1,2]
            nums.remove(c)
            if board[r][nums[0]] == "O" and board[r][nums[1]] == "O" and board[r][c] == "-":
                board[r][c] = "O"
                placed = True
            else:
                pass
    for c in range(3):
        for r in range(3):
            nums = [0,1,2]
            nums.remove(r)
            if board[nums[0]][c] == "O" and board[nums[1]][c] == "O" and board[r][c] == "-":
                board[r][c] = "O"
                placed = True
            else:
                pass
    for c in range(3):
        nums = [0,1,2]
        nums.remove(c)
        if board[nums[0]][nums[0]] == "O" and board[nums[1]][nums[1]] == "O" and board[c][c] == "-":
            board[c][c] = "O"
            placed = True
        else:
            pass
    for c in range(3):
        nums = [0,1,2]
        nums.remove(c)
        if board[nums[0]][2-nums[0]] == "O" and board[nums[1]][2-nums[1]] == "O" and board[2-c][c] == "-":
            board[2-c][c] = "O"
            placed = True
            #check this
        else:
            pass
    if placed == False and mode == 3:
        board = hard(board,items)
    elif placed == False and mode == 2:
        board = easy(board,items)
    else:
        pass
    return board

def hard(board,items):
'''
Hard Mode: if computer is about to win it will place the right piece, if not if the player
Regression Line.py
'''
    placed = False
    for r in range(3):
        for c in range(3):
            nums = [0,1,2]
            nums.remove(c)
            if board[r][nums[0]] == "X" and board[r][nums[1]] == "X" and board[r][c] == "-":
                board[r][c] = "O"
                placed = True
            else:
                pass
    for c in range(3):
        for r in range(3):
            nums = [0,1,2]
            nums.remove(r)
            if board[nums[0]][c] == "X" and board[nums[1]][c] == "X" and board[r][c] == "-":
                board[r][c] = "O"
                placed = True
            else:
                pass
    for c in range(3):
        nums = [0,1,2]
        nums.remove(c)
        if board[nums[0]][nums[0]] == "X" and board[nums[1]][nums[1]] == "X" and board[c][c] == "-":
            board[c][c] = "O"
            placed = True
        else:
            pass
    for c in range(3):
        nums = [0,1,2]
        nums.remove(c)
        if board[nums[0]][2-nums[0]] == "X" and board[nums[1]][2-nums[1]] == "X" and board[2-c][c] == "-":
            board[2-c][c] = "O"
            placed = True
        else:
            pass
        #check this
    if placed == False:
        board = easy(board,items)
    else:
        pass
    return board
    
    
def multiplayer():
'''
Allows two players to play together
'''
    board = [["-","-","-"],["-","-","-"],["-","-","-"]]
    items = ["X","O"]
    winner = 0 #0 = no winner 1 = player 1 2 = player 2 3 = draw
    while winner == 0:
        for player in range(2):
            print (board[0])
            print (board[1])
            print (board[2])
            print("Player",player+1,"Choose row: ")
            row = int(input()) - 1
            print("Player",player+1,"Choose collumn: ")
            collumn = int(input()) - 1
            while board[row][collumn] != "-":
                 print ("not available")
                 print ("Player",player+1,"Choose row: ")
                 row = int(input()) - 1
                 print("Player",player+1,"Choose row: ")
                 collumn = int(input()) - 1
            board[row][collumn] = items[player]
            winner = finished(board,winner)
            finish = True
            for item in board:
                for count in range(3):
                    if item[count] == "-":
                        finish = False
                    else:
                        pass
            if finish == True:
                winner = 3
            else:
                pass
            print("\n\n")
    print (board[0])
    print (board[1])
    print (board[2])
    if winner == 3:
        print ("Its a draw!")
    else:
        print ("winner is player",winner)

def singleplayer():
'''
Main game for playing against computer, will use either hard, medium or easy functions above
'''
    board = [["-","-","-"],["-","-","-"],["-","-","-"]]
    items = ["X","O"]
    mode = int(input("1.Easy \n2.Medium \n3.Hard \n"))
    winner = 0
    while winner == 0:
        print (board[0])
        print (board[1])
        print (board[2])
        row = int(input("Choose row: ")) - 1
        collumn = int(input("Choose collumn: ")) - 1
        while board[row][collumn] != "-":
            print ("not available")
            row = int(input("Choose row: ")) - 1
            collumn = int(input("Choose collumn: ")) - 1
        board[row][collumn] = items[0]
        if mode == 1:
            board = easy(board,items)
        elif mode == 2:
            board = medium(board,items,mode)
        else:
            board = medium(board,items,mode)
        winner = finished(board,winner)
        finish = True
        for item in board:
            for count in range(3):
                if item[count] == "-":
                    finish = False
                else:
                   pass
        if finish  == True:
            winner = 3
        else:
            pass
        print("\n\n")
            
    print (board[0])
    print (board[1])
    print (board[2])
    if winner == 1:
        print("You Win")
    elif winner == 3:
        print ("Its a Draw")
    else:
        print("You Loose")

choice = int(input("Choose a mode:\n1.Singleplayer \n2.Multiplayer \n3.Exit\n"))
while choice != 3:
    if choice == 1:
        singleplayer()
    else:
        multiplayer()
    choice = int(input("Choose a mode:\n1.Singleplayer \n2.Multiplayer \n3.Exit\n"))

print("Goodbye")
