#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_board(val):
    print(val[1]+ '|' + val[2]+ '|' + val[3])
    print("------")
    print(val[4]+ '|' + val[5]+ '|' + val[6])
    print("------")
    print(val[7]+ '|'  +val[8]+ '|' +val[9])


# In[2]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[3]:


def player_input():
    choice = 'wrong'
    
    while choice not in ['X','O']:
        
         choice = input("Player1 please select X OR O: ")
            
         if choice not in ['X','O']:
                print("Sorry invalid choice!")
        
        
    return choice


# In[4]:


player_input()


# In[5]:


def position_choice():
    
    position = 'wrong'
    
    while position not in [1,2,3,4,5,6,7,8,9]:
        
        position = int(input("Enter a position you want to pick(1-9): "))
        
        if  position not in [1,2,3,4,5,6,7,8,9]:
            print ("Please enter a valid position!")
            
            
    return position
    
##board[position] = player_input()


# In[6]:


position_choice()


# In[7]:


def place_marker(board, choice, position):
    
    board[position]= choice


# In[8]:


place_marker(test_board, 'O', 5)
display_board(test_board)


# In[9]:


def win_check(board, mark):
    
    return ((board[1] == mark) and (board[2] == mark) and (board[3] == mark) or 
       (board[4] == mark) and (board[5] == mark) and (board[6] == mark) or
       (board[7] == mark) and (board[8] == mark) and (board[9] == mark) or
       (board[1] == mark) and (board[4] == mark) and (board[7] == mark) or 
       (board[2] == mark) and (board[5] == mark) and (board[8] == mark) or 
       (board[3] == mark) and (board[6] == mark) and (board[9] == mark) or 
       (board[1] == mark) and (board[5] == mark) and (board[9] == mark) or 
       (board[3] == mark) and (board[5] == mark) and (board[7] == mark))
        


# In[10]:


win_check(test_board, "X")


# In[11]:


import random

def choose_first():
      if random.randint(0, 1) == 0:
        return 'Player 2'
      else:
        return 'Player 1'


# In[12]:


def space_check(board, position):
    
    if board[position] == ' ':
        return True
    else:
        return False


# In[13]:


def full_board_check(board):
    
    for x in range(1,9):
        if space_check(board, x):
            return False
    return True
       


# In[14]:


full_board_check(test_board)


# In[15]:


test_board


# In[16]:


full_board_check(test_board)


# In[17]:


def replay():
    
     return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[19]:


print('Welcome to Tic Tac Toe!')

while replay() == True:
        game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        display_board(game_board)
        
        mark_player1 = player_input()
        
        if mark_player1 == 'X':
            mark_player2 == 'O'
        else:
            mark_player2 == 'X'
            
        turn = choose_first()  
        print(turn + ' will go first.')
    
        play_game = input('Are you ready to play? Enter Yes or No.')
    
        if play_game.lower()[0] == 'y':
             game_on = True
        else:
            game_on = False

            
        while game_on:
            if turn == 'Player 1':
           
                 display_board(game_board)
                 position = position_choice()
                 place_marker(game_board, mark_player1, position)

                      if win_check(game_board, mark_player1):
                            display_board(game_board)
                            print('Congratulations! Player 1  won the game!')
                            game_on = False
                    else:
                            if full_board_check(game_board):
                                display_board(game_board)
                                print('The game is a draw!')
                                break
                            else:
                                 turn = 'Player 2'

        
          
        
            else:
                    display_board(game_board)
                    position = position_choice()
                    place_marker(game_board,mark_player2, position)

                    if win_check(game_board, mark_player2):
                            display_board(game_board)
                            print('Player 2 has won!')
                            game_on = False
                    else:
                        if full_board_check(game_board):
                                display_board(game_board)
                                print('The game is a draw!')
                                break
                        else:
                            turn = 'Player 1'


        if not replay():
        break
      


# In[20]:


print('Welcome to Tic Tac Toe !!')

while True:
    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(game_board)
        
    mark_player1 = player_input()
    mark_player2 = "q"
        
    if mark_player1 == 'X':
            mark_player2 == 'O'
    else:
            mark_player2 == 'X'
            
    turn = choose_first()  
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
        
    if play_game.lower()[0] == 'y':
             game_on = True
    else:
            game_on = False
            
    while game_on:
            if turn == 'Player 1':
                display_board(game_board)
                position = position_choice()
                place_marker(game_board, mark_player1, position)
                
                if win_check(game_board, mark_player1):
                        display_board(game_board)
                        print('Congratulations! Player 1  won the game!')
                        game_on = False
                            
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print('The game is a draw!')
                        break
                    else:
                         turn = 'Player 2'
                            
                            
            else:
                display_board(game_board)
                position = position_choice()
                place_marker(game_board,mark_player2, position)
                    
                if win_check(game_board, mark_player2):
                             display_board(game_board)
                             print('Player 2 has won!')
                             game_on = False
                             
                else:
                         if full_board_check(game_board):
                                display_board(game_board)
                                print('The game is a draw!')
                                break
                                
                         else:
                            turn = 'Player 1'

                            
    if not replay():
                     break
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




