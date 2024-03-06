from cgitb import text
from gc import disable, enable
from tracemalloc import start
import game
import helpers
from tkinter import *



# def format_board(board):
#     size = len(board)
#     line = f'\n  {"+".join("-" * size)}\n'
#     rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
#     return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'

# def play_move(board, player):
#     print(f'{player} to play:')
#     row = int(input()) - 1
#     col = int(input()) - 1
#     board[row][col] = player
#     print(format_board(board))

def on_click(button_name, player):
    if player == 'Player1':
        player = 'X'
    elif player == 'Player1':
        player = 'O'
        
    if button_name == 'first_button':
        first_button.configure(text = player,state = DISABLED)
        print()



def play_game(board_size, player1, player2):
    is_draw = True
    rounds = board_size * board_size
    current_player.set(player1)
    first_button['state'] = NORMAL

    #board = helpers.make_board(board_size)
    #print(format_board(board))
    
    # for _ in range(rounds):
    #    # play_move(board, current_player)
        
    #  #   if helpers.winner(board):
    #         helpers.print_winner(current_player)
    #         is_draw = False
    #         break
        
    #     if current_player == player1:
    #         current_player = player2
    #     elif current_player == player2:
    #         current_player = player1
    # if is_draw:            
    #     helpers.print_draw()


def start_game():
    print('BoardSize: 3x3')
   # res = f'The size of the board is: {txt_size_board.get()} x {txt_size_board.get()}'
   # lbl_size_board.configure(text = res)
    play_game(helpers.BOARDSIZE,helpers.PLAYER1,helpers.PLAYER2)


if __name__ == '__main__':

    #Widget
    root = Tk()
    root.title('Tic-Tac-Toe-Game')
   # root.geometry('350x400')
    root.iconbitmap('favicon.ico')
    
    current_player = StringVar()
    current_player.set('Current Player')

    game_label = Label(root, text='Tic Tac Toe Game')
    game_label.grid(row=0,column=1)

    # board_size_label = Label(root, text='Choose the Size of the Board')
    # board_size_label.grid(row=0,column=5)
    # board_size_entry = Entry(root, width = 20, fg = 'red')
    # board_size_entry.grid(row=0,column=6)
    # board_size_button = Button(root, text='Enter', command= start_game)
    # board_size_button.grid(row=0,column=7)

    first_button = Button(root, text=' ',padx=40,pady=70,fg='black',state= DISABLED,
                           command=lambda: on_click('first_button',current_player.get()))
    first_button.grid(row=1,column=0)
    second_button = Button(root, text=' ',padx=40,pady=70,fg='black')
    second_button.grid(row=1,column=1)
    three_button = Button(root,text=' ',padx=40,pady=70,fg='black')
    three_button.grid(row=1,column=2)
    four_button = Button(root, text=' ',padx=40,pady=70,fg='black')
    four_button.grid(row=2,column=0)
    five_button = Button(root, text=' ',padx=40,pady=70,fg='black')
    five_button.grid(row=2,column=1)
    six_button = Button(root, text=' ',padx=40,pady=70,fg='black')
    six_button.grid(row=2,column=2)
    seven_button = Button(root, text=' ',padx=40,pady=70,fg='black')
    seven_button.grid(row=3,column=0)
    eight_button = Button(root, text=' ',padx=40,pady=70,fg='black')
    eight_button.grid(row=3,column=1)
    nine_button = Button(root, text=' ',padx=40,pady=70,fg='black')
    nine_button.grid(row=3,column=2)
    
    start_button = Button(root, text='Start',padx=30,background='green',command= start_game)
    start_button.grid(row=4,column=1)
    exit_button = Button(root, text='Exit',padx=30,background='red', command= root.quit)
    exit_button.grid(row=4,column=0)
    current_player_label = Label(root,textvariable = current_player)
    current_player_label.grid(row=4,column=2)


    root.mainloop()
   
