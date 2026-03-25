class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Key missing intuition: reverse the logic. Go from the ocean to cells not cells to oceans
        COLS, ROWS = len(heights[0]), len(heights)

        # valid indices of the borders, where pacific are the pacific border points and atlantic are the atlantic border points
        pacific_borders = [[0, i] for i in range(COLS)] + [[i, 0] for i in range(1, ROWS)]
        atlantic_borders = [[i, COLS-1] for i in range(ROWS)] + [[ROWS-1, i] for i in range(COLS-1)]
        # print(f"pacific:{pacific_borders}\natlantic:{atlantic_borders}")
        # sets 
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable_set): 
            reachable_set.add(tuple([r,c]))
            dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in dirs: 
                nr, nc = r + dr, c + dc 
                if (nr in range(ROWS) and 
                    nc in range(COLS) and 
                    (nr, nc) not in reachable_set and 
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable_set)

        for r, c in pacific_borders:
            dfs(r, c, pacific_reachable)

        for r, c in atlantic_borders: 
            dfs(r, c, atlantic_reachable )

        newSet = pacific_reachable & atlantic_reachable
        
        # print(f"pacific:{pacific_reachable}\natlantic:{atlantic_reachable}\nintersection:{newSet}")
        
        return [list(x) for x in newSet]

        
            

        # def dfs(r, c): 
        #     if r == ROWS or c == COLS or r < 0 or c < 0: 
        #         return 
            
        #     for dr, dc in 

            





        # Honest Attempt, didnt work. 
        # ROWS, COLS = len(heights), len(heights[0])
        
        # # borders for pacific and atlantic, less than is pacific, greater than is atlantic.
        # bottom, right = len(heights), len(heights[0])
        
        # directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        # self.res = set()        
        # self.seen_poa = set()
        # self.stack = []

        # def dfs(r, c, stack): 
        #     print(self.seen_poa)
        #     if (r == ROWS-1 or c == COLS-1 or r == 0 or c == 0): 
        #         if stack: 
        #             if stack[0] in self.seen_poa: 
        #                 self.res.add(stack[0])
        #                 self.seen_poa.remove(stack[0])
        #             else: 
        #                 self.seen_poa.add(stack[0])
        #         return
        #     for dr, dc in directions: 
        #         nr, nc = (r+dr), (c+dc)
        #         if (nr in range(ROWS) and 
        #             nc in range(COLS) and 
        #             heights[nr][nc] <= heights[r][c]):
        #             stack.append((r,c))
        #             print(stack)
        #             dfs(nr, nc, stack)
                    
            
        # for r in range(ROWS): 
        #     for c in range(COLS):
        #         dfs(r,c, [])

        # return [x for x in self.res]

                



            

            