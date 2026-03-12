class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # up, down, left, right
        directions = [(-1, 0), (1, 0) , (0, -1), (0, 1)]
        seen = set()

        def dfs(r, c):
            if r == (len(grid)) or c  == (len(grid[0])) or r < 0 or c < 0: 
                return 

            if (r,c) in seen: 
                return 
            
            if grid[r][c] == '0': 
                return 
            
            seen.add((r,c))
            for d in directions: 
                nr, nc = d[0], d[1]
                dfs(r + nr, c + nc)
        
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0 
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == '1' and (r,c) not in seen: 
                    islands += 1 
                    dfs(r,c)
        
        return islands

