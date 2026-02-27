class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        start = []
        for r in range(ROW): 
            for c in range(COL): 
                if board[r][c] == word[0]: 
                    start.append((r, c))


        # up, down, left, right
        directions = {(-1,0) : 'up', (1,0) : 'down', (0,-1): 'left', (0,1): 'right'}

        def dfs(r, c, idx, visited):
            # print(f"{r}\t{c}\t{idx}\t{sum(ord(board[r][c]) for r, c in visited) == sum(ord(s) for s in word)}")
            if idx == len(word):
                self.found = True 
                return True
            if (
                r < 0 or r >= ROW or 
                c < 0 or c >= COL or 
                board[r][c] != word[idx] or 
                (r,c) in visited
            ):
                return False

            visited.add((r,c))
            
            # explore neighbors 
            if dfs(r+1, c, idx+1, visited): return True
            if dfs(r-1, c, idx+1, visited): return True 
            if dfs(r, c+1, idx+1, visited): return True 
            if dfs(r, c-1, idx+1, visited): return True
            visited.remove((r,c))

            return False
            # print(found)  
        # print(start)
        for points in start: 
            r, c = points[0], points[1]
            if  dfs(r, c, 0,set()):
                return True 

        # print(res, strings)

        return False