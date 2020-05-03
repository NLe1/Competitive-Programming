# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """

class Solution:
    def cleanRoom(self, robot: Robot):
        # direction top,right,down,left
        dir = [(-1,0), (0,1), (1,0), (0,-1)]
        visited = set()
        def go_back():
            robot.turnRight()
            robot.right()
            robot.turnRight()
            robot.turnRight()
            robot.turnRight()

        # @param(cell) is the position of the current cell
        # @param(dir) is the direction it take place
        def backtrack(cell = (0,0), d = 0):
            robot.clean()
            visited.add(cell)
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + dir[new_d][0], cell[1] + dir[new_d][1])
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                robot.turnRight()
        backtrack()

