class Solution:
    def intToRoman(self, num: int) -> str:
        itr = "1 4 5 9 10 40 50 90 100 400 500 900 1000"
        rti = "I IV V IX X XL L XC C CD D CM M"

        itr = itr.split(" ")
        itr = [int(i) for i in itr]

        rti = rti.split(" ")
        map = {itr[i]: rti[i] for i in range(len(itr)-1,-1,-1)}
        # print(map)
        res = []
        for k, v in map.items(): 
            while num >= k: 
                res.append(v)
                num -= k
        
        return ''.join(res)
            