class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
      
        #move the stones first
        ROWS, COLS = len(box), len(box[0])

        for r in range(ROWS): 
            i = COLS -1 
            for c in range(COLS -1, -1, -1): 
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1 
                elif box[r][c] == "*": 
                    i = c - 1
                

        print(box)
        res = []

        j = 0
        while j < len(box[0]):
            temp = []
            for i in range(len(box) -1 , -1, -1): 
                temp.append(box[i][j])
            res.append(temp)
            j += 1 
        
        return res
        # return res  




            
