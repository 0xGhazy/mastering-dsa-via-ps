class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0,0]
        # go to north if get G it will increment the y coordinate by 1
        direction = [0, 1]
        for i in range(4):
            for instruction in instructions:
                if instruction == "G":
                    pos[0] += direction[0]
                    pos[1] += direction[1]
                elif instruction == "L":
                    direction = [-direction[1], direction[0]]
                elif instruction == "R":
                    direction = [direction[1], -direction[0]]
        # check if we stay in the same point
        return pos == [0, 0]




## old answer
# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         cp = [0, 0]                 # current position
#         if instructions == "GL" or instructions == "LG" or \
#            instructions == "GR" or instructions == "RG":
#             return True
#         current_direction = "North"
#         for instruction in instructions:
#             if instruction != 'G':
#                 current_direction = self.get_direction(current_direction, instruction)
#             if instruction == 'G':
#                 if current_direction == "North":
#                     cp[0], cp[1] = cp[0]+1, cp[1]+1
#                 elif current_direction == "West":
#                     cp[0], cp[1] = cp[0]-1, cp[1]+1
#                 elif current_direction == "East":
#                     cp[0], cp[1] = cp[0]+1, cp[1]-1
#                 elif current_direction == "South":
#                     cp[0], cp[1] = cp[0]-1, cp[1]-1
        
#         if cp[0] == 0 and cp[1] == 0 or current_direction != "North":
#             return True
#         return False

#     def get_direction(self, current_direction: str, instruction: str):
#         if current_direction == "North":
#             if instruction == "L":
#                 return "West"
#             elif instruction == "R":
#                 return "East"
#         if current_direction == "West":
#             if instruction == "L":
#                 return "South"
#             elif instruction == "R":
#                 return "North"
#         if current_direction == "East":
#             if instruction == "L":
#                 return "South"
#             elif instruction == "R":
#                 return "North"
#         if current_direction == "South":
#             if instruction == "L":
#                 return "East"
#             elif instruction == "R":
#                 return "West"


x = Solution()
print(x.isRobotBounded("GGLLGG") == True) # == True
print(x.isRobotBounded("GG") == False)
print(x.isRobotBounded("GL") == True)
print(x.isRobotBounded("GLGLGGLGL") == False)