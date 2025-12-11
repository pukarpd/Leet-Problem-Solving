class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # multiple failed attempts, neetcode solution
        stack = []

        for a in asteroids: 
            while stack and a < 0 and stack[-1] > 0: 
                diff = a + stack[-1]
                if diff < 0: 
                    stack.pop()
                elif diff > 0: 
                    a = 0 
                else: 
                    a = 0 
                    stack.pop()
            if a: 
                stack.append(a)
            

        # print(stack)
        return stack
        # # Simpler Solution, reframed as stack simulation.
        # stack = []
        # # base case of the first element traveling to the left. 
        # # if asteroids[0] < 0: 
        # #     stack.append(asteroids[0])
        # #     asteroids.pop(0)
        
        # for a in asteroids:
        #     if stack: 
        #         top = stack[-1]
        #         if top > 0 and a < 0: 
        #             if abs(top) > abs(a): 
        #                 continue 
        #             elif abs(top) < abs(a): 
        #                 stack.pop()
        #                 stack.append(a)
        #             elif abs(top) == abs(a): 
        #                 stack.pop()
        #                 continue
        #         else:
        #             stack.append(a)
        #     if not stack:  
        #         stack.append(a)

        # return stack 

                


        # Solution too complex, scrapped due to increased complexity but had basic logic flow. 
        # Passed basic test cases. 
        # res = []
        # asteroids1 = deepcopy(asteroids)
        # for a in asteroids1:
        #     f, s = asteroids1[-1], asteroids1[-2]
        #     print(f,s) 
        #     if f < 0 and s > 0:
        #         if abs(f) > abs(s):
        #             asteroids1.pop(-2)
        #         elif abs(f) < abs(s): 
        #             asteroids1.pop()
        #         else: 
        #             asteroids1.pop()
        #             asteroids1.pop()
        #     if f > 0 and s < 0: 
        #         if abs(f) > abs(s):
        #             asteroids1.pop(-2)
        #         elif abs(f) < abs(s): 
        #             asteroids1.pop()
        #         else: 
        #             asteroids1.pop()
        #             asteroids1.pop()
        #     if asteroids1 and f > 0 and s > 0: 
        #         res.append(asteroids1.pop())
        #         res.append(asteroids1.pop())
        #     t = asteroids1[-3] if len(asteroids) > 3 else -1
        #     if asteroids1 and f < 0 and s < 0 and t > 0:
        #         if abs(t) < abs(f): 
        #             res.append(asteroids1.pop())


        # print(res)
        # return asteroids1

        



