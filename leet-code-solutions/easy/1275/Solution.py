from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        bord = [" "] * 9
        for i in range(len(moves)):
            idx = self.map_to_index(moves[i])
            player_sign = "A" if i % 2 == 0 else "B"
            bord[idx] = player_sign
        return self.check_for_winner(bord, player_sign)


    def map_to_index(self, pair: List[int]):
        if pair == [0,0]: return 0
        elif pair == [0,1]: return 1
        elif pair == [0,2]: return 2
        elif pair == [1,0]: return 3
        elif pair == [1,1]: return 4
        elif pair == [1,2]: return 5
        elif pair == [2,0]: return 6
        elif pair == [2,1]: return 7
        elif pair == [2,2]: return 8
    

    def check_for_winner(self, b: List[int], player_sign: str):
        # check for rows
        if b[0]==b[1]==b[2]==player_sign or \
           b[3] == b[4] == b[5] == player_sign or \
           b[6] == b[7] == b[8] == player_sign:
            return player_sign
        # check for columns
        if b[0]==b[3]==b[6]==player_sign or \
           b[1] == b[4] == b[7] == player_sign or \
           b[2] == b[5] == b[8] == player_sign:
            return player_sign
        # check for diagonal
        if b[0] == b[4] == b[8] == player_sign or \
           b[2] == b[4] == b[6] == player_sign:
            return player_sign
        no_moves_flag = True
        for i in b:
            if i == " ":
                no_moves_flag = False
        if no_moves_flag:
            return "Draw"
        else:
            return "Pending"

    def print_bord(self, b: List[int]):
        print(f" {b[0]} | {b[1]} | {b[2]} ")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]} ")



x = Solution()
print(x.tictactoe(moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]) == "A")
print(x.tictactoe(moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]) == "B")
print(x.tictactoe(moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]) == "Draw")
        