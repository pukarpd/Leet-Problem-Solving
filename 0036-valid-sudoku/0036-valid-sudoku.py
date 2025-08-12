class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        i = 0 
        j = 0 
        ctracker = {}

        for row in board: 
            print(row)

        while i < 9:
            while j < 9: 
                num = board[i][j]
                if num not in ctracker and num != ".": 
                    ctracker[num] = 1 
                elif num in ctracker: 
                    ctracker[num] += 2
                j += 1
            # print(ctracker)
            for key, value in ctracker.items():
                if value > 1:
                    return False
            ctracker = {}
            j = 0 
            i += 1 
        
        i = 0
        j = 0
        ctracker = {}
        while j < 9:
            while i < 9: 
                num = board[i][j]
                if num not in ctracker and num != ".": 
                    ctracker[num] = 1 
                elif num in ctracker: 
                    ctracker[num] += 2
                i += 1
            # print(ctracker)
            for key, value in ctracker.items():
                if value > 1:
                    return False
            ctracker = {}
            i = 0 
            j += 1 
        
       
        i = 0
        j = 0
        m = 3
        n = 3
        jtracker = 0
        itracker = 0
        ctracker = {}
        while m <= 9:
            print(m, itracker, jtracker)
            while n <= 9:
                i = itracker  
                while i < m:
                    j = jtracker
                    while j < n: 
                        num = board[i][j]
                        # print(i,j,num)
                        if num not in ctracker and num != ".": 
                            ctracker[num] = 1 
                        elif num in ctracker: 
                            ctracker[num] += 2
                        j += 1 
                    for key, value in ctracker.items():
                        if value > 1:
                            return False
                    print(ctracker)
                    i += 1
                jtracker += 3
                ctracker = {}
                # print("i = ", i ,"j:", j ,"jtracker: ", jtracker)
                n += 3
            itracker += 3
            jtracker = 0
            ctracker = {}
            m += 3
            n = 3

            

        return True
    
            
        
                 