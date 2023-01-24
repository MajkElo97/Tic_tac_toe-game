import numpy as np
from random import choice, randint

#### V2 ####
def computer_choice():
    marked = False
    while not marked:
        location = choice(available_positions)
        print(location)
        if signs[location[0], location[1]] == " ":
            signs[location[0], location[1]] = "O"
            available_positions.remove(location)
            marked = True


def check_for_win(sign):
    count_diag = (np.diag(signs) == sign).sum()
    count_sec_diag = (np.diag(np.fliplr(signs)) == sign).sum()
    for i in range(3):
        count_row = (signs[i] == sign).sum()
        count_column = (signs[:, i] == sign).sum()
        if count_row == 3 or count_column == 3 or count_diag == 3 or count_sec_diag == 3:
            print(f"'{sign}' win!!!")
            print_board()
            return False
    return True


def print_board():
    board = f"""{signs[0, 0]} | {signs[0, 1]} | {signs[0, 2]}
---------
{signs[1, 0]} | {signs[1, 1]} | {signs[1, 2]}
---------
{signs[2, 0]} | {signs[2, 1]} | {signs[2, 2]}
---------"""
    print(board)


available_positions = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
signs = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])


game_is_on = True
while game_is_on:
    print_board()
    print("Choose where you want to put a 'X'")
    user_row = int(input("row (0-2): "))
    user_column = int(input("column (0-2): "))
    if [user_row, user_column] in available_positions:
        signs[user_row, user_column] = "X"
        available_positions.remove([user_row, user_column])
        game_is_on = check_for_win("X")
        if game_is_on:
            if (signs == " ").sum() == 0:
                game_is_on = False
                print("Game over!")
                print_board()
            else:
                computer_choice()
                game_is_on = check_for_win("O")
    else:
        print("This place is occupied, try another!")


#### V1 ####
# def computer_choice():
#     marked = False
#     while not marked:
#         row = randint(0, 2)
#         column = randint(0, 2)
#         if signs[row, column] == " ":
#             signs[row, column] = "O"
#             marked = True
#
#
# def check_for_win(sign):
#     count_diag = (np.diag(signs) == sign).sum()
#     count_sec_diag = (np.diag(np.fliplr(signs)) == sign).sum()
#     for i in range(3):
#         count_row = (signs[i] == sign).sum()
#         count_column = (signs[:, i] == sign).sum()
#         if count_row == 3 or count_column == 3 or count_diag == 3 or count_sec_diag == 3:
#             print(f"'{sign}' win!!!")
#             print_board()
#             return False
#     return True
#
#
# def print_board():
#     board = f"""{signs[0, 0]} | {signs[0, 1]} | {signs[0, 2]}
# ---------
# {signs[1, 0]} | {signs[1, 1]} | {signs[1, 2]}
# ---------
# {signs[2, 0]} | {signs[2, 1]} | {signs[2, 2]}
# ---------"""
#     print(board)
#
#
# available_positions = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
# signs = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
#
# game_is_on = True
# while game_is_on:
#     print_board()
#     print("Choose where you want to put a 'X'")
#     user_row = int(input("row (0-2): "))
#     user_column = int(input("column (0-2): "))
#     if signs[user_row, user_column] == " ":
#         signs[user_row, user_column] = "X"
#         game_is_on = check_for_win("X")
#         if game_is_on:
#             if (signs == " ").sum() == 0:
#                 game_is_on = False
#                 print("Game over!")
#                 print_board()
#             else:
#                 computer_choice()
#                 game_is_on = check_for_win("O")
#     else:
#         print("This place is occupied, try another!")


