"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cx,co=0,0
    for i in board:
        for j in i:
            if j == X :
                cx+=1
            elif j ==O :
                co+=1
    if cx>co:
        return O
    elif co>cx:
        return X
    else :
        return X

    
    raise NotImplementedError


def actions(board):
    possible_action=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                possible_action.add((i,j))
    print(possible_action)
    return possible_action

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j=action
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or i==None or j==None:
        raise IndexError("Action is out of bounds")
    
    res_board = deepcopy(board)
    res_board[i][j]=player(board)
    return res_board


    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    plays = X if player(board) == O else O
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    
    return None


    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    if len(actions(board))==0:
        return True
    
    return False
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board)==O:
        return -1
    
    return 0
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board"""
    curr=player(board)
    act=None
    if terminal(board):
        return None
    if curr == X:
        _,act=maxvalue(board)

    else:
        _,act=minvalue(board)

    return act
    raise NotImplementedError

def maxvalue(board):
    if terminal(board):
        return utility(board),None
    mov =None
    v=float('-inf')
    for action in actions(board):
        val,act=minvalue(result(board,action))
        if val>v:
            v=val
            mov=action
            if v==1:
                return (v,mov)
    return (v,mov)

def minvalue(board):
    if terminal(board):
        return utility(board),None
    v=float('inf')
    mov=None
    for action in actions(board):
        val,act=maxvalue(result(board,action))
        if val<v:
            v=val
            mov=action
            if v==-1:
                return (v,mov)
    return (v,mov)
        





