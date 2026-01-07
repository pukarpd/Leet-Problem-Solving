class RecentCounter:
    def __init__(self): 
        self.queue = deque()

    def ping(self, t:int) ->int: 
        self.queue.append(t)

        # out with the old.
        while self.queue[0] < t - 3000: 
            self.queue.popleft()  
        
        return len(self.queue)

    #  more optimal solution


    # working solution, weird with test cases as there was one edge case. 
    # def __init__(self):
    #     self.queue = deque([0] * 3000)
    #     self.old_t = 0
    # def ping(self, t: int) -> int:
    #     range_t = [t-3000-1, t-1]

    #     if range_t[0] < 0: 
    #         self.queue[t-1] = 1 
                
    #     else: 
    #         popper = range_t[0] - self.old_t
    #         # print(popper)
    #         while popper != 0: 
    #             self.queue.popleft()
    #             self.queue.append(0)
    #             popper -= 1
    #         self.old_t = range_t[0]
    #         self.queue[(range_t[1] - range_t[0])-1] = 1 
        
    #     return self.queue.count(1)



        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)