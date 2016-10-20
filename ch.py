import sys
import time
import random
import os
        
def symbol(piece):
    if(piece=="n"):
        return "\u2658"
    elif(piece=="-n"):
        return "\u265E"
    elif(piece=="k"):
        return "\u2654"
    elif(piece=="-k"):
        return "\u265A"
    else:
        return "\u2656"
	
def chessboardIndex():
    boardindex=[]
    row='abcdefgh'
    col='87654321'
    for c in col:
        for r in row:
            boardindex.append(r+c)
    return boardindex

def setupChessboard(white_chess, black_chess):
    board=[]
    for i in black_chess:   #first is black
        board.append(i)         
    for k in range(48):     #second
        board.append(".")
    for o in white_chess:   #last is white
        board.append(o)        

    return board
    


def knightTable(boardIndex):
    table=dict()
    night=[\
 -50,-40,-30,-30,-30,-30,-40,-50,\
 -40,-20,  0,  0,  0,  0,-20,-40,\
 -30,  0, 10, 15, 15, 10,  0,-30,\
 -30,  5, 15, 20, 20, 15,  5,-30,\
 -30,  0, 15, 20, 20, 15,  0,-30,\
 -30,  5, 10, 15, 15, 10,  5,-30,\
 -40,-20,  0,  5,  5,  0,-20,-40,\
 -50,-40,-20,-30,-30,-20,-40,-50]
    for i in range(64):
        table[boardIndex[i]]=night[i]
    return table

def kingTable(boardIndex):
    table=dict()
    Kingv=[\
 -50,-40,-30,-20,-20,-30,-40,-50,\
 -30,-20,-10,  0,  0,-10,-20,-30,\
 -30,-10, 20, 30, 30, 20,-10,-30,\
 -30,-10, 30, 40, 40, 30,-10,-30,\
 -30,-10, 30, 40, 40, 30,-10,-30,\
 -30,-10, 20, 30, 30, 20,-10,-30,\
 -30,-30,  0,  0,  0,  0,-30,-30,\
 -50,-30,-30,-30,-30,-30,-30,-50]
    for i in range(64):
        table[boardIndex[i]]=Kingv[i]
    return table

#using dictionary to store chess state.
def assignValue(boardIndex,board):
    value=dict()
    for i in range(64):
        value[boardIndex[i]]=board[i]
    return value
    


def displayBoard(board):
    i=64
    for b in board:
        if i%8==0: print(int(i/8),end=" ")
        i-=1
        if(b=='.'):print(b,end=" ")
        else:print(symbol(b), end=" ")
        if i%8==0: print('')
    print("  a b c d e f g h")
    
def displayDict(current_board):
    i=64
    for b in boardIndex:
        if i%8==0: print(int(i/8),end=" ")
        i-=1
        #print(b,end=" ")
        if(current_board[b]=='.'):print(current_board[b],end=" ")
        else:print(symbol(current_board[b]), end=" ")
        #else:print((current_board[b]), end=" ")
        if i%8==0: print('')
    print("  a b c d e f g h")




def rook_possible_move(position, current_board, condition):
#if condition is True, then move include own peice. 
    moves=[]

    #print("in rook possible move ", position)    
    col=ord(position[0])   #col
    while(col>97):    #check left
        col=col-1
        p=chr(col)+position[1]

        if(current_board[p]=='.' ): moves.append(p)
        elif(current_board[p][0]=='-'):  #and is oppose peice.
            moves.append(p)
            break
        else:
            if(condition):
                moves.append(p)         #to check if can protect own peice.
            break

    col=ord(position[0])   #col
    while(col<104):    #check right
        col=col+1
        p=chr(col)+position[1]

        #if the square is not empty, 
        if(current_board[p]=='.' ): moves.append(p)
        elif(current_board[p][0]=='-'):  #and is oppose peice.
            moves.append(p)
            break
        else:
            if(condition):
                moves.append(p)         #to check if can protect own peice.
            break
        
    row=ord(position[1])  #row
    while(row>49):              #may go down
        row=row-1
        p=position[0]+chr(row)
        if(current_board[p]=='.' ): moves.append(p)
        elif(current_board[p][0]=='-'):  #and is oppose peice.
            moves.append(p)
            break
        else:
            if(condition):
                moves.append(p)         #to check if can protect own peice.
            break        

    row=ord(position[1])  #row
    while(row<56):              #may go up
        row=row+1
        p=position[0]+chr(row)
        if(current_board[p]=='.' ): moves.append(p)
        elif(current_board[p][0]=='-'):  #and is oppose peice.
            moves.append(p)
            break
        else:
            if(condition):
                moves.append(p)         #to check if can protect own peice.
            break
    return moves     


def knight_possible_move(position, current_board, condition,turn):
#if condition is True, then move include own peice. 
    moves=[]
    #print("in knight possible move")
    col=ord(position[0])   #col abcdefgh
    row=ord(position[1])    #12345678
    if(col-2>96):     #can move left        
        if(row+1 <57):     #can move up
            p=chr(col-2)+chr(row+1)             
            if(current_board[p]!='.'):                
                if(turn=="black"):              #turn=black
                    if(current_board[p][0]=='-'):
                        if(condition):
                            moves.append(p) 
                        #condition=true, will include own peice
                    else:
                        moves.append(p)
                else:                           #turn=white
                    if(current_board[p][0]=='-'):
                        moves.append(p)
                    else:
                        if(condition):moves.append(p)
            else:
                moves.append(p)
                        
        if(row-1>48):       #can move down
            p=chr(col-2)+chr(row-1)
            if(current_board[p]!='.'):
                if(turn=="black"):              #turn=black
                    if(current_board[p][0]=='-'):
                        if(condition):moves.append(p) 
                        #condition=true, will include own peice
                    else:moves.append(p)
                else:                           #turn=white
                    if(current_board[p][0]=='-'):moves.append(p)
                    else:
                        if(condition):moves.append(p)   
            else:
                moves.append(p)                        
                         
    if(col+2<105):    #can move right
        if(row+1 <57):     #can move up
            p=chr(col+2)+chr(row+1) 
            if(current_board[p]!='.'):
                if(turn=="black"):              #turn=black
                    if(current_board[p][0]=='-'):
                        if(condition):moves.append(p) 
                        #condition=true, will include own peice
                    else:moves.append(p)
                else:                           #turn=white
                    if(current_board[p][0]=='-'):moves.append(p)
                    else:
                        if(condition):moves.append(p)   
            else:
                moves.append(p)                                 
        if(row-1>48):       #can move down
            p=chr(col+2)+chr(row-1)
            if(current_board[p]!='.'):
                if(turn=="black"):              #turn=black
                    if(current_board[p][0]=='-'):
                        if(condition):moves.append(p) 
                        #condition=true, will include own peice
                    else:moves.append(p)
                else:                           #turn=white
                    if(current_board[p][0]=='-'):moves.append(p)
                    else:
                        if(condition):moves.append(p)
            else:
                moves.append(p)                        
                                    
    if(row+2 <57):     #can move up
        if(col-1 >96):     #can move left
            p=chr(col-1)+chr(row+2) 
            if(current_board[p]!='.'):
                if(turn=="black"):              #turn=black
                    if(current_board[p][0]=='-'):
                        if(condition):moves.append(p) 
                        #condition=true, will include own peice
                    else:moves.append(p)
                else:                           #turn=white
                    if(current_board[p][0]=='-'):moves.append(p)
                    else:
                        if(condition):moves.append(p)
            else:
                moves.append(p)                        
                                    
        if(col+1<105):       #can move right
            p=chr(col+1)+chr(row+2)
            if(current_board[p]!='.'):
                if(turn=="black"):              #turn=black
                    if(current_board[p][0]=='-'):
                        if(condition):moves.append(p) 
                        #condition=true, will include own peice
                    else:moves.append(p)
                else:                           #turn=white
                    if(current_board[p][0]=='-'):moves.append(p)
                    else:
                        if(condition):moves.append(p)  
            else:
                moves.append(p)                                  
    if(row-2>48):       #can move down
        if(col-1 >96):     #can move left
            p=chr(col-1)+chr(row-2) 
            if(current_board[p]!='.'):
                if(turn=="black"):              #turn=black
                    if(current_board[p][0]=='-'):
                        if(condition):moves.append(p) 
                        #condition=true, will include own peice
                    else:moves.append(p)
                else:                           #turn=white
                    if(current_board[p][0]=='-'):moves.append(p)
                    else:
                        if(condition):moves.append(p) 
            else:
                moves.append(p)                                   
        if(col+1<105):       #can move right
            p=chr(col+1)+chr(row-2)
            if(current_board[p]!='.'):
                if(turn=="black"):              #turn=black
                    if(current_board[p][0]=='-'):
                        if(condition):moves.append(p) 
                        #condition=true, will include own peice
                    else:moves.append(p)
                else:                           #turn=white
                    if(current_board[p][0]=='-'):moves.append(p)
                    else:
                        if(condition):moves.append(p) 
            else:
                moves.append(p)                                   
    return moves     
    
def king_possible_move(position, current_board, condition, turn):
#if condition=true, possible move include own.
    moves=set()
    #print("in king possible move")
    col=ord(position[0])   #col abcdefgh
    row=ord(position[1])    #12345678
    
    if(col-1>96):                       #can move left
        p=chr(col-1)+chr(row) #left position
        if(current_board[p]=='.'):
            moves.add(p)
        else:
            if(turn=="black"):
                if(current_board[p][0]!='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]=='-' ):
                    moves.add(p)
            else:
                if(current_board[p][0]=='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]!='-' ):
                    moves.add(p)
             
    if(col-1)>96 and (row+1 <57):     #can move left up
        p=chr(col-1)+chr(row+1)           #up left position
        if(current_board[p]=='.'):
            moves.add(p)
        else:
            if(turn=="black"):
                if(current_board[p][0]!='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]=='-' ):
                    moves.add(p)
            else:
                if(current_board[p][0]=='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]!='-' ):
                    moves.add(p)                #own peice
    
    if(col-1)>96 and (row-1) >48:     #can move left down
        p=chr(col-1)+chr(row-1)           #down right position
        if(current_board[p]=='.'):
            moves.add(p)
        else:
            if(turn=="black"):
                if(current_board[p][0]!='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]=='-' ):
                    moves.add(p)
            else:
                if(current_board[p][0]=='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]!='-' ):
                    moves.add(p)                #own peice
            
    if (row+1) <57:     #can move up
        p=chr(col)+chr(row+1)           #up position
        if(current_board[p]=='.'):
            moves.add(p)
        else:
            if(turn=="black"):
                if(current_board[p][0]!='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]=='-' ):
                    moves.add(p)
            else:
                if(current_board[p][0]=='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]!='-' ):
                    moves.add(p)                #own peice         
                        
    if(row-1>48):       #can move down
        p=chr(col)+chr(row-1)   #down positon
        if(current_board[p]=='.'):
            moves.add(p)
        else:
            if(turn=="black"):
                if(current_board[p][0]!='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]=='-' ):
                    moves.add(p)
            else:
                if(current_board[p][0]=='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]!='-' ):
                    moves.add(p)
          
             
    if(col+1<105):    #can move right
        p=chr(col+1)+chr(row)       #right position
        if(current_board[p]=='.'):
            moves.add(p)
        else:
            if(turn=="black"):
                if(current_board[p][0]!='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]=='-' ):
                    moves.add(p)
            else:
                if(current_board[p][0]=='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]!='-' ):
                    moves.add(p)   
            
    if (col+1)<105 and (row+1) <57 :     #can move right up
        p=chr(col+1)+chr(row+1)   #up right position
        if(current_board[p]=='.'):
            moves.add(p)
        else:
            if(turn=="black"):
                if(current_board[p][0]!='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]=='-' ):
                    moves.add(p)
            else:
                if(current_board[p][0]=='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]!='-' ):
                    moves.add(p)   
           
                        
    if(col+1)<105 and row-1>48:       #can move right down
        p=chr(col+1)+chr(row-1)   #right down positon
        if(current_board[p]=='.'):
            moves.add(p)
        else:
            if(turn=="black"):
                if(current_board[p][0]!='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]=='-' ):
                    moves.add(p)
            else:
                if(current_board[p][0]=='-'):  #not own peice
                    moves.add(p) 
                if(condition and current_board[p][0]!='-' ):
                    moves.add(p)   
            
  
    return list(moves)

def return_possible_move_of_given_position(b,turn,Cboard):
    m=[]
    if(turn=="white"):
        if(Cboard[b]=='r'):
            m=rook_possible_move(b,Cboard,False)  
        elif(Cboard[b]=='k'):
            m=king_possible_move(b,Cboard,False, turn)  
        elif(Cboard[b]=='n'):                
            m=knight_possible_move(b,Cboard,False,turn)  
    else:
        if(Cboard[b]=='-n'):
            m=knight_possible_move(b,Cboard,False,turn)  
        elif(Cboard[b]=='-k'):
            m=king_possible_move(b,Cboard,False,turn)  
    return m
    

                
def return_one_side_peice(current_board, turn):
    peices=dict()
    for b in boardIndex:
        if(current_board[b]!='.'):
            if(current_board[b][0]=='-' and turn=="black"): 
                peices[current_board[b]]=b
            if(current_board[b][0]!='-' and turn=="white"): 
                peices[current_board[b]]=b
    return peices
    

        
def check_user_input(a,b,turn):
    if(a not in boardIndex):return False
    if(b not in boardIndex):return False
    target_move=return_possible_move_of_given_position(a,turn,current_board)
    if(turn=="black"):
        if current_board[a][0]=='-' and b in target_move:
            return True
    if (turn=="white"):
        if current_board[a][0]!='-' and current_board[a][0]!='.' and b in target_move:
            return True
    
    #check if can move to the square
    
    return False



    

    





#========================= begin of heuristic of black ======================================


    
def heuristicY(yboard,current_peice_value): #y is black
    #find all peices in board.
    peice_b=return_one_side_peice(yboard, "black")
    peice_w=return_one_side_peice(yboard, "white")
    black_moves=one_side_moves(peice_b, yboard,"black", True)
    white_moves=one_side_moves(peice_w, yboard,"white", False)
    
    if('-k' not in peice_b):
        return -99999
        
    h_value=peiceSquareValue(peice_b,"black")   #find peice position value,  positive
    
    if (boardPeiceValue(peice_b)==current_peice_value):  #peice value, white positive, black negative
        h_value+=5000
    else:
        h_value-=2111
    
    h_value+=(boardPeiceValue(return_one_side_peice(current_board,"white")) - boardPeiceValue(peice_w))
    
    
    #check which peice is attacked by 
    if("-k" in peice_b)  and (peice_b['-k'] in white_moves):
        h_value-=1000 
    else:
        h_value+=200
    if("-n" in peice_b)  and (peice_b['-n'] in white_moves):
        h_value-=200
    else:
        h_value+=200
    #check knight protected by king or at most two squares from king
    if("-n" in peice_b)  and (peice_b['-n'] in black_moves):
        h_value+=knightValue

    return h_value

#========================= end of heuristic of black ======================================

def boardPeiceValue(peices):
    h_value=0
    #black side 
    if("-k" in peices):         
        h_value-=kingValue
    if("-n" in peices):         
        h_value-=knightValue
   #white side
    if("k" in peices):        
        h_value+=kingValue
    if( "n"  in peices):        
        h_value+=knightValue
    if( "r"  in peices): 
        h_value+=rookValue
    return h_value
       
def one_side_moves(peices,xboard, turn,condition):
    one_moves=[]
    #black side 
    if turn=="black":
        if("-k" in peices):         
            one_moves.extend( king_possible_move(peices["-k"], xboard, condition, "black") )        
        if("-n" in peices):         
            one_moves.extend(knight_possible_move(peices["-n"], xboard, condition, "black") )
     
    #white side
    else:
        if("k" in peices):        
            one_moves.extend( king_possible_move(peices["k"], xboard, condition, "white") )
        if( "n"  in peices):        
            one_moves.extend( knight_possible_move(peices["n"], xboard, condition, "white") )  
        if( "r"  in peices):        
            one_moves.extend(rook_possible_move(peices["r"], xboard, condition))      
    return one_moves    
        
        

def peiceSquareValue(peices,turn):
    score=0
    if(turn=="black"):
        if("-k" in peices):
            if peices['-k'][0]!='a' or peices['-k'][0]!='h' or peices['-k'][1]!='1' or peices['-k'][1]!='8':
                score+=50
            else:  
                score-=30
        if("-n" in peices):
            score+=knightSquareValue[peices['-n']]
    else:
        if("k" in peices):
            score+=kingSquareValue[peices['k']]  
        if("n" in peices):
            score+=knightSquareValue[peices['n']]
        if("r" in peices):
            if peices['r'][0]=='a' or peices['r'][0]=='h' or\
             peices['r'][1]=='1' or peices['r'][1]=='8':
                score-=10
    return score

def heuristicX(yboard,current_peice_value): #x is white
    #find all peices in board.
    peice_b=return_one_side_peice(yboard, "black")
    peice_w=return_one_side_peice(yboard, "white")
    black_moves=one_side_moves(peice_b, yboard,"black", False)
    white_moves=one_side_moves(peice_w, yboard,"white", True)
    
    h_value=peiceSquareValue(peice_w,"white")   #find peice position value, white positive, black negative
    h_value+=(current_peice_value-boardPeiceValue(peice_w) )  #peice value, white positive, black negative

 
    h_value+=((boardPeiceValue(peice_b))-boardPeiceValue(return_one_side_peice(current_board,"black")) )
   
    
    #check which peice is attacked by 
    if("k" in peice_w)  and (peice_w['k'] in black_moves):
        h_value-=2000
    if("r" in peice_w)  and (peice_w['r'] in black_moves):
        h_value-=(2*rookValue)  
    if("n" in peice_w)  and (peice_w['n'] in black_moves):
        h_value-=100
    #check defend by own peice
    if("k" in peice_w)  and (peice_w['k'] in white_moves):
        h_value+=300
    if("r" in peice_w)  and (peice_w['r'] in white_moves):
        h_value+=300 
    if("n" in peice_w)  and (peice_w['n'] in white_moves):
        h_value+=150
    #check rook can checkmate
    if('-k' not in peice_b):
        h_value+=5000
    if('-k' in peice_b) and (peice_b['-k'] in white_moves):
        h_value+=2000
    #check knight is 2 square from rook or 3 square from -king
    
    return h_value
    
#============= end of huristic y ======================    
    
#========================== working on here ==========
def optimal_possible_move_of_given_position(b,turn,Cboard):
    m=[]

    col=ord(b[0])
    row=ord(b[1])
    w_peice=return_one_side_peice(Cboard, "white")
    w_moves=one_side_moves(w_peice, Cboard, "white", False)    
    b_peice=return_one_side_peice(Cboard,"black")
    b_moves=one_side_moves(b_peice, Cboard, "black", False)
    if(turn=="white"):
        if(Cboard[b]=='r'):
            n=rook_possible_move(b,Cboard,False) 
            for ch in n:
                if ch not in m:
                    if('-k' in b_peice ):
                        if(b_peice['-k'] in n): 
                            m.append(b_peice['-k'])
                        if(ord(ch[0])==ord(b_peice['-k'][0]) or ord(ch[1])==ord(b_peice['-k'][1]) and ch not in m):m.append(ch)
                        if(ord(ch[0])==(ord(b_peice['-k'][0])-1) or ord(ch[1])==(ord(b_peice['-k'][1])-1) and ch not in m):m.append(ch)
                        if(ord(ch[0])==(ord(b_peice['-k'][0])+1) or ord(ch[1])==(ord(b_peice['-k'][1])+1) and ch not in m):m.append(ch)
                    if('-n' in b_peice) and ch not in m:
                        if(ord(ch[0])==ord(b_peice['-n'][0]) or ord(ch[1])==ord(b_peice['-n'][1])):m.append(ch)
                        
                 
        elif(Cboard[b]=='k'): 
            n=king_possible_move(b,Cboard,False, turn)  
            for ch in n:
                if('-k' in b_peice):#choose king is close to -king and at least 2 square distance
                    if abs(ord(ch[0])-ord(b_peice['-k'][0]))>1:
                        if abs(ord(ch[0])-ord(b_peice['-k'][0]))<abs(col-ord(b_peice['-k'][0])):
                            if ch not in m:m.append(ch)  
                    if abs(ord(ch[1])-ord(b_peice['-k'][1]))>1:                   
                        if abs(ord(ch[1])-ord(b_peice['-k'][1]))<abs(row-ord(b_peice['-k'][1])):
                            if ch not in m:m.append(ch)
                   
                if('-n' in b_peice): #as close as possible to knight
                    if abs(ord(ch[0])-ord(b_peice['-n'][0]))<abs(col-ord(b_peice['-n'][0])):
                        if ch not in m:m.append(ch)                 
                    if abs(ord(ch[1])-ord(b_peice['-n'][1]))<abs(row-ord(b_peice['-n'][1])):
                        if ch not in m:m.append(ch)
             
        elif(Cboard[b]=='n'):             
            n=knight_possible_move(b,Cboard,False,turn)  
            for ch in n:
                if('-k' in b_peice):#choose king is close to -king and at least 2 square distance                
                    if abs(ord(ch[0])-ord(b_peice['-k'][0]))<abs(col-ord(b_peice['-k'][0])):
                        if ch not in m:m.append(ch)              
                    if abs(ord(ch[1])-ord(b_peice['-k'][1]))<abs(row-ord(b_peice['-k'][1])):
                        if ch not in m:m.append(ch)
        for poi in m:
            if poi in b_moves:
                m.remove(poi)         
    else:        
        if(Cboard[b]=='-n'):
            m=knight_possible_move(b,Cboard,False,turn)  
            if('-k' in b_peice):
                for p in m:
                    if (abs(ord(p[0])-ord(b_peice['-k'][0])))>1 or (abs(ord(p[1])-ord(b_peice['-k'][1])))>1:
                        m.remove(p)
        optimal=[]
        if(Cboard[b]=='-k'):
            rt=''
            m=king_possible_move(b,Cboard,False,turn)   
            if 'r' in w_peice:
                
                if w_peice['r'] in m: rt=w_peice['r']
                for poi in m:            
                    if w_peice['r'] != poi:
                        if w_peice['r'][0]== poi[0] or w_peice['r'][1]==poi[1]:
                            m.remove(poi) 
                
            if('-n' in b_peice):
                
                for p in m:
                    if (abs(ord(p[0])-ord(b_peice['-n'][0])))<=1 and (abs(ord(p[1])-ord(b_peice['-n'][1])))<=1:
                        
                        optimal.append(p)
                m=optimal
            if len(rt)==2:m.append(rt)
                        

    return m      

def checking(turn):
#need one side all possible move to check if king's position in these possible movement.
    me=return_one_side_peice(current_board, turn)

    if(turn=="white"):
        peices=return_one_side_peice(current_board, "black")
        foe=one_side_moves(peices,current_board, "black", False)
        if me['k'] in foe:return True
        else:return False
    else:
        peices=return_one_side_peice(current_board, "white")
        foe=one_side_moves(peices,current_board, "white", False)
        if me['-k'] in foe:return True
        else:return False
    return False

def checkmate(turn):
#need one side all possible move to check if king's position in these possible movement.
    
    
    if(turn=="white"):
        me=return_one_side_peice(current_board, "black")
        if('-k' not in me): return True
        peices=return_one_side_peice(current_board, "white")
        m=king_possible_move(me['-k'],current_board,False,"black")
                
        mymoves=one_side_moves(peices,current_board, "white", False)
        for km in m:
            if km not in mymoves:
                return False
        return True
    else:
        me=return_one_side_peice(current_board, "white")
        if('k' not in me): return True
        peices=return_one_side_peice(current_board, "black")
        m=king_possible_move(me['k'],current_board,False,"white")                
        mymoves=one_side_moves(peices,current_board, "black", False)
        for km in m:
            if km not in mymoves:
                return False
        return True


def minMax(mboard, turn, opponent):    
    max1=-99999
    min2=99999
    max3=-99999
    min4=99999
    max5=-99999
    move_choice=[]
    t=-998
    #get current peice in board, find states
    allmoves=[]
    level1=return_one_side_peice(mboard,turn) 
    current_peice_value=boardPeiceValue(level1)
    cm=False
    for p in level1:
        if checking(turn): #if checkmate, only to move king
            cm=True
            print("check.........")
            if(turn=="black"):p='-k'
            if(turn=="white"):p='k'

        for q in optimal_possible_move_of_given_position(level1[p],turn,mboard): 
            
            nboard=mboard.copy()
            move(level1[p],q,nboard)            
            level2=return_one_side_peice(nboard,opponent)
            for x1 in level2: 
                levelmove2=optimal_possible_move_of_given_position(level2[x1],opponent,nboard)
                for y1 in levelmove2:                                           
                    oboard=nboard.copy()                   
                    move(level2[x1],y1,oboard)                 
                    level3=return_one_side_peice(oboard,turn)
                    for x2 in level3:
                        for y2 in optimal_possible_move_of_given_position(level3[x2],turn,oboard):
                            pboard=oboard.copy()
                            move(level3[x2],y2,pboard)                            
                            level4=return_one_side_peice(pboard,opponent)
                            for x3 in level4:
                                level4move=optimal_possible_move_of_given_position(level4[x3],opponent,pboard)
                                for y3 in level4move:                  
                                    qboard=pboard.copy()
                                    move(level4[x3],y3,qboard)                                    
                                    level5=return_one_side_peice(qboard,turn)
                                    for x4 in level5:
                                        #print("p=",p," h value=", end=" ")
                                        for y4 in optimal_possible_move_of_given_position(level5[x4],turn,qboard): 
                                            rboard=qboard.copy()
                                            move(level5[x4],y4,rboard)                                             
                                            
                                            if(turn=="white"):      #using black h function
                                                h=heuristicX(rboard,current_peice_value)
                                                max5=max(max5,h)
                                                #print(h,end=" ")
                                            if(turn=="black"):    #using white heuristic function
                                                h=heuristicY(rboard,current_peice_value)
                                                if h>5000: max5=max(max5,h)
                                        #print('')
                                        
                                    min4=min(min4,max5)
                            max3=max(max3,min4)
                    min2=min(min2,max3)            
            max1=max(max1,min2)
            #print("max1=",max1," min2=",min2," max3=",max3," min4=",min4," max5=",max5)
            #input("one option")
            #print("p=",p," ",level1[p]," h=", max1)
            temp_list=[]
            if(t!=max1):
                if(print_switch):print("max1=",max1, " a=",p," b=",q)
                temp_list.append(level1[p])
                temp_list.append(q) 
                move_choice=temp_list
            t=max1
            if(max1==min2):
                tlist=[p,level1[p],q,max1]
                if tlist not in allmoves:allmoves.append(tlist)
        #input("in third level...")
        if(cm):break  
    max1=-99999
    
    oc=[]
    for am in allmoves:
        sboard=mboard.copy()
        move(am[1],am[2],sboard)                                             
        
        if(turn=="white"):      #using black h function
            h=heuristicX(sboard,current_peice_value)
            if(max1<h):
                max1=h
                tempoc=[]
                tempoc.append(am[1])
                tempoc.append(am[2])
                oc=tempoc
            #print("move ",am, " h=",h)
        if(turn=="black"):    #using white heuristic function
            h=heuristicY(sboard,current_peice_value)
            if(max1<h):
                max1=h
                tempoc=[]
                tempoc.append(am[1])
                tempoc.append(am[2])
                oc=tempoc
            #print("move ",am, " h=",h)
    move_choice=oc
    return move_choice     


def return_position_peice(b):
    p=""
    if(current_board[b]=='r'): p='R:'
    if(current_board[b]=='k'): p='K:'
    if(current_board[b]=='n'): p='N:'
    if(current_board[b]=='-n'): p='N:'
    if(current_board[b]=='-k'): p='K:'
    return p
    
def log(string, turn):
    if(turn=="white"):
        if not os.access("log_X.txt", os.W_OK):             
            print("file is open,cannot write")
            time.sleep(2)
            log(string,turn)
        else:
            with open("log_X.txt", 'a') as logfile:
                logfile.write(string)

    else:
        if not os.access("log_Y.txt", os.W_OK):            
            
            print("file is open,cannot write")
            time.sleep(2)
            log(string,turn)
        else:
            with open("log_Y.txt", 'a') as logfile:               
                logfile.write(string)
            
def findPosion(peice,turn):
    allpeice=return_one_side_peice(current_board,turn)
    return allpeice[peice]
    
def readMove(turn, steps):  #check if the index equal current step number.
    #print("in read move, step is:",steps)
    rms=[]        
    line=""
    if(turn=="white"):
        if not os.access("log_X.txt", os.W_OK):
            time.sleep(2)
            readMove(turn, steps)
        else:
            with open("log_X.txt", 'r') as logfile:
                for line in logfile:
                    pass
                #print("line is:",line)
                if(len(line)>5):
                    a=line.split(" ")
                    if(a[0]==str(steps)):
                        a=a[1].split(':')       ##1 X:K:g2\n
                        if(a[1]=='K'):rms.append(findPosion('k',turn))
                        if(a[1]=='N'):rms.append(findPosion('n',turn))
                        if(a[1]=='R'):rms.append(findPosion('r',turn))
                        rms.append(a[2])
                        return rms
            
            
    else:
        if not os.access("log_Y.txt", os.W_OK):
            time.sleep(2)
            readMove(turn, steps)
        else:
            with open("log_Y.txt", 'r') as logfile:
                for line in logfile:
                    pass
                if(len(line)>5):
                    a=line.split(" ")
                    if(a[0]==str(steps)):
                        a=a[1].split(':')       ##1 X:K:g2\n
                        if(a[1]=='K'):rms.append(findPosion('-k',turn))
                        if(a[1]=='N'):rms.append(findPosion('-n',turn))
                        rms.append(a[2])
                        return rms
           
    time.sleep(2)
    readMove(turn,steps)
    
    
def move(a,b,Cboard):       
    Cboard[b]=Cboard[a]
    Cboard[a]='.'
def showMove(a,b,Cboard):
    print("move from ",a, " to ",b)
    displayDict(Cboard) 
    return
         
def play(counter):
    logX="log_X.txt"
    logY="log_Y.txt"
    
    while(True):
        turn="white"
        opponent="black"
        print("please choose black or white: \n \
input 'b' for black, or 'w' for white:")
        player=input()
        
        if(player=='b'):
            print("you choose black, white move first")
            pc=turn
            with open(logX,'w') as empty:   #clean file
                print(" ")
                break
        if(player=='w'):
            print("you choose white, you move first")
            pc=opponent  
            with open(logY,'w') as empty:  #clean file
                print(" ")          
            break
        print("wrong input")
    
    displayDict(current_board)
    
    steps=1
    logtext=""
    moveone=""
    if(pc==opponent): #player choose white
        while steps<counter:          
            #if foe choose white. then I need to read the logx.file to make a move.
            print("round ",steps," turn =", turn)   
            input("enter to read from text file")          
            print("getting move from log_X.txt")
            Xmove=readMove(turn,steps)
            
            a=Xmove[0]
            b=Xmove[1][:2]
            
            moveone=return_position_peice(a)
            logtext=""+str(steps)+" X:"+moveone+b+"\n"      #1 X:K:g2\n            
            log(logtext,turn)
            
            print("a=",current_board[a]," b=",len(b))
            move(a,b,current_board)
            showMove(a,b,current_board)
            if checkmate(turn): 
                input("checkmate")
                logtext="game result: white win\n"      #1 X:K:g2\n           
                log(logtext,turn)
                log(logtext,opponent)
                return
                
            turn,opponent=opponent,turn 
            steps+=1
            
            #===============================================
            print("round ",steps," turn =", turn)
            choice=minMax(current_board, turn, opponent)
            
            moveone=return_position_peice(choice[0])            
            logtext=str(steps)+" Y:"+moveone+choice[1]+"\n"      #2 Y:K:g2\n
            log(logtext, turn)
            #log(logtext, opponent)            
            
            move(choice[0],choice[1],current_board)
            showMove(choice[0],choice[1],current_board)
            if checkmate(turn): 
                input("checkmate")
                logtext="game result: black win\n"      #1 X:K:g2\n           
                log(logtext,turn)
                log(logtext,opponent)
                return
            turn,opponent=opponent,turn  
            steps+=1
    else:
        while steps <counter:
            print("round ",steps," turn =", turn)
            choice=minMax(current_board, turn, opponent)
            
            moveone=return_position_peice(choice[0])            
            logtext=str(steps)+" X:"+moveone+choice[1]+"\n"      #1 X:K:g2\n
            log(logtext, turn)
            #log(logtext, opponent)
                 
            steps+=1
            
            move(choice[0],choice[1],current_board)
            showMove(choice[0],choice[1],current_board)
            if checkmate(turn): 
                input("checkmate")
                logtext="game result: white win\n"      #1 X:K:g2\n           
                log(logtext,turn)
                log(logtext,opponent)
                return
            turn,opponent=opponent,turn 
            
            print("round ",steps," turn =", turn)  
            input("enter to read from text file")
                       
            print("getting move from log_Y.txt")
            Xmove=readMove(turn,steps)
            a=Xmove[0]
            b=Xmove[1][:2]
            
            moveone=return_position_peice(a)
                   
            logtext=str(steps)+" Y:"+moveone+b+"\n"      #1 X:K:g2\n           
            log(logtext,opponent)
            
            print("a=",current_board[a]," b=",len(b))
            
            steps+=1            
            move(a,b,current_board)
            showMove(a,b,current_board)
            if checkmate(turn): 
                input("checkmate")
                logtext="game result: black win\n"      #1 X:K:g2\n           
                log(logtext,turn)
                log(logtext,opponent)
                return
            turn,opponent=opponent,turn 
    logtext="game result: withdraw\n"      #1 X:K:g2\n           
    log(logtext,turn)
    log(logtext,opponent)
knightValue=320
rookValue=500
kingValue=32767    
boardIndex=chessboardIndex()   #a1,a2... b1, b2...
knightSquareValue=knightTable(boardIndex)
kingSquareValue=kingTable(boardIndex)

white_chess=[".",".", ".", ".", "k", ".", "n", "r"]#initial positon
black_chess=[".",".", "-n", ".", "-k", ".", ".", "."]

board= setupChessboard(white_chess, black_chess)        #board initial.
current_board=assignValue(boardIndex, board)
print_switch=False


def main():

    

    
    '''
    if not os.access(logX, os.W_OK):
        print("file is open")
    else:
        print("file is closed")
    

    input("pause...")  #variable=line.split(' ')
    '''

  
    

    step_counter=0
    while(True ):
        try:
            step_counter=int(input("enter an even number of steps,(maximum 50):"))
        except ValueError:
            print("input integer only")
            continue
        else:
            if(step_counter <6 or step_counter>80 or step_counter%2==1):
                print("not even number or range out of 5-75")
            else:                
                break
    
    #displayBoard(board)
    #displayDict(current_board) 
    
    if step_counter>75 or step_counter<5:step_counter=35
    
    play(step_counter)    

 

if __name__=="__main__":
    main()

    
    


