class Solution:
    def simplifyPath(self, path: str) -> str:
        
        
        parts = path.split('/') # split into segments
        print(parts)
        # parts = [x for x in parts if x != '.' ]
        # parts = [x for x in parts if x != '']
        print(parts)       
        stack = []
        for p in parts:
            print(stack)
            if not p or p == '.':    # ignore empty segments and "."
                continue
            if p == '..':
                if stack:            # pop one directory if possible
                    stack.pop()
                # if stack empty and path is absolute, stay at root
            else:
                stack.append(p)      # normal directory -> push

        return '/' + '/'.join(stack)



        # much simpler solution using delimiter splitting (forgot about this)


        # parts = path.split('/')
        # stack = parts
        # res = []
        # print(parts)
        # k = 0
        # # initial dots removal

        # stack = [x for x in stack if x != '']
        # stack = [x for x in stack if x != '.']
        # print(stack)
        # dd_counter = 0
        # i = 0
        # while i < len(stack): 
        #     if dd_counter > 0 and stack[i] != '..': 
        #         while dd_counter * 2 != 0 or stack:
        #             dynamic_length = len(stack) 
        #             stack.remove(stack[i - 1]) 
        #             dd_counter -= 1  
        #     if not stack: 
        #         break
            
        #     if stack[i] == '..': 
        #         dd_counter += 1 
        #     i += 1 
            
        

        # if not res: 
        #     return '/'
        
        # resa = ''
        # for word in res[::-1]: 
        #     resa +='/'
        #     resa += word


        # return resa
        # while stack:
        #     # part of the delimeter split, python shows nothing when splitting if theres
        #     # nothing between each delimeter split.
        #     print(stack, res)
        #     if stack[-1] == '': 
        #         stack.pop()
            
        #     elif stack[-1] == '..': 
        #         stack.pop()
        #         stack.pop()
            
        #     # while True:
        #     #     if stack[-1] != '..' or not stack: 
        #     #         break
        #     #     k += 1 
        #     #     stack.pop()
        #     # while True: 
        #     #     if k == 0 or not stack: 
        #     #         break
        #     #     stack.pop()
        #     #     k-= 1 
                
        #     elif stack[-1] == '.':  
        #         stack.pop()
        #     else: 
        #         res.append(stack[-1])
        #         stack.pop()
        





















        # initial failed solution seeing the stack clue
        #  without implementing too miuch logic and cleaning. 
        # stack = list(path) 

        # hashmap = {3 : ['///', '//.', '/./', '/..'], 
        # 4 : ['////', '/../', '/./.', '//..', '///.', '/.//', '//./']}
        # # universal pop
        # if stack[-1] == '/': 
        #         stack.pop()
        
        # # edge cases handler that algorithm  wont handle
        # path2 = ''.join(stack)
        # if len(stack) == 2: 
        #     if path2 == "/.":
        #         stack.pop()

        # if len(stack) == 3: 
        #     for val in hashmap[3]:
        #         if path2 == val:  
        #             for i in range(len(hashmap[3][0])-1): 
        #                 stack.pop()

            
        # if len(stack) == 4:
        #     for val in hashmap[4]:  
        #         if path2 == val: 
        #             for i in range(len(hashmap[4][0])-1): 
        #                 stack.pop()

        # solution = []
        # # main algo
        # if len(stack) > 4: 

        #     # removal of the first single slash
            
        #     # First remove all double dots
        #     for i in range(len(stack)):  
        #         if stack[-1] == '.' and stack[-2] == '.': 
        #             while stack[-1] == '/' and stack[-2] != '/': 
        #                 stack.pop()    
        #         solution.append(stack[-1])
        #         stack.pop() 
        #     # then remove all singe dots 
        #     for i in range(len(stack)):  
        #         if stack[-1] == '.' and stack[-2] == '/': 
        #             stack.pop()
        #         solution.append(stack[-1])
        #         stack.pop() 

        #     # then remove all multiple slashes
        #     for i in range(len(stack)):
        #         if stack[-1] == '/' and stack[-2] != '/': 
        #             while stack[-1] == '/' and stack[-2] != '/': 
        #                 stack.pop()
        #         solution.append(stack[-1])
        #         stack.pop() 
        # # strategy: first remove the initial "/"
        # # then remove all the "."
        # #then remove all the repeating "/"
        # # then the result.
        # print(stack, solution)


             


            

