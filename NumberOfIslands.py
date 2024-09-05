class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        #iterate through the grid and look for islands '1'
        for r in range(len(grid)):
            for c in range(len(grid[row])):
                if grid[r][c] == '1':
                    #call recursive helper function to convert all connected pieces of the island to water, as to not           recount each island
                    sinkIsland(grid, r, c):
                    #increment islands count
                    islands += 1

        return islands


    def sinkIsland(grid, r, c):
        #recursive break case
        #check that coordinates are within bounds of grid and does not equal a "1"
        if r < 0 or r >= len(r) or c < 0 or c > len(grid[r]) or grid[r][c] != '1':
            return

        #set island square to 0
        sinkIsland(grid, r - 1, c) #UP
        sinkIsland(grid, r + 1, c) #DOWN
        sinkIsland(grid, r, c - 1) #LEFT
        sinkIsland(grid, r, c + 1) #RIGHT