from termcolor import colored
from IPython.display import clear_output

def display_board(lst):
    clear_output()
    i=43
    while i>=1:
        print(lst[i]+" | "+lst[i+1]+" | "+lst[i+2]+" | "+lst[i+3]+" | "+lst[i+4]+" | "+lst[i+5]+" | "+lst[i+6])
        if i!=1:
            print("--------------------------")
        i-=7
board=["#"]+[" "]*49 #total 7*7 = 49 cells in the board
display_board(board)
col1=[1,8,15,22,29,36,43]
col2=[2,9,16,23,30,37,44]
col3=[3,10,17,24,31,38,45]
col4=[4,11,18,25,32,39,46]
col5=[5,12,19,26,33,40,47]
col6=[6,13,20,27,34,41,48]
col7=[7,14,21,28,35,42,49] #each column stores the the values assigned to each cell in that very column

def assign_to_column(playerno):
    while True:
        try:
            col=int(input("Which column do you want to drop your marker? Write the number"))
        except:
            continue
        else:
            break
    
    while True:
        if 1<=col<=7:
            if col==1:
                if check_for_space(col1): #check for space checks if col==[] which means column is filled, how? you'll see in the next steps
                    pos=min(col1) #pos is the bottommost cell in that column
                    col1.remove(pos) #once that position is filled remove the cell number from that column (means that cell is no more available)
                    break
                else:
                    col=col_filled(col1) #col_filled just displays the message when the column is filled and prompts the user to choose another column
            if col==2:
                if check_for_space(col2):
                    pos=min(col2)
                    col2.remove(pos)
                    break
                else:
                    col=col_filled(col2)
            if col==3:
                if check_for_space(col3):
                    pos=min(col3)
                    col3.remove(pos)
                    break
                else:
                    col=col_filled(col3)
            if col==4:
                if check_for_space(col4):
                    pos=min(col4)
                    col4.remove(pos)
                    break
                else:
                    col=col_filled(col4)
            if col==5:
                if check_for_space(col5):
                    pos=min(col5)
                    col5.remove(pos)
                    break
                else:
                    col=col_filled(col5)
            if col==6:
                if check_for_space(col6):
                    pos=min(col6)
                    col6.remove(pos)
                    break
                else:
                    col=col_filled(col6)
            if col==7:
                if check_for_space(col7):
                    pos=min(col7)
                    col7.remove(pos)
                    break
                else:
                    col=col_filled(col7)
        else:
            col=col_filled(col)
    #the loop doesnt end until the chosen column is valid, and when it is, it executes the below statements   
    if playerno==1:
        board[pos]=marker1
    else:
        board[pos]=marker2
        
def check_for_space(col):
    return col!=[]
def col_filled(col):
    col=int(input("Please choose another column"))
    return col
def board_filled(board):
    for item in board:
        if item==" ":
            return False
    return True

def check_for_four(board,marker):
    cond= (board[1]==board[8]==board[15]==board[22]==marker or board[29]==board[8]==board[15]==board[22]==marker 
           or board[29]==board[36]==board[15]==board[22]==marker or board[29]==board[36]==board[43]==board[22]==marker
           or board[2]==board[9]==board[16]==board[23]==marker or board[30]==board[9]==board[16]==board[23]==marker
           or board[30]==board[37]==board[16]==board[23]==marker or board[30]==board[37]==board[44]==board[23]==marker
           or board[3]==board[10]==board[17]==board[24]==marker or board[31]==board[10]==board[17]==board[24]==marker
           or board[31]==board[38]==board[17]==board[24]==marker or board[31]==board[38]==board[45]==board[24]==marker
           or board[4]==board[11]==board[18]==board[25]==marker or board[32]==board[11]==board[18]==board[25]==marker
           or board[32]==board[39]==board[18]==board[25]==marker or board[32]==board[39]==board[46]==board[25]==marker
           or board[5]==board[12]==board[19]==board[26]==marker or board[33]==board[12]==board[19]==board[26]==marker
           or board[33]==board[40]==board[19]==board[26]==marker or board[33]==board[40]==board[47]==board[26]==marker
           or board[6]==board[13]==board[20]==board[27]==marker or board[34]==board[13]==board[20]==board[27]==marker
           or board[34]==board[41]==board[20]==board[27]==marker or board[34]==board[41]==board[48]==board[27]==marker
           or board[7]==board[14]==board[21]==board[28]==marker or board[35]==board[14]==board[21]==board[28]==marker
           or board[35]==board[42]==board[21]==board[28]==marker or board[35]==board[42]==board[49]==board[28]==marker
           #checking for verticals
           
           or board[1]==board[2]==board[3]==board[4]==marker or board[2]==board[3]==board[4]==board[5]==marker 
           or board[3]==board[4]==board[5]==board[6]==marker or board[4]==board[5]==board[6]==board[7]==marker
           or board[8]==board[9]==board[10]==board[11]==marker or board[9]==board[10]==board[11]==board[12]==marker
           or board[10]==board[11]==board[12]==board[13]==marker or board[11]==board[12]==board[13]==board[14]==marker
           or board[15]==board[16]==board[17]==board[18]==marker or board[16]==board[17]==board[18]==board[19]==marker
           or board[17]==board[18]==board[19]==board[20]==marker or board[18]==board[19]==board[20]==board[21]==marker
           or board[22]==board[23]==board[24]==board[25]==marker or board[23]==board[24]==board[25]==board[26]==marker
           or board[24]==board[25]==board[26]==board[27]==marker or board[25]==board[26]==board[27]==board[28]==marker
           or board[29]==board[30]==board[31]==board[32]==marker or board[30]==board[31]==board[32]==board[33]==marker
           or board[31]==board[32]==board[33]==board[34]==marker or board[32]==board[33]==board[34]==board[35]==marker
           or board[36]==board[37]==board[38]==board[39]==marker or board[37]==board[38]==board[39]==board[40]==marker
           or board[38]==board[39]==board[40]==board[41]==marker or board[39]==board[40]==board[41]==board[42]==marker
           or board[43]==board[44]==board[45]==board[46]==marker or board[44]==board[45]==board[46]==board[47]==marker
           or board[45]==board[46]==board[47]==board[49]==marker or board[46]==board[47]==board[48]==board[49]==marker
           #checking for horizontals
    
           or board[1]==board[9]==board[17]==board[25]==marker or board[9]==board[17]==board[25]==board[33]==marker
           or board[17]==board[25]==board[33]==board[41]==marker or board[25]==board[33]==board[41]==board[49]==marker
           or board[8]==board[16]==board[24]==board[32]==marker or board[16]==board[24]==board[32]==board[40]==marker
           or board[24]==board[32]==board[40]==board[48]==marker
           or board[15]==board[23]==board[31]==board[39]==marker or board[23]==board[31]==board[39]==board[47]==marker
           or board[22]==board[30]==board[38]==board[46]==marker
           or board[2]==board[10]==board[18]==board[26]==marker or board[10]==board[18]==board[26]==board[34]==marker
           or board[18]==board[26]==board[34]==board[42]==marker
           or board[3]==board[11]==board[19]==board[27]==marker or board[11]==board[19]==board[27]==board[35]==marker
           or board[4]==board[12]==board[20]==board[28]==marker
           #checking for right diagonals
           
           or board[7]==board[13]==board[19]==board[25]==marker or board[13]==board[19]==board[25]==board[31]==marker
           or board[19]==board[25]==board[31]==board[37]==marker or board[25]==board[31]==board[37]==board[43]==marker
           or board[14]==board[20]==board[26]==board[32]==marker or board[20]==board[26]==board[32]==board[38]==marker 
           or board[26]==board[32]==board[38]==board[44]==marker
           or board[21]==board[27]==board[33]==board[39]==marker or board[27]==board[33]==board[39]==board[45]==marker
           or board[28]==board[34]==board[40]==board[46]==marker
           or board[6]==board[12]==board[18]==board[24]==marker or board[12]==board[18]==board[24]==board[30]==marker
           or board[18]==board[24]==board[30]==board[36]==marker
           or board[5]==board[11]==board[17]==board[23]==marker or board[11]==board[17]==board[23]==board[29]==marker
           or board[4]==board[10]==board[16]==board[22]==marker)
           #checking for left diagonals
    return cond==True

playing=True
print("Welcome to Connect Four")
board=["#"]+[" "]*49

marker1=colored('O', 'red')
marker2=colored('O', 'yellow')

while playing:
    display_board(board)
    if board_filled(board):
        print("Board is filled. It's a tie")
        playing=False
    else:
        print ("Player 1's turn")
        assign_to_column(1)
        display_board(board)
        if check_for_four(board,marker1):
            print("Player 1 wins")
            break

        print ("Player 2's turn")
        assign_to_column(2)
        display_board(board)
        if check_for_four(board,marker2):
            print("Player 2 wins")
            break
    