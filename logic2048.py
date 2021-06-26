import random
def start_game():
    game_matrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    return game_matrix
def add_new_2(game_matrix):
    while True:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        if game_matrix[r][c] == 0:
            game_matrix[r][c] = 2
            break

def adjust(game_matrix):
    samp_matrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    flag=False
    for i in range(4):
        pos=0
        for j in range(4):
            if game_matrix[i][j]!=0:
                if j!=pos:
                    flag=True
                samp_matrix[i][pos]=game_matrix[i][j]
                pos+=1
    return samp_matrix,flag
def mergematrix(game_matrix):
    flag=False
    for i in range(4):
        for j in range(3):
            if game_matrix[i][j]!=0 and (game_matrix[i][j]==game_matrix[i][j+1]):
                game_matrix[i][j]=game_matrix[i][j]*2
                game_matrix[i][j+1]=0
                flag=True
    return game_matrix,flag
def reverse(game_matrix):
    new_matrix=[]
    for i in range(4):
        new_matrix.append(game_matrix[i][::-1])
    return new_matrix
def transpose(game_matrix):
    new_matrix=[[],[],[],[]]
    for i in range(4):
        new=0
        for j in range(4):
            new_matrix[new].append(game_matrix[i][j])
            new+=1
    return new_matrix
def move_up(game_matrix):
    transposed=transpose(game_matrix)
    new,change1=adjust(transposed)
    new,change2=mergematrix(new)
    final_change = change1 or change2
    new,temp=adjust(new)
    return transpose(new),final_change

def move_down(game_matrix):
    transposed=transpose(game_matrix)
    reversed=reverse(transposed)
    new,change1=adjust(reversed)
    new,change2=mergematrix(new)
    final_change = change1 or change2
    new,temp=adjust(new)
    final_reversed=reverse(new)
    final_mat=transpose(final_reversed)
    return final_mat,final_change
def move_right(game_matrix):
    reversed = reverse(game_matrix)
    new,change1=adjust(reversed)
    new,change2=mergematrix(new)
    final_change = change1 or change2
    new ,temp= adjust(new)
    return reverse(new),final_change
def move_left(game_matrix):
    new,change1=adjust(game_matrix)
    new,change2=mergematrix(new)
    final_change=change1 or change2
    final,temp=adjust(new)
    return final,final_change



def currgame(game_matrix):
    #Three cases (Either you have won  or Continue the game or You have lost)
    #case1:win
    for i in range(4):
        for j in range(4):
            if game_matrix[i][j]==2048:
                return 'You won'
    #case2:Continue the game
    for i in range(4):
        for j in range(4):
            if game_matrix[i][j]==0:
                return 'continue'
    for i in range(3):
        for j in range(3):
            if game_matrix[i][j]==game_matrix[i+1][j] or game_matrix[i][j]==game_matrix[i][j+1]:
                return 'continue'
    for i in range(3):
        if game_matrix[i][3]==game_matrix[i+1][3]:
            return 'continue'
    for i in range(3):
        if game_matrix[3][i]==game_matrix[3][i+1]:
            return 'continue'
    #case3: You lost the game
    return 'lost'

