class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        # best greedy approach readibility wise, the ordered hashmap is O(n)
        count = Counter(hand)
        hand.sort()
        for card in hand: 
            if count[card]: 
                for i in range(card, card + groupSize): 
                    if not count[i]: 
                        return False 
                    count[i] -= 1 
        
        return True 
        




        # O(n**2) solution yet again. 
        # hand2 = copy.deepcopy(hand)
        # hand2.sort()
        # cardCounter = Counter(hand)

        # res = []
        # for num in hand2:  
        #     if cardCounter[num] == 0:
        #         continue 
        #     temp = []
        #     size = copy.deepcopy(groupSize)
        #     if cardCounter[num] > 0: 
        #         temp.append(num)
        #         cardCounter[num] -= 1 
        #         size -= 1 
        #     while size >0 :
        #         if not temp: 
        #             break  
        #         elif temp[-1] +1 in cardCounter and cardCounter[temp[-1]+1] > 0: 
        #             val = temp[-1] + 1 
        #             temp.append(val)
        #             cardCounter[val] -= 1 
        #             size -= 1 
        #         else: 
        #             break
        #     if len(temp) > 0:
        #         res.append(temp)

        # return True if len(res) == groupSize else False
                


         


        




