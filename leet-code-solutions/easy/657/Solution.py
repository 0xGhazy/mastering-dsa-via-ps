class Solution:
    def judgeCircle(self, moves: str) -> bool:
        current_pos = [0, 0]
        for move in moves:
            if move == 'U':
                current_pos[0] += 1
            elif move == 'D':
                current_pos[0] -= 1
            elif move == 'L':
                current_pos[1] -= 1
            else:
                current_pos[1] += 1
        return current_pos == [0, 0]