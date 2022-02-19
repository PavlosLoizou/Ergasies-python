# __Global Var__
import random

move = 0
sum = 0

board = ["*", "*", "*",
         "*", "*", "*",
         "*", "*", "*"]



for i in range(100):

 sum = sum + move


 game_still_going = True

 move = 0

 board = ["*", "*", "*",
          "*", "*", "*",
          "*", "*", "*"]





 def play_game():


         while game_still_going:
             handle_turn()

             check_if_game_over()


 def handle_turn():

#βάζω σε τυχαία θέση
     position = random.randint(0, 8)
#εαν δεν υπάρχει καπάκι βάζω τυχαίω
     if board[position] == "*":

         kapakia = ['1', '2', '3']


         board[position] = random.choice(kapakia)

         kinisis()

#εαν ειναι ο πιο μικρός μπορώ να βάλω μεγάλο η μεσσαίο
     elif board[position] == '1':

         kapakia1 = ['2', '3']

         board[position] = random.choice(kapakia1)

         kinisis()

#εαν υπάρχει ο μεσαίος τοτε μπορώ να βάλω  μεγάλο

     elif board[position] == '2':


         board[position] = '3'
         kinisis()





 def check_if_game_over():
     check_win()


 def check_win():
     check_rows()

     check_columns()

     check_diagonals()

     return


 def check_rows():

     global game_still_going

     row_1 = board[0] == board[1] == board[2] != "*"
     row_2 = board[3] == board[4] == board[5] != "*"
     row_3 = board[6] == board[7] == board[8] != "*"
     if row_1 or row_2 or row_3:
         game_still_going = False
     elif board[0] == '1' and board[1] == '2' and board[2] == '3':
         game_still_going = False
     elif board[3] == '1' and board[2] == '2' and board[1] == '3':
         game_still_going = False
     elif board[3] == '1' and board[4] == '2' and board[5] == '3':
         game_still_going = False
     elif board[5] == '1' and board[4] == '2' and board[3] == '3':
         game_still_going = False
     elif board[0] == '1' and board[1] == '2' and board[2] == '3':
         game_still_going = False
     elif board[3] == '1' and board[2] == '2' and board[1] == '3':
         game_still_going = False

     return


 def check_columns():

     global game_still_going

     col_1 = board[0] == board[3] == board[6] != "*"
     col_2 = board[1] == board[4] == board[7] != "*"
     col_3 = board[2] == board[5] == board[8] != "*"
     if col_1 or col_2 or col_3:
         game_still_going = False
     elif board[0] == '1' and board[3] == '2' and board[6] == '3':
         game_still_going = False
     elif board[6] == '1' and board[3] == '2' and board[0] == '3':
         game_still_going = False
     elif board[1] == '1' and board[4] == '2' and board[7] == '3':
         game_still_going = False
     elif board[7] == '1' and board[4] == '2' and board[1] == '3':
         game_still_going = False
     elif board[2] == '1' and board[5] == '2' and board[8] == '3':
         game_still_going = False
     elif board[8] == '1' and board[5] == '2' and board[2] == '3':
         game_still_going = False

     return


 def check_diagonals():

     global game_still_going

     diag_1 = board[0] == board[4] == board[8] != "*"
     diag_2 = board[6] == board[4] == board[2] != "*"

     if diag_1 or diag_2:
         game_still_going = False
     elif board[0] == '1' and board[4] == '2' and board[8] == '3':
         game_still_going = False
     elif board[8] == '1' and board[4] == '2' and board[0] == '3':
         game_still_going = False
     elif board[2] == '1' and board[4] == '2' and board[6] == '3':
         game_still_going = False
     elif board[6] == '1' and board[4] == '2' and board[2] == '3':
         game_still_going = False

     return


 def kinisis():

     global move
     move = move + 1

     return

 play_game()


avg = sum/100
print("Average moves Per Game: ")
print(int(avg))
