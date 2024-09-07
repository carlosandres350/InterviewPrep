class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        boxRow = len(box)
        boxCol = len(box[0])
        # init response array with the rows and columns inverted from the given box
        # the rows will equal the boxCol and the cols will equal boxRow
        res = [['.'] * boxRow for i in range(boxCol)]
        print(res)

        # 0, 0 becomes 0, 1
        # 1, 0 becomes 0, 0
        
        #keys :
        # '#' a stone, that will fall from gravity
        # '*' a stationary obstacle, that will hold stones
        # '.' empty square
        #iterate through the box and shift stones from left to right starting at the end of the row
        for r in range(boxRow):
            for c in range(boxCol -1 , -1, -1):
                #if there is a stone, shift it completely right until we hit end of matrix or an obstacle
                if box[r][c] == '#':
                    self.shiftRight(box, r, c)
        print(box)
        #rotate the box
        # for 
        #     for c in range(boxRow):
        #         #the first row , becomes the last column
        #         # the first column becomes the the first row
        #         res[r][c] = box[r][c]

        for row in range(len(res)):
            for col in range(len(res[row])):
                res[row][col] = box[col][row]
        

 
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
                return 
            #check if we can shift right, or there is an open sqaure
            elif box[r][i+1] != '.':
                box[r][i] = '#'
                return

