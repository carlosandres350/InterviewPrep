class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        boxRow = len(box)
        boxCol = len(box[0])
        res = [['.'] * boxRow for r in range(boxCol)]

        #keys :
        # '#' a stone, that will fall from gravity
        # '*' a stationary obstacle, that will hold stones
        # '.' empty square
        #iterate through the box and shift stones from left to right starting at the end of the row
        for r in range(boxRow):
            for c in range(boxCol -1 , -1, -1):
                #if there is a stone, shift it completely right until we hit end of matrix or an obstacle
                if box[r][c] == '#':
                    box = self.shiftRight(box, r, c)

        
        #rotate the box
        for i in range(boxRow):
            for j in range(boxCol):
                res[j][boxRow - i - 1] = box[i][j]
        
 
        return res

    def shiftRight(self, box, r, c):
        #[.  X  .  X]
        #remove current square location
        box[r][c] = '.'
        #shift a rock all the way right until we hit end of matrix or an obstacle 
        for i in range(c, len(box[r])):
            #check if were already at the last index
            if i == len(box[r]) -1:
                box[r][i] = '#'
                return box
            #check if we can shift right, or there is an open sqaure
            elif box[r][i+1] != '.':
                box[r][i] = '#'
                return box


                




        